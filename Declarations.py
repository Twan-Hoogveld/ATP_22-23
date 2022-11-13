from abc import ABC, abstractmethod
from typing import Callable, List, Tuple, Union
from Runner import *
from dataclasses import dataclass

def DEBUG_DECORATOR(func: Callable) -> Callable:
    """A debug decorator for the Run function of all nodes. This helps the user to see what node is running in what order.

    Args:
        func (Callable): The run function of a Node

    Returns:
        Callable: Returns the run function of a Node or the wrapper inside this function
    """
    def wrapper(*args, **kwargs):
        print(f"\033[92mRunning node:\033[0m {args[0]}")
        return func(*args, **kwargs)
    
    DEBUG = False
    if DEBUG:
        return wrapper
    return func

@dataclass
class NODE(ABC):
    """Abstract class for all nodes in the AST.

    Args:
        ABC (_type_): Asbsract class inheritance
    """

    def __init__(self) -> None:
        super().__init__()
    
    @abstractmethod
    def run(self, CodeRunner: CodeRunner) -> None:
        """Runs the node and excecute/run nested nodes

        Args:
            Runner (Runner): The Runner for variable and function storage
        """
        return

@dataclass
class VALUE(NODE):
    '''Class for single values in the code'''
    value : any  # type: ignore
    
    @DEBUG_DECORATOR
    def run(self, CodeRunner: CodeRunner):
        return self.value

@dataclass
class VAR_DECLARATION(NODE):
    '''Class for variable declarations in the code'''
    return_type : type
    name : str

    @DEBUG_DECORATOR
    def run(self, CodeRunner: CodeRunner):
        if CodeRunner.key_exists(self.name):
            raise Exception(f"Variable {self.name} declared somewhere else.")
        CodeRunner[self.name] = None

class VAR_DEFINITON(NODE):
    '''Class for variable definitions in the code'''
    def __init__(self, return_type : type, name : str, value : NODE):
        self.return_type = return_type
        self.name = name
        self.value = value
        
        #Check if the node supports a value type check
        try:
            #try and check if the type is valid
            try:
                self.return_type(self.value.value)  # type: ignore
            except (ValueError, TypeError):
                raise Exception(f"Type {self.return_type} does not match type {type(self.value.value)}. Found {self.return_type}")  # type: ignore
        except AttributeError:
            pass
            
    @DEBUG_DECORATOR
    def run(self, CodeRunner: CodeRunner):
        return_value = self.value.run(CodeRunner)
        CodeRunner[self.name] = return_value

@dataclass
class VAR_ASSIGNMENT(NODE):
    '''Class for variable assignments in the code'''
    name : str
    value : NODE

    @DEBUG_DECORATOR
    def run(self, CodeRunner: CodeRunner):
        if not CodeRunner.key_exists(self.name):
            raise Exception(f"Variable {self.name} is not declared.")
        CodeRunner[self.name] = self.value.run(CodeRunner)
  
@dataclass   
class VAR_CALL(NODE):
    '''Class for variable calls in the code'''
    name : str

    @DEBUG_DECORATOR
    def run(self, CodeRunner: CodeRunner):
        if not self.name in CodeRunner:
            raise Exception(f"Variable {self.name} is not declared.")
        return CodeRunner[self.name]

@dataclass
class FUNC_DECLARATION(NODE):
    '''Node for function declarations in the code'''
    name : str
    return_type : type
    parameters : List[VAR_DECLARATION]

    @DEBUG_DECORATOR
    def run(self, CodeRunner: CodeRunner):
        CodeRunner.set_location(self.name) # Set the location of the Runner to the function
        CodeRunner['__return_type__'] = self.return_type # Set the return type of the function
        CodeRunner['__parameters__'] = self.parameters # Set the parameter nodes of the function
        CodeRunner.pop_location() # Remove the location of the Runner to the function

@dataclass
class FUNC_DEFINITION(NODE):
    '''Node for function def in the code'''
    name : str
    return_type : type
    parameters : List[VAR_DECLARATION]
    body : List[NODE]

    @DEBUG_DECORATOR
    def run(self, CodeRunner: CodeRunner):        
        CodeRunner.set_location(self.name) # Set the location of the Runner to the function
        CodeRunner['__return_type__'] = self.return_type # Set the return type of the function
        CodeRunner['__parameters__'] = self.parameters # Set the parameter nodes of the function
        list(map(lambda x: CodeRunner.set_value(x.name, x.run(CodeRunner)), self.parameters)) # Fill the Runner with the parameters.
        CodeRunner['__body__'] = self.body # Set the body of the function
        CodeRunner.pop_location() # Remove the location of the Runner to the function

