import unittest
from Parser import *
from Lexer import *
from Runner import *
from Declarations import *
import random
import sys

def run_nodes(node_list):
    lib = CodeRunner({},[""])
    list(map( lambda x: x.run(lib), node_list))
    return lib

def load_data_from_file(fileName : str = ""):
    if fileName != "":
        fileName = "_" + fileName
    
    with open(f'FileExamples/poopies{fileName}.moji', 'r', encoding="utf-8") as file:
        data = file.read()

    token_list : List[TOKEN] = Lexer().get_token_list(data)
    node_list, token_list = Parser().get_node_list(token_list)
    results = run_nodes(node_list)
    
    return token_list,node_list,results

def load_data_from_string(data : str):
    token_list = Lexer().get_token_list(data)
    #Copy for later on in the testing.
    token_list2 = token_list.copy()
    node_list, token_list = Parser().get_node_list(token_list)
    results = run_nodes(node_list)
    
    return token_list2,node_list,results

def test_template_addition(value1 : int = 10, value2 : int = 20, resultVar : str  = 'resultVariable'):
    line =  f"💩💩 x 💩💩💩💩💩💩💩💩💩💩💩 {value1} 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 \n"
    line += f"💩💩 y 💩💩💩💩💩💩💩💩💩💩💩 {value2} 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 \n"
    line += f"💩💩 {resultVar} 💩💩💩💩💩💩💩💩💩💩💩 x 💩💩💩💩💩💩💩 y 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 \n"
    return load_data_from_string(line), value1 + value2

def test_template_substraction(value1 : int = 70, value2 : int = 20, resultVar : str = 'resultVariable'):
    line =  f"💩💩 x 💩💩💩💩💩💩💩💩💩💩💩 {value1} 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 \n"
    line += f"💩💩 y 💩💩💩💩💩💩💩💩💩💩💩 {value2} 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 \n"
    line += f"💩💩 {resultVar} 💩💩💩💩💩💩💩💩💩💩💩 x 💩💩💩💩💩💩💩💩 y 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 \n"
    return load_data_from_string(line), value1 - value2

def test_template_multiplication(value1 : int = 10, value2 : int  = 20, resultVar : str = 'resultVariable'):
    line =  f"💩💩 x 💩💩💩💩💩💩💩💩💩💩💩 {value1} 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 \n"
    line += f"💩💩 y 💩💩💩💩💩💩💩💩💩💩💩 {value2} 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 \n"
    line += f"💩💩 {resultVar} 💩💩💩💩💩💩💩💩💩💩💩 x 💩💩💩💩💩💩💩💩💩 y 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 \n"
    return load_data_from_string(line), value1 * value2

def test_template_division(value1 : int = 100, value2 : int  = 20, resultVar : str = 'resultVariable'):
    line =  f"💩💩 x 💩💩💩💩💩💩💩💩💩💩💩 {value1} 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 \n"
    line += f"💩💩 y 💩💩💩💩💩💩💩💩💩💩💩 {value2} 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 \n"
    line += f"💩💩 {resultVar} 💩💩💩💩💩💩💩💩💩💩💩 x 💩💩💩💩💩💩💩💩💩💩 y 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 \n"
    return load_data_from_string(line), value1 / value2

#Code in python
def sommig(n):
    result = 0
    while(n>=1):
        result += n
        n-=1
    return result

#Code in Poopilang
def poopi_sommig(input0 = 3):
    line =  f"💩💩 sommig 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 💩💩 n 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 \n"
    line += f"  💩💩 result 💩💩💩💩💩💩💩💩💩💩💩 0 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 \n"
    line += f"  💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 n 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 1 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 \n"
    line += f"      result 💩💩💩💩💩💩💩💩💩💩💩 result 💩💩💩💩💩💩💩 n 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 \n"
    line += f"      n 💩💩💩💩💩💩💩💩💩💩💩 n 💩💩💩💩💩💩💩💩 1 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 \n"
    line += f"  💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 \n"
    line += f"  💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 result 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 \n"
    line += f"💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 \n"
    line += f"💩💩 x 💩💩💩💩💩💩💩💩💩💩💩 sommig 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 {input0} 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 \n"
    _,_,result = load_data_from_string(line)
    return result.content.__getitem__('x')

#Code in Python
def evenOrUneven(n : int) -> bool:
    def oneven(n: int) -> bool:
        if n == 0:
            return False
        return even(n - 1)
            
    def even(n: int) -> bool:
        if n == 0:
            return True
        return oneven(n - 1)
            
    return oneven(n)

