from typing import TypedDict

prefix = "__decaf__"
class ConstantTypes(TypedDict):
    init_function_name: str
    
consts: ConstantTypes = {
    'init_function_name': 'init'
}

def get_constant(key: ConstantTypes.keys):
    return prefix + consts[key]