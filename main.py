import logging
import sys
import subprocess
import antlr4
import shutil
import os

from grammar.DecafLexer import  DecafLexer
from grammar.DecafParser import DecafParser
from sym_table.sym_table_visitor import SymTableVisitor
from code_gen.code_gen_visitor import CodeGenVisitor


def main(**args):
    logging.basicConfig(level=logging.INFO)

    # Handle input file path
    input_path = args["file"]
    base_path, ext = os.path.splitext(input_path)
    filename = base_path.split("/")[-1]
    base_path = '/'.join(base_path.split("/")[:-1])

    if not ext:  # If no extension provided
        input_file_address = base_path + ".java"
    elif ext.lower() != ".java":
        logging.error("Input file must have .java extension")
        return
    else:
        input_file_address = input_path
    
    # Generate output paths
    output_file_address = base_path + "/" + filename + ".c"
    debug_file_address = base_path + "/" + filename + ".json"
    executable_file = base_path + "/" + filename
    assembly_file = base_path + "/" + filename + ".s"

    # Transpilation pipeline
    stream = antlr4.FileStream(fileName=input_file_address, encoding='utf8')
    lexer = DecafLexer(stream)
    token_stream = antlr4.CommonTokenStream(lexer)
    parser = DecafParser(token_stream)
    parse_tree = parser.goal()
    logging.info("Initializing Symbol Table Visitor.")
    symtable_visitor = SymTableVisitor()
    symtable_visitor.visit(parse_tree)
    
    code_gen_visitor = CodeGenVisitor(symbol_table=symtable_visitor.symTable.symbols)
    code_gen_visitor.visit(parse_tree)

    output = code_gen_visitor.output
    
    pretty = "\n".join(output)
    with open(output_file_address, "w") as file: 
        file.write(pretty)
    
    # Copy lib to output directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    array_wrapper_src = os.path.join(current_dir, 'lib', 'array_wrapper.h')
    output_dir = os.path.dirname(os.path.abspath(output_file_address))
    array_wrapper_dst = os.path.join(output_dir, 'array_wrapper.h')
    os.makedirs(output_dir, exist_ok=True)
    shutil.copy2(array_wrapper_src, array_wrapper_dst)
    
    # Generate optional assembly with array wrapper
    subprocess.run(['gcc', '-I.', '-S', output_file_address, '-o', assembly_file])
    
    # Compile to executable with array wrapper
    subprocess.run(['gcc', '-I.', output_file_address, '-o', executable_file])
    
    logging.info(f"Generated assembly: {assembly_file}")
    logging.info(f"Generated executable: {executable_file}")
    
    with open(debug_file_address, "w") as file: 
        file.write(str(symtable_visitor.symTable.print_table()).replace('\'', '"'))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <filename.java>")
        sys.exit(1)
    main(file=sys.argv[1])