#Code in Poopilang
def poopi_evenOrUneven(input = 10):
    #function even
    line =  f"💩💩 even 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 💩💩 n 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 \n" # int even(int n){
    line += f"💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 n 💩💩💩💩💩💩💩💩💩💩💩💩 0 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 @if n == 0 \n" #if (n == 0) {
    line += f"  💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 💩💩💩💩💩 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 @return true \n" # return true ;
    line += f"  💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 \n" # }
    line += f"  💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 oneven 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 n 💩💩💩💩💩💩💩💩 1 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩  @return even(n - 1); \n" # return oneven ( n - 1 )
    line += f"  💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 \n" # }

#    #function oneven
    line +=  f"💩💩 oneven 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 💩💩 n 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 \n" # int oneven(int n){
    line +=  f"💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 n 💩💩💩💩💩💩💩💩💩💩💩💩 0 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 @if n == 0 \n" #if (n == 0) {
    line +=  f"  💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 💩💩💩💩💩💩 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 @return false \n" # return false ;
    line +=  f"  💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 \n" # }
    line += f"  💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 even 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 n 💩💩💩💩💩💩💩💩 1 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩  @return even(n - 1); \n" # return even ( n - 1 )
    line += f"  💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 \n" # }
    
    # #calling a function
    line += f"💩💩 ResultVariable 💩💩💩💩💩💩💩💩💩💩💩 oneven 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 {input} 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 \n"
    
    _,_,result = load_data_from_string(line)
    return result.content.__getitem__('ResultVariable')

