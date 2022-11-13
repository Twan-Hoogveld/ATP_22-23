from Parser import *
from Lexer import *
from Runner import *
from Declarations import *
from Tester import *
import sys

def run_nodes(node_list):
    lib = CodeRunner({},[""])
    list(
        map(
            lambda x:
                x.run(lib), node_list
            )
        )
    return lib

if __name__ == '__main__':

    #get the arugments from the command line
    args = sys.argv[1:]
    fileName = ""
    if len(args) > 0:
        fileName = "_" + args[0]
    
    if len(args) > 1:
        DEBUG = args[1]
    else:
        DEBUG = False

    with open(f'FileExamples/poopies{fileName}.moji', 'r', encoding="utf-8") as file:
        data = file.read()
    
    token_list = Lexer().get_token_list(data)
    node_list, token_list = Parser().get_node_list(token_list)
    
    results = run_nodes(node_list)
