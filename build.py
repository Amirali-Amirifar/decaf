import logging
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, List

import antlr4
from grammar.DecafLexer import DecafLexer
from grammar.DecafParser import DecafParser
from sym_table.sym_table_visitor import SymTableVisitor
from code_gen.code_gen_visitor import CodeGenVisitor


@dataclass
class FileConfig:
    input_path: Path
    output_dir: Path
    filename: str

    @property
    def input_file(self) -> Path:
        return self.input_path

    @property
    def output_c_file(self) -> Path:
        return self.output_dir / f"{self.filename}.c"

    @property
    def debug_file(self) -> Path:
        return self.output_dir / f"{self.filename}.json"

    @property
    def executable_file(self) -> Path:
        return self.output_dir / self.filename

    @property
    def assembly_file(self) -> Path:
        return self.output_dir / f"{self.filename}.s"


class JavaToCTranspiler:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def setup_file_config(self, input_path: str) -> Optional[FileConfig]:
        """Set up file paths and validate input file."""
        path = Path(input_path)

        if not path.suffix:
            path = path.with_suffix('.java')
        elif path.suffix.lower() != '.java':
            self.logger.error("Input file must have .java extension")
            return None

        return FileConfig(
            input_path=path,
            output_dir=path.parent,
            filename=path.stem
        )

    def parse_java(self, input_file: Path) -> Optional[tuple[antlr4.tree.Tree, SymTableVisitor]]:
        """Parse Java source code and generate AST."""
        try:
            stream = antlr4.FileStream(str(input_file), encoding='utf8')
            lexer = DecafLexer(stream)
            token_stream = antlr4.CommonTokenStream(lexer)
            parser = DecafParser(token_stream)
            parse_tree = parser.goal()

            self.logger.info("Initializing Symbol Table Visitor")
            symtable_visitor = SymTableVisitor()
            symtable_visitor.visit(parse_tree)

            return parse_tree, symtable_visitor
        except Exception as e:
            self.logger.error(f"Error parsing Java file: {e}")
            return None

    def generate_c_code(self, parse_tree: antlr4.tree.Tree, symbol_table: dict) -> Optional[List[str]]:
        """Generate C code from the AST."""
        try:
            code_gen_visitor = CodeGenVisitor(symbol_table=symbol_table)
            code_gen_visitor.visit(parse_tree)
            return code_gen_visitor.output
        except Exception as e:
            self.logger.error(f"Error generating C code: {e}")
            return None

    def copy_array_wrapper(self, output_dir: Path):
        """Copy array wrapper header to output directory."""
        try:
            current_dir = Path(__file__).parent
            array_wrapper_src = current_dir / 'lib' / 'array_wrapper.h'
            array_wrapper_dst = output_dir / 'array_wrapper.h'
            output_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(array_wrapper_src, array_wrapper_dst)
        except Exception as e:
            self.logger.error(f"Error copying array wrapper: {e}")

    def compile_output(self, config: FileConfig):
        """Compile the generated C code to assembly and executable."""
        try:
            # Generate assembly
            subprocess.run(['gcc', '-I.', '-S', str(config.output_c_file),
                            '-o', str(config.assembly_file)], check=True)
            self.logger.info(f"Generated assembly: {config.assembly_file}")

            # Generate executable
            subprocess.run(['gcc', '-I.', str(config.output_c_file),
                            '-o', str(config.executable_file)], check=True)
            self.logger.info(f"Generated executable: {config.executable_file}")
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Compilation failed: {e}")
        except Exception as e:
            self.logger.error(f"Error during compilation: {e}")

    def transpile(self, input_path: str) -> bool:
        """Main transpilation pipeline."""
        # Setup and validate files
        config = self.setup_file_config(input_path)
        if not config:
            return False

        # Parse Java code
        parse_result = self.parse_java(config.input_file)
        if not parse_result:
            return False
        parse_tree, symtable_visitor = parse_result

        # Generate C code
        c_code = self.generate_c_code(parse_tree, symtable_visitor.symTable.symbols)
        if not c_code:
            return False

        # Write C code to file
        try:
            config.output_dir.mkdir(parents=True, exist_ok=True)
            config.output_c_file.write_text('\n'.join(c_code))

            # Write debug info
            debug_info = str(symtable_visitor.symTable.print_table()).replace('\'', '"')
            config.debug_file.write_text(debug_info)
        except Exception as e:
            self.logger.error(f"Error writing output files: {e}")
            return False

        # Copy array wrapper and compile
        self.copy_array_wrapper(config.output_dir)
        self.compile_output(config)
        return True