class TEST_DATATYPES(unittest.TestCase):
    
    def test_correct_datatype(self, correctType = int):
        _,node_list,_ = load_data_from_file()
        for node in node_list:
            test_value = node.return_type == correctType  # type: ignore
            message = f"Node '{node.name}' is not an {correctType}!"  # type: ignore
            self.assertTrue(test_value,message)
            
    def test_pi(self, pi : float = 3.14159265359):
        line = f"💩💩💩 myFloat 💩💩💩💩💩💩💩💩💩💩💩 {pi} 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 \n"
        _,node_list,_ = load_data_from_string(line)
        for node in node_list:
            test_value = node.return_type == type(pi)  # type: ignore
            message = f"Node '{node.name}' is not an {type(pi)}!"  # type: ignore
            self.assertTrue(test_value,message)
    
    def test_string(self, myStr : str = '"Hello World!"'):
        line = f'💩💩💩💩 resultVariable 💩💩💩💩💩💩💩💩💩💩💩 {myStr} 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 \n'
        _,_,results  = load_data_from_string(line)
        self.assertEqual(results.content['resultVariable'],myStr.strip('"'))
        
    def test_nodes(self, input0 : int = 10):
        line =  f"💩💩 sommig 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 💩💩 n 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 \n"
        line += f"  💩💩 result 💩💩💩💩💩💩💩💩💩💩💩 0 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 \n"
        line += f"  💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 n 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 1 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 \n"
        line += f"      result 💩💩💩💩💩💩💩💩💩💩💩 result 💩💩💩💩💩💩💩 n 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 \n"
        line += f"      n 💩💩💩💩💩💩💩💩💩💩💩 n 💩💩💩💩💩💩💩💩 1 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 \n"
        line += f"  💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 \n"
        line += f"  💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 {input0} 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 \n"
        line += f"💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 \n"
             
        token_list,node_list,_ = load_data_from_string(line)
    
        # is the function an integer?
        self.assertEqual(node_list[0].__getattribute__('name'),'sommig')         
        self.assertEqual(node_list[0].__getattribute__('return_type'),int)

        # does the function return an int?
        self.assertEqual(node_list[0].__getattribute__('parameters')[0].__getattribute__('return_type'),int)        
        self.assertEqual(node_list[0].__getattribute__('parameters')[0].__getattribute__('name'),'n')
        
        # is n >= 1 ? 
        self.assertEqual(node_list[0].__getattribute__('body')[1].__getattribute__('expression').lhs.name,'n')
        self.assertEqual(node_list[0].__getattribute__('body')[1].__getattribute__('expression').expression_type,operator.__ge__)
        self.assertEqual(node_list[0].__getattribute__('body')[1].__getattribute__('expression').rhs.value,1)
        
        # is resulta a incremented by n ? 
        self.assertEqual(node_list[0].__getattribute__('body')[1].__getattribute__('body')[0].name,'result')
        self.assertEqual(node_list[0].__getattribute__('body')[1].__getattribute__('body')[0].value.lhs.name,'result')
        self.assertEqual(node_list[0].__getattribute__('body')[1].__getattribute__('body')[0].value.expression_type,operator.__add__)
        self.assertEqual(node_list[0].__getattribute__('body')[1].__getattribute__('body')[0].value.rhs.name,'n')

        #Is n substracted by 1?
        self.assertEqual(node_list[0].__getattribute__('body')[1].__getattribute__('body')[1].name,'n')
        self.assertEqual(node_list[0].__getattribute__('body')[1].__getattribute__('body')[1].value.lhs.name,'n')
        self.assertEqual(node_list[0].__getattribute__('body')[1].__getattribute__('body')[1].value.expression_type,operator.__sub__)
        self.assertEqual(node_list[0].__getattribute__('body')[1].__getattribute__('body')[1].value.rhs.value,1)
        
        #TESTING THE TOKENS
        # is the function an integer?
        self.assertEqual(node_list[0].__getattribute__('name'),'sommig')         
        self.assertEqual(node_list[0].__getattribute__('return_type'),int)

        # does the function return an int?
        self.assertEqual(node_list[0].__getattribute__('parameters')[0].__getattribute__('return_type'),int)        
        self.assertEqual(node_list[0].__getattribute__('parameters')[0].__getattribute__('name'),'n')
        
        # is n >= 1 ? 
        self.assertEqual(node_list[0].__getattribute__('body')[1].__getattribute__('expression').lhs.name,'n')
        self.assertEqual(node_list[0].__getattribute__('body')[1].__getattribute__('expression').expression_type,operator.__ge__)
        self.assertEqual(node_list[0].__getattribute__('body')[1].__getattribute__('expression').rhs.value,1)
        
        # is resulta a incremented by n ? 
        self.assertEqual(node_list[0].__getattribute__('body')[1].__getattribute__('body')[0].name,'result')
        self.assertEqual(node_list[0].__getattribute__('body')[1].__getattribute__('body')[0].value.lhs.name,'result')
        self.assertEqual(node_list[0].__getattribute__('body')[1].__getattribute__('body')[0].value.expression_type,operator.__add__)
        self.assertEqual(node_list[0].__getattribute__('body')[1].__getattribute__('body')[0].value.rhs.name,'n')

        #Is n substracted by 1?
        self.assertEqual(node_list[0].__getattribute__('body')[1].__getattribute__('body')[1].name,'n')
        self.assertEqual(node_list[0].__getattribute__('body')[1].__getattribute__('body')[1].value.lhs.name,'n')
        self.assertEqual(node_list[0].__getattribute__('body')[1].__getattribute__('body')[1].value.expression_type,operator.__sub__)
        self.assertEqual(node_list[0].__getattribute__('body')[1].__getattribute__('body')[1].value.rhs.value,1)

        #call to the function, is the input really the same as input0?
        self.assertEqual(node_list[0].__getattribute__('body')[2].value.value,input0)   
        
        EXPECTED_LIST_OF_TOKENS = [
            TOKEN_DEFINTION.INT,
            TOKEN_DEFINTION.VARIABLE,
            TOKEN_DEFINTION.LEFTROUNDBRACKET,
            TOKEN_DEFINTION.INT,
            TOKEN_DEFINTION.VARIABLE,
            TOKEN_DEFINTION.RIGHTROUNDBRACKET,
            TOKEN_DEFINTION.LEFTCURLYBRACKET,
            TOKEN_DEFINTION.INT,
            TOKEN_DEFINTION.VARIABLE,
            TOKEN_DEFINTION.IS,
            TOKEN_DEFINTION.DIGIT,
            TOKEN_DEFINTION.SEMICOLON,
            TOKEN_DEFINTION.WHILE,
            TOKEN_DEFINTION.LEFTROUNDBRACKET,
            TOKEN_DEFINTION.VARIABLE,
            TOKEN_DEFINTION.GREATERTHANOREQUALTO,
            TOKEN_DEFINTION.DIGIT,
            TOKEN_DEFINTION.RIGHTROUNDBRACKET,
            TOKEN_DEFINTION.LEFTCURLYBRACKET,
            TOKEN_DEFINTION.VARIABLE,
            TOKEN_DEFINTION.IS,
            TOKEN_DEFINTION.VARIABLE,
            TOKEN_DEFINTION.ADDITION,
            TOKEN_DEFINTION.VARIABLE,
            TOKEN_DEFINTION.SEMICOLON,
            TOKEN_DEFINTION.VARIABLE,
            TOKEN_DEFINTION.IS,
            TOKEN_DEFINTION.VARIABLE,
            TOKEN_DEFINTION.SUBTRACTION,
            TOKEN_DEFINTION.DIGIT,
            TOKEN_DEFINTION.SEMICOLON,
            TOKEN_DEFINTION.RIGHTCURLYBRACKET,
            TOKEN_DEFINTION.RETURN,
            TOKEN_DEFINTION.DIGIT,
            TOKEN_DEFINTION.SEMICOLON,
            TOKEN_DEFINTION.RIGHTCURLYBRACKET,
            TOKEN_DEFINTION.EOF]
        
        for token_found,token_needed  in zip(token_list,EXPECTED_LIST_OF_TOKENS):
            self.assertEqual(token_found.type,token_needed)

