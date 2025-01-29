import logging
from dataclasses import dataclass
from typing import Dict, Optional, List


@dataclass
class Symbol:
    name: str
    type: str
    scope: str
    is_initialized: bool = False
    line_number: int = 0
    # For methods/functions
    parameters: List[Dict[str, str]] = None
    return_type: Optional[str] = None
    # For classes
    parent_class: Optional[str] = None
    full_name: Optional[str] = None
    # For arrays
    is_array: bool = False
    
    def __repr__(self) -> str:
        details = {}
        if self.name:
            details["name"] = self.name
        if self.type:
            details["type"] = self.type
        if self.full_name:
            details["full_name"] = self.full_name
        if self.parameters:
            details["parameters"] = self.parameters
        if self.return_type:
            details["return_type"] = self.return_type
        if self.parent_class:
            details["parent_class"] = self.parent_class
        if self.is_array:
            details["is_array"] = True
        return str(details)

class SymbolTable:
    def __init__(self):
        self.symbols: Dict[str, Dict[str, Symbol]] = {}
        self.current_scope = "global"
        self.scope_stack = ["global"]
        self.symbols["global"] = {}
        
        # Configure logger
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.DEBUG)
        
        # Remove any existing handlers to prevent duplicates
        self.logger.handlers = []
        
        # Create console handler with detailed formatting
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - [%(levelname)s] - %(message)s - {Scope: %(scope)s}')
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)
        
        # Prevent propagation to root logger
        self.logger.propagate = False
        
    def enter_scope(self, scope_name: str):
        """Enter a new scope (e.g., class, method, or block)"""
        new_scope = f"{self.current_scope}.{scope_name}"
        self.logger.info(f"Entering scope {new_scope}", extra={'scope': new_scope})
        self.scope_stack.append(new_scope)
        self.current_scope = new_scope
        self.symbols[self.current_scope] = {}

    def exit_scope(self):
        """Exit the current scope"""
        old_scope = self.current_scope
        self.scope_stack.pop()
        self.current_scope = self.scope_stack[-1]
        self.logger.info(f"Exiting scope {old_scope}", extra={'scope': self.current_scope})

    def insert(self, name: str, type: str, line_number: int = 0, **kwargs) -> bool:
        """Insert a symbol into the current scope"""
        if self.lookup_in_current_scope(name):
            self.logger.error(f"Symbol '{name}' already exists in current scope", extra={'scope': self.current_scope})
            return False

        symbol = Symbol(
            name=name,
            type=type,
            scope=self.current_scope,
            line_number=line_number,
            **kwargs
        )
        self.symbols[self.current_scope][name] = symbol
        self.logger.info(
            f"Inserted symbol: {name} (Type: {type})",
            extra={
                'scope': self.current_scope,
                'line_number': line_number,
                'symbol_details': str(kwargs)
            }
        )
        return True

    def lookup(self, name: str) -> Optional[Symbol]:
        """Look up a symbol in current and enclosing scopes"""
        for scope in reversed(self.scope_stack):
            if scope in self.symbols and name in self.symbols[scope]:
                symbol = self.symbols[scope][name]
                self.logger.debug(
                    f"Found symbol '{name}' in scope {scope}",
                    extra={'scope': scope, 'symbol_type': symbol.type}
                )
                return symbol
        
        self.logger.warning(
            f"Symbol '{name}' not found in any accessible scope",
            extra={'scope': self.current_scope, 'searched_scopes': str(self.scope_stack)}
        )
        return None

    def lookup_in_current_scope(self, name: str) -> Optional[Symbol]:
        """Look up a symbol in only the current scope"""
        if self.current_scope in self.symbols:
            symbol = self.symbols[self.current_scope].get(name)
            if symbol:
                self.logger.debug(
                    f"Found symbol '{name}' in current scope",
                    extra={'scope': self.current_scope, 'symbol_type': symbol.type}
                )
                return symbol
        return None

    def declare_class(self, name: str, parent_class: Optional[str] = None, line_number: int = 0):
        """Declare a class in the symbol table"""
        # Construct full class name based on current scope
        full_class_name = f"global.{name}"
            
        self.logger.info(f"Declaring class {full_class_name}", extra={'scope': self.current_scope})
        
        # Check for duplicate class declaration using full name
        if self.lookup(name):
            self.logger.error(f"Class {full_class_name} already declared", 
                             extra={'scope': self.current_scope})
            return False
            
        # Validate parent class if specified
        if parent_class:
            parent_symbol = self.lookup(parent_class)
            if not parent_symbol or parent_symbol.type != "class":
                self.logger.error(f"Parent class '{parent_class}' not found or not a class",
                                extra={'scope': self.current_scope})
                return False
                
        # Store the full class name in the symbol
        return self.insert(name, "class", line_number, 
                          parent_class=parent_class, 
                          full_name=full_class_name)

    def declare_method(self, name: str, return_type: str, parameters: List[Dict[str, str]], line_number: int = 0):
        """Declare a method in the symbol table"""
        if return_type != "void" and not self.is_valid_type(return_type):
            self.logger.error(
                f"Invalid return type: {return_type}",
                extra={'scope': self.current_scope, 'method': name}
            )
            return False
        
        for param in parameters:
            for param_name, param_type in param.items():
                if not self.is_valid_type(param_type):
                    self.logger.error(
                        f"Invalid parameter type: {param_type} for parameter {param_name}",
                        extra={'scope': self.current_scope, 'method': name}
                    )
                    return False
        
        self.logger.info(
            f"Declaring method: {name} -> {return_type}",
            extra={
                'scope': self.current_scope,
                'parameters': str(parameters)
            }
        )
        return self.insert(name, "method", line_number, return_type=return_type, parameters=parameters)

    def declare_variable(self, name: str, type_str: str, line_number: int = 0, is_array: bool = False):
        """Declare a variable in the symbol table"""
        if not self.is_valid_type(type_str):
            self.logger.error(
                f"Invalid variable type: {type_str}",
                extra={'scope': self.current_scope, 'variable': name}
            )
            return False
            
        self.logger.info(
            f"Declaring variable: {name}: {type_str}",
            extra={
                'scope': self.current_scope,
                'is_array': is_array
            }
        )
        return self.insert(name, type_str, line_number, is_array=is_array)

    def is_valid_type(self, type_str: str) -> bool:
        """Check if a type is valid"""
        basic_types = {'int', 'boolean', 'int[]', 'String[]'}
        if type_str in basic_types:
            return True
            
        # Check if it's a declared class type
        class_symbol = self.lookup(type_str)
        if class_symbol and class_symbol.type == 'class':
            return True
            
        self.logger.warning(f"Invalid type: {type_str}", extra={'scope': self.current_scope})
        return False

    def get_method_signature(self, class_name: str, method_name: str) -> Optional[Symbol]:
        """Get method signature from a class (including inherited methods)"""
        class_symbol = self.lookup(class_name)
        if not class_symbol:
            return None

        # Check current class
        method_scope = f"{self.current_scope}.{class_name}"
        if method_scope in self.symbols and method_name in self.symbols[method_scope]:
            return self.symbols[method_scope][method_name]

        # Check parent class if exists
        if class_symbol.parent_class:
            return self.get_method_signature(class_symbol.parent_class, method_name)
        
        return None

    def print_table(self):
        """Print the entire symbol table in a readable format"""
        import json
        
        formatted_table = {}
        for scope, symbols in self.symbols.items():
            # Include all scopes, even empty ones
            formatted_table[scope] = {}
            for name, symbol in symbols.items():
                # Convert the symbol representation to a dictionary
                symbol_dict = eval(str(symbol))
                formatted_table[scope][name] = symbol_dict
        
        self.logger.info(
            "Symbol Table Contents:\n" + 
            json.dumps(formatted_table, indent=2, sort_keys=True),
            extra={'scope': self.current_scope}
        )
        return formatted_table