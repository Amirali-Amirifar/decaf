# Decaf Compiler

A compiler implementation for the Decaf programming language, which is a subset of Java. This compiler translates Decaf source code into C code, providing object-oriented programming features in a simplified context.

## Project Architecture

The compiler is organized into several main components:

### 1. Grammar Definition (grammar/Decaf.g4)

The project uses ANTLR4 for lexical analysis and parsing. The grammar defines:
- Object-oriented programming constructs
- Basic control structures (if-else, while)
- Array operations
- Method declarations and invocations
- Expression handling (arithmetic, logical, method calls)

Key features:
- Class declarations with inheritance support
- Main class requirement
- Type system (int, boolean, arrays, user-defined types)
- Method parameter handling

### 2. Symbol Table Management (sym_table/)

The symbol table implementation provides scope management and symbol tracking:

- Hierarchical scope handling (global, class, method, block)
- Symbol attributes tracking:
  - Name and type information
  - Scope information
  - Initialization status
  - Method parameters and return types
  - Class inheritance information
  - Array type handling

### 3. Code Generation (code_gen/)

The code generator translates Decaf to C code using a visitor pattern:

- Class translation to C structs
- Virtual method table (vtable) generation for inheritance
- Constructor generation
- Method implementation
- Expression evaluation
- Statement translation
- Array operations support

## Features

- Object-oriented programming support
- Inheritance with virtual method tables
- Array operations with bounds checking
- Type checking and scope analysis
- Memory management
- Error reporting and logging

## Implementation Details

1. **Grammar Processing**:
   - ANTLR4 generates lexer and parser
   - Supports Java-like syntax
   - Handles expressions with operator precedence

2. **Symbol Management**:
   - Scope-based symbol tracking
   - Type checking support
   - Inheritance chain validation
   - Method overriding verification

3. **Code Generation**:
   - C code generation with struct-based objects
   - Virtual method table implementation
   - Constructor chaining for inheritance
   - Array bounds checking
   - Standard library integration

