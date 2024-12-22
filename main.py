import sys

import antlr4

from grammar.DecafLexer import  DecafLexer
from grammar.DecafParser import DecafParser
from visitor import MyVisitor


def main(**args):
    # Step 1: Load input source into the stream object
    stream = antlr4.FileStream(fileName=args["file"], encoding='utf8')

    # Step 2: Create an instance of AssignmentStLexer
    lexer = DecafLexer(stream)

    # Step 3: Convert the input source into a list of tokens
    token_stream = antlr4.CommonTokenStream(lexer)

    # Step 4: Create an instance of the AssignmentStParser
    parser = DecafParser(token_stream)

    # Step 5: Create parse tree
    parse_tree = parser.goal()

    # Step 6: Create an instance of DesignMetrics listener class
    # my_listener = DesignMetrics()
    my_visitor = MyVisitor()
    my_visitor.visit(parse_tree)
    # Step 7: Create a walker to traverse the parse tree and callback our listener
    walker = antlr4.ParseTreeWalker()
    # walker.walk(t=parse_tree, listener=my_listener)

    # Step 8: Getting the results
    # print(f'DSC={my_listener.get_design_size}')


if __name__ == "__main__":
    main(file="test.java")
