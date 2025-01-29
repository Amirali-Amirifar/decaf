from enum import EnumType

from grammar.DecafParser import DecafParser
from grammar.DecafVisitor import DecafVisitor



class MyVisitor(DecafVisitor):
    def __init__(self):
        super().__init__()
        self.symbols = {}

    def visitMainClass(self, ctx:DecafParser.MainClassContext):
        main_class_name = ctx.Identifier(0)
        main_method_args_name = ctx.Identifier(1)
        print(main_class_name)
        print(main_method_args_name)