@dataclass
class FUNC_CALL(NODE):
    '''Node for function calls in the code'''
    name : str
    parameters : List[Union[VAR_CALL, VALUE]]

    def run_body(self, body: List[NODE], CodeRunner: CodeRunner):
        if len(body) == 0: # If the body is empty, return None
            CodeRunner.pop_location()
            return None
        body[0].run(CodeRunner)
        if '__return_value__' in CodeRunner: # If the function returns a value, return it
            return_value = CodeRunner.pop('__return_value__')
            CodeRunner.pop_location()
            return return_value
        return self.run_body(body[1:], CodeRunner) # Otherwise, run the next line of the body

    @DEBUG_DECORATOR
    def run(self, CodeRunner: CodeRunner):
        if not CodeRunner.key_exists(self.name):
            raise Exception(f"Function {self.name} is not declared.")
        
        # Get the value of every parameter in this function call
        parameter_values = list(map(lambda x: x.run(CodeRunner), self.parameters))
        # Set the location to this function call
        CodeRunner.set_location(self.name)
        # Zip the names of the parameters with the corresponding values
        parameter_name_value_zip: Tuple[List[VAR_DECLARATION], any] = zip(CodeRunner['__parameters__'], parameter_values)  # type: ignore


        if not '__body__' in CodeRunner:
            raise Exception(f"Function {self.name} is declared but never defined.")
        if not len(self.parameters) == len(CodeRunner['__parameters__']):
            raise Exception(f"Function {self.name} is declared with {len(CodeRunner['__parameters__'])} parameters but called with {len(self.parameters)} parameters.")
        # if not all(map(lambda x: type(x[1]) is type(x[0]), parameter_name_value_zip)):
        #     raise Exception(f"Function {self.name} is declared with parameters of type {type(Runner['__parameters__'][0])} but called with parameters of type {type(self.parameters[0])}.")
        # Set the values of the parameters in the Runner
        list(map(lambda x: CodeRunner.set_value(x[0].name, x[1]), parameter_name_value_zip))

        return self.run_body(CodeRunner['__body__'], CodeRunner)

@dataclass
class EXPRESSION(NODE):
    '''Node for expressions in the code'''
    lhs : NODE
    expression_type : Callable
    rhs : NODE

    @DEBUG_DECORATOR
    def run(self, CodeRunner: CodeRunner):
        return self.expression_type(self.lhs.run(CodeRunner), self.rhs.run(CodeRunner)) # Run the expression

@dataclass
class CONDITION(NODE):
    '''Node for if blocks in the code'''
    expression : EXPRESSION
    body : List[NODE]

    @DEBUG_DECORATOR
    def run(self, CodeRunner: CodeRunner):
        if self.expression.run(CodeRunner): # If the expression is true
            list(map(lambda x: x.run(CodeRunner), self.body)) # Run the body

@dataclass
class RETURN(NODE):
    '''Node for returns in the code'''
    value : NODE

    @DEBUG_DECORATOR
    def run(self, CodeRunner: CodeRunner):
        if not '__return_type__' in CodeRunner:
            pass
        if not type(CodeRunner['__return_type__']) is type(self.value): 
            pass
        CodeRunner['__return_value__'] = self.value.run(CodeRunner) # Set the return value

@dataclass
class WHILE(NODE):
    '''Node for while loops in the code'''
    expression : EXPRESSION
    body : List[NODE]

    @DEBUG_DECORATOR
    def run(self, CodeRunner: CodeRunner):
        if self.expression.run(CodeRunner): # If the expression is true
            list(map(lambda x: x.run(CodeRunner), self.body)) # Run the body
            self.run(CodeRunner) # Run this node again

@dataclass
class PRINT(NODE):
    '''Node for prints in the code'''
    value : NODE

    @DEBUG_DECORATOR
    def run(self, CodeRunner: CodeRunner):
        # Print an empty line if the value is None, otherwise print the value
        print(self.value.run(CodeRunner) if self.value else '')