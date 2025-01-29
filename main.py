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
    logging.info("Reading the file")
    input_file_address = args["file"] + ".java"
    output_file_address = args["file"] + ".c"
    debug_file_address = args["file"] + ".json"
     
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
 
    # Compile C code to executable
    executable_file = args["file"]
    assembly_file = args["file"] + ".s"
    
    # Copy array_wrapper.h to output directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    array_wrapper_src = os.path.join(current_dir, 'lib', 'array_wrapper.h')
    array_wrapper_dst = os.path.join(os.path.dirname(output_file_address), 'array_wrapper.h')
    shutil.copy2(array_wrapper_src, array_wrapper_dst)
    
    # Generate assembly with array wrapper
    subprocess.run(['gcc', '-I.', '-S', output_file_address, '-o', assembly_file])
    
    # Compile to executable with array wrapper
    subprocess.run(['gcc', '-I.', output_file_address, '-o', executable_file])
    
    logging.info(f"Generated assembly: {assembly_file}")
    logging.info(f"Generated executable: {executable_file}")
    
    with open(debug_file_address, "w") as file: 
        file.write(str(symtable_visitor.symTable.print_table()).replace('\'', '"'))
        
    
    # Add this line    # Step 6: Create an instance of DesignMetrics listener class
    # my_listener = DesignMetrics()
    # Step 7: Create a walker to traverse the parse tree and callback our listener
    # walker = antlr4.ParseTreeWalker()
    # walker.walk(t=parse_tree, listener=my_listener)

    # Step 8: Getting the results

if __name__ == "__main__":
    main(file=f"tests/{sys.argv[1]}")
