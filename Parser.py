from typing import List, Tuple
from Lexer import Lexer
from Tokens import TOKEN_DEFINTION, TOKEN
from Declarations import *

class Parser:
    """This Parser class is responsible to check all Tokens and convert them to a nested Nodes tree"""
    def get_parameters(self, TOKEN_LIST: List[TOKEN]) -> Tuple[List[VAR_DECLARATION], List[TOKEN]]:
        """# Returns a list of VAR_DECLERATION and a list of Tokens

        Args:
            TOKEN_LIST (List[Token]): A list of tokens provided by the Lexer class.

        Raises:
            Exception: No Variable Type

        Returns:
            Tuple[List[VAR_DECLERATION], List[Token]]: Returns a list with VAR_DECLERATION and the rest of the token list..
        """
        NODE_RESULT         : VAR_DECLARATION       = None  # type: ignore
        NODE_RESULT_LIST    : List[VAR_DECLARATION] = []

        if TOKEN_LIST[0].type == TOKEN_DEFINTION.RIGHTROUNDBRACKET:
            return [], TOKEN_LIST

        elif TOKEN_LIST[0].type in [TOKEN_DEFINTION.BOOL, TOKEN_DEFINTION.INT, TOKEN_DEFINTION.FLOAT]:
            variable_type: type = TOKEN_LIST.pop(0).value
            variable_name: str = TOKEN_LIST.pop(0).value

            if TOKEN_LIST[0].type == TOKEN_DEFINTION.COMMA: TOKEN_LIST.pop(0)
            NODE_RESULT = VAR_DECLARATION(variable_type, variable_name)
            NODE_RESULT_LIST, TOKEN_LIST = self.get_parameters(TOKEN_LIST)

        else:
            raise Exception("Expected variable type!")

        return [NODE_RESULT] + NODE_RESULT_LIST, TOKEN_LIST

    # get_next_node :: List[Token] -> Tuple[List[Node], List[Token]]
    def get_call_parameters(self, TOKEN_LIST: List[TOKEN]) -> Tuple[List[NODE], List[TOKEN]]:
        """Returns a list of Nodes for the FunctionCallNode and a list of Tokens

        Args:
            TOKEN_LIST (List[Token]): The TokenList from the Lexer

        Returns:
            Tuple[List[Node], List[Token]]: Returns a list of Nodes and a list of the unused Tokens
        """
        NODE_RESULT         : NODE          = None  # type: ignore
        NODE_RESULT_LIST    : List[NODE]    = []

        if TOKEN_LIST[0].type == TOKEN_DEFINTION.RIGHTROUNDBRACKET:
            return [], TOKEN_LIST
        else:
            NODE_RESULT, TOKEN_LIST = self.get_next_node(TOKEN_LIST)
            NODE_RESULT_LIST, TOKEN_LIST = self.get_call_parameters(TOKEN_LIST)
            return [NODE_RESULT] + NODE_RESULT_LIST, TOKEN_LIST
        
    # get_next_node :: List[Token] -> Tuple[Node, List[Token]]
    def get_next_node(self, TOKEN_LIST: List[TOKEN]) -> Tuple[NODE, List[TOKEN]]:
        """Finds the next node in a TokenList and returns it

        Args:
            TOKEN_LIST (List[Token]): Tokenlist from Lexer

        Raises:
            Exception: No variable name

        Returns:
            Tuple[Node, List[Token]]: The found Node and a List of unused Tokens
        """
        NODE_RESULT: NODE = None  # type: ignore
        # Check if TOKEN_LIST is empty. If so, return empty list
        if len(TOKEN_LIST) == 0:
            return None, TOKEN_LIST  # type: ignore

        # Check if the first token is a semicolon or EOF. If so pop it and call this function recursively.
        elif TOKEN_LIST[0].type in [TOKEN_DEFINTION.SEMICOLON, TOKEN_DEFINTION.EOF]:
            return None, TOKEN_LIST[1:]  # type: ignore

        # Check if the first token is a digit
        elif TOKEN_LIST[0].type in [TOKEN_DEFINTION.DIGIT, TOKEN_DEFINTION.TRUE, TOKEN_DEFINTION.FALSE]:
            NODE_RESULT = VALUE(TOKEN_LIST.pop(0).value)
        
        # Check if first token is a BOOL, INT, FLOAT
        elif TOKEN_LIST[0].type in [TOKEN_DEFINTION.BOOL, TOKEN_DEFINTION.INT, TOKEN_DEFINTION.FLOAT]:
            if TOKEN_LIST[1].type != TOKEN_DEFINTION.VARIABLE:
                raise Exception("Expected a variable name after the type")
            elif TOKEN_LIST[2].type == TOKEN_DEFINTION.SEMICOLON:
                # VAR_DECLERATION
                return_type: type = TOKEN_LIST.pop(0).value
                variable_name: str = TOKEN_LIST.pop(0).value
                NODE_RESULT = VAR_DECLARATION(return_type, variable_name)
            elif TOKEN_LIST[2].type == TOKEN_DEFINTION.IS:
                # VAR_DEFINITION
                return_type: type = TOKEN_LIST.pop(0).value
                variable_name: str = TOKEN_LIST.pop(0).value
                TOKEN_LIST.pop(0) # Remove TOKEN_DEFINTION.IS
                value, TOKEN_LIST= self.get_next_node(TOKEN_LIST)
                NODE_RESULT = VAR_DEFINITON(return_type, variable_name, value)
            elif TOKEN_LIST[2].type == TOKEN_DEFINTION.LEFTROUNDBRACKET:
                return_type: type = TOKEN_LIST.pop(0).value
                function_name: str = TOKEN_LIST.pop(0).value
                TOKEN_LIST.pop(0) # Remove TOKEN_DEFINTION.LEFTROUNDBRACKET
                parameter_list, TOKEN_LIST = self.get_parameters(TOKEN_LIST)
                TOKEN_LIST.pop(0) # Remove TOKEN_DEFINTION.RIGHTROUNDBRACKET
                if TOKEN_LIST[0].type == TOKEN_DEFINTION.LEFTCURLYBRACKET:
                    # FUNC_DEFINITION
                    TOKEN_LIST.pop(0) # Remove TOKEN_DEFINTION.LEFTCURLYBRACKET
                    body, TOKEN_LIST= self.get_node_list(TOKEN_LIST)
                    TOKEN_LIST.pop(0) # Remove TOKEN_DEFINTION.RIGHTCURLYBRACKET
                    NODE_RESULT = FUNC_DEFINITION(function_name, return_type, parameter_list, body)
                else:
                    # FUNC_DEFINITION
                    print(function_name, return_type, parameter_list)
                    NODE_RESULT = FUNC_DEFINITION(function_name, return_type, parameter_list)  # type: ignore
        
        elif TOKEN_LIST[0].type == TOKEN_DEFINTION.STRING:
            if TOKEN_LIST[1].type != TOKEN_DEFINTION.VARIABLE:
                raise Exception("Expected a variable name after the string type")
            elif TOKEN_LIST[2].type == TOKEN_DEFINTION.IS:
                # VAR_DEFINITION
                return_type: type = TOKEN_LIST.pop(0).value
                variable_name: str = TOKEN_LIST.pop(0).value
                TOKEN_LIST.pop(0) # Remove TOKEN_DEFINTION.IS
                value = VALUE(TOKEN_LIST.pop(0).value) #self.get_next_node(TOKEN_LIST)
                NODE_RESULT = VAR_DEFINITON(return_type, variable_name, value)

        # Check for TOKEN_VARIABLE
        elif TOKEN_LIST[0].type == TOKEN_DEFINTION.VARIABLE:
            if TOKEN_LIST[1].type == TOKEN_DEFINTION.LEFTROUNDBRACKET:
                # FUNC_CALL
                function_name: str = TOKEN_LIST.pop(0).value
                TOKEN_LIST.pop(0) # Remove TOKEN_DEFINTION.LEFTROUNDBRACKET
                parameter_list, TOKEN_LIST = self.get_call_parameters(TOKEN_LIST)
                TOKEN_LIST.pop(0) # Remove TOKEN_DEFINTION.RIGHTROUNDBRACKET
                NODE_RESULT = FUNC_CALL(function_name, parameter_list)  # type: ignore
            elif TOKEN_LIST[1].type == TOKEN_DEFINTION.IS:
                # VAR_ASSIGNMENT
                variable_name: str = TOKEN_LIST.pop(0).value
                TOKEN_LIST.pop(0) # Remove TOKEN_DEFINTION.IS
                value, TOKEN_LIST = self.get_next_node(TOKEN_LIST)
                NODE_RESULT = VAR_ASSIGNMENT(variable_name, value)
            else:
                # VAR_CALL
                variable_name: str = TOKEN_LIST.pop(0).value
                NODE_RESULT = VAR_CALL(variable_name)
        
        # if statement
        elif TOKEN_LIST[0].type == TOKEN_DEFINTION.IF:
            TOKEN_LIST.pop(0) # Remove TOKEN_DEFINTION.IF
            TOKEN_LIST.pop(0) # Remove TOKEN_DEFINTION.LEFTROUNDBRACKET
            condition, TOKEN_LIST = self.get_next_node(TOKEN_LIST)
            TOKEN_LIST.pop(0) # Remove TOKEN_DEFINTION.RIGHTROUNDBRACKET
            TOKEN_LIST.pop(0) # Remove TOKEN_DEFINTION.LEFTCURLYBRACKET
            body, TOKEN_LIST= self.get_node_list(TOKEN_LIST)
            TOKEN_LIST.pop(0) # Remove TOKEN_DEFINTION.RIGHTCURLYBRACKET
            NODE_RESULT = CONDITION(condition, body)  # type: ignore

        # While loop
        elif TOKEN_LIST[0].type == TOKEN_DEFINTION.WHILE:
            TOKEN_LIST.pop(0) # Remove TOKEN_DEFINTION.WHILE
            TOKEN_LIST.pop(0) # Remove TOKEN_DEFINTION.LEFTROUNDBRACKET
            condition, TOKEN_LIST = self.get_next_node(TOKEN_LIST)
            TOKEN_LIST.pop(0) # Remove TOKEN_DEFINTION.RIGHTROUNDBRACKET
            TOKEN_LIST.pop(0) # Remove TOKEN_DEFINTION.LEFTCURLYBRACKET
            body, TOKEN_LIST= self.get_node_list(TOKEN_LIST)
            TOKEN_LIST.pop(0) # Remove TOKEN_DEFINTION.RIGHTCURLYBRACKET
            NODE_RESULT = WHILE(condition, body)  # type: ignore

        # return statement
        elif TOKEN_LIST[0].type == TOKEN_DEFINTION.RETURN:
            TOKEN_LIST.pop(0) # Remove TOKEN_DEFINTION.RETURN
            return_node, TOKEN_LIST = self.get_next_node(TOKEN_LIST)
            NODE_RESULT = RETURN(return_node)

        # print statement
        elif TOKEN_LIST[0].type == TOKEN_DEFINTION.PRINT:
            TOKEN_LIST.pop(0) # Remove TOKEN_DEFINTION.PRINT
            TOKEN_LIST.pop(0) # Remove TOKEN_DEFINTION.LEFTROUNDBRACKET
            print_node, TOKEN_LIST = self.get_next_node(TOKEN_LIST)
            NODE_RESULT = PRINT(print_node)
            TOKEN_LIST.pop(0) # Remove TOKEN_DEFINTION.RIGHTROUNDBRACKET

        if len(TOKEN_LIST) == 0:
            return NODE_RESULT, TOKEN_LIST

        # checking for expressions
        if TOKEN_LIST[0].type in [TOKEN_DEFINTION.ADDITION, TOKEN_DEFINTION.SUBTRACTION, TOKEN_DEFINTION.MULTIPLICATION, TOKEN_DEFINTION.DIVISION, TOKEN_DEFINTION.EQUALTO, TOKEN_DEFINTION.NOTEQUAL, TOKEN_DEFINTION.GREATERTHAN, TOKEN_DEFINTION.GREATERTHANOREQUALTO, TOKEN_DEFINTION.LESSTHAN, TOKEN_DEFINTION.LESSTHANOREQUALTO,TOKEN_DEFINTION.LOGICALOR, TOKEN_DEFINTION.LOGICALAND, TOKEN_DEFINTION.LOGICALNOT]:
            lhs = NODE_RESULT
            conditional: Callable = TOKEN_LIST.pop(0).value
            rhs, TOKEN_LIST = self.get_next_node(TOKEN_LIST)
            NODE_RESULT = EXPRESSION(lhs, conditional, rhs)

        #check for semicolon
        if TOKEN_LIST[0].type == TOKEN_DEFINTION.SEMICOLON:
            TOKEN_LIST.pop(0)
                
        #return results
        return NODE_RESULT, TOKEN_LIST

    def get_node_list(self, TOKEN_LIST: List[TOKEN]) -> Tuple[List[NODE], List[TOKEN]]:
        """Gets a list of nodes from a token list.
        This functions ends when a EOF or RIGHTCURLYBRACKET token is found

        Args:
            TOKEN_LIST (List[Token]): List of tokens provided by the Lexer class

        Returns:
            Tuple[List[NODE], List[TOKEN]]: Returns a list of nodes found.
        """

        # Create a list to store the nodes
        NODE_RESULT     : NODE          = None  # type: ignore
        NODE_RESULT_LIST: List[NODE]    = []

        if len(TOKEN_LIST) == 0:
            return NODE_RESULT_LIST, TOKEN_LIST

        # if EOF or RIGHTCURLYBRACKET is found, return an empty list.
        if TOKEN_LIST[0].type in [TOKEN_DEFINTION.RIGHTCURLYBRACKET, TOKEN_DEFINTION.EOF]:
            return [], TOKEN_LIST

        else:
            NODE_RESULT, TOKEN_LIST = self.get_next_node(TOKEN_LIST)
            NODE_RESULT_LIST, TOKEN_LIST = self.get_node_list(TOKEN_LIST)
            return [NODE_RESULT] + NODE_RESULT_LIST, TOKEN_LIST

#Solely for testing purposes
if __name__ == '__main__':
    data = f'💩💩💩💩 myString 💩💩💩💩💩💩💩💩💩💩💩 "hello" 💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩💩 \n'
    tkns: List[TOKEN] = Lexer().get_token_list(data)
    node_list, TOKEN_LIST = Parser().get_node_list(tkns)