class TEST_BASIC_ARITHMETIC(unittest.TestCase):
    
    def test_addition(self):
        (_,_,results),expected_result = test_template_addition()
        self.assertEqual(results.content['resultVariable'],expected_result,f"Value of {'resultVariable'} is not {expected_result}!")

    def test_subtraction(self):
        (_,_,results),expected_result = test_template_substraction()
        self.assertEqual(results.content['resultVariable'],expected_result,f"Value of {'resultVariable'} is not {expected_result}!")
    
        (_,_,results),expected_result = test_template_substraction(value1 = 1234, value2 = 4321)
        self.assertEqual(results.content['resultVariable'],expected_result,f"Value of {'resultVariable'} is not {expected_result}!")

        (_,_,results),expected_result = test_template_substraction(value1 = 1000, value2 = 1000)
        self.assertEqual(results.content['resultVariable'],expected_result,f"Value of {'resultVariable'} is not {expected_result}!")
          
    def test_multiplication(self):
        (_,_,results),expected_result = test_template_multiplication()
        self.assertEqual(results.content['resultVariable'],expected_result,f"Value of {'resultVariable'} is not {expected_result}!")

        (_,_,results),_ = test_template_multiplication(value1= 100 , value2 = 100)
        expected_result = 10000
        self.assertEqual(results.content['resultVariable'],expected_result,f"Value of {'resultVariable'} is not {expected_result}!")
        
    def test_division(self):
        (_,_,results),expected_result = test_template_division()
        self.assertEqual(results.content['resultVariable'],expected_result,f"Value of {'resultVariable'} is not {expected_result}!")

        (_,_,results),expected_result = test_template_division(value1= 100 , value2 = 10)
        self.assertEqual(results.content['resultVariable'],expected_result,f"Value of {'resultVariable'} is not {expected_result}!")

class TEST_BASIC_FILE_LEXING_PARSING(unittest.TestCase):
    
    def test_basic_logic(self, valueTrue = "💩💩💩💩💩", valueFalse = "💩💩💩💩💩💩", result = True, resultVar = 'z'):
        #OR
        line =  f"💩 {resultVar} 💩💩💩💩💩💩💩💩💩💩💩 {valueTrue} 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 {valueFalse} 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩" 
        _,_,results = load_data_from_string(line)
        self.assertEqual(results.content[resultVar],result,f"Value of {resultVar} is not {result}")
        
        #AND
        line =  f"💩 {resultVar} 💩💩💩💩💩💩💩💩💩💩💩 {valueTrue} 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 {valueTrue} 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩" 
        line += f"@Dikke test string die eruit word gehaald!\n "
        _,_,results = load_data_from_string(line)
        self.assertEqual(results.content[resultVar],result,f"Value of {resultVar} is not {result}")

class TEST_FUNCTIONS(unittest.TestCase):
    
    #TEST
    def test_evenOrUneven(self):
        self.assertEqual(poopi_evenOrUneven(0), evenOrUneven(0))
        self.assertEqual(poopi_evenOrUneven(1), evenOrUneven(1))
        self.assertEqual(poopi_evenOrUneven(2), evenOrUneven(2))
        self.assertEqual(poopi_evenOrUneven(50), evenOrUneven(50))
        self.assertEqual(poopi_evenOrUneven(101), evenOrUneven(101))
        for _ in range(100):
            x = random.randint(1,100)
            self.assertEqual(poopi_evenOrUneven(x),evenOrUneven(x))
    
    #TEST
    def test_sommig(self):
        self.assertEqual(poopi_sommig(3),sommig(3)) 
        self.assertEqual(poopi_sommig(8),sommig(8)) 
        self.assertEqual(poopi_sommig(17),sommig(17)) 
        self.assertEqual(poopi_sommig(33),sommig(33))
        for _ in range(100):
            x = random.randint(1,100)
            self.assertEqual(poopi_sommig(x),sommig(x))

       
if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    unittest.main()