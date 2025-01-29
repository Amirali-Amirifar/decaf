import logging
import sys
from symtable import symtable
import json
import antlr4

from grammar.DecafLexer import  DecafLexer
from grammar.DecafParser import DecafParser
from sym_table.sym_table_visitor import SymTableVisitor
from code_gen.code_gen_visitor import CodeGenVisitor


def main(**args):
    logging.basicConfig(level=logging.INFO)
    logging.info("Reading the file")
    stream = antlr4.FileStream(fileName=args["file"], encoding='utf8')
    lexer = DecafLexer(stream)
    token_stream = antlr4.CommonTokenStream(lexer)
    parser = DecafParser(token_stream)
    parse_tree = parser.goal()
    # logging.info("Initializing Symbol Table Visitor.")
    # symtable_visitor = SymTableVisitor()
    # symtable_visitor.visit(parse_tree)
    # symtable_visitor.symTable.print_table() 
    
    code_gen_visitor = CodeGenVisitor()
    code_gen_visitor.visit(parse_tree)

    output = code_gen_visitor.output
    
    print("\n".join(output))
    
    # Add this line    # Step 6: Create an instance of DesignMetrics listener class
    # my_listener = DesignMetrics()
    # Step 7: Create a walker to traverse the parse tree and callback our listener
    # walker = antlr4.ParseTreeWalker()
    # walker.walk(t=parse_tree, listener=my_listener)

    # Step 8: Getting the results

if __name__ == "__main__":
    main(file=f"tests/{sys.argv[1]}.java")
