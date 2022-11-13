from dataclasses import dataclass
from typing import List
from Tokens import TOKEN, TOKEN_DATA, TOKEN_DEFINTION
import operator

@dataclass
class Lexer:
    '''Lexer class that translates a string into a list with tokens'''
    
    # get_next_digit :: str -> str
    def get_next_digit(self, data: str) -> str:
        """returns the next digit from a string

        Args:
            data (str): A random string

        Returns:
            str: the next full digit or decimal number
        """
        if data == '':
            return ''
        
        if data[0].isdigit() or data[0] == '.' :
            return data[0] + self.get_next_digit(data[1:])
        
        return ''

    # get_next_word :: str -> str
    def get_next_word(self, data: str) -> str:
        """Returns the next word of a string

        Args:
            data (str): A random string

        Returns:
            str: The next word in the given string
        """
        if len(data) > 0:
            if data != '' and data[0].isalpha() or data[0] == '💩':
                return data[0] + self.get_next_word(data[1:])
            if data[0] == '"':
                substr = data[0:data.rfind('"') + 1]
                return substr
        return ''

    # get_next_token :: str -> TokenData -> List[Token]
    def get_token_list(self, data: str, tkn_data: TOKEN_DATA = TOKEN_DATA(1,1)) -> List[TOKEN]:
        """get a list of tokens from a string.

        Args:
            data (str): A string following poopie text syntax
            token_data (TokenData, optional): The line and character of the token. Defaults to TokenData(1,1).

        Raises:
            Exception: Illegal Character
            Exception: Invalid or no Existing Token

        Returns:
            List[Token]: A list of tokens in the string
        """
        unicode_poopie = "\U0001f4a9"
        result_token: TOKEN = None  # type: ignore
        result_string: str = None  # type: ignore
                
        if data == "" or data is None:
            result_token = TOKEN(TOKEN_DEFINTION.EOF, result_string, tkn_data)
            return [result_token]
        
        #Skipping comment lines that start with @
        if data[0] == '@':
            while data[0] != '\n':
                data = data[1:]
            return self.get_token_list(data, tkn_data)

        # Check if first char in data is a digit and get the full digit string
        # then check if the digit string is an integer or float and fill result_token with the corresponding TOKEN_DEFINTION
        elif data[0].isdigit():
            result_string = self.get_next_digit(data)
            if result_string.isdigit():
                result_token = TOKEN(TOKEN_DEFINTION.DIGIT, int(result_string), tkn_data)
            elif result_string.count('.') == 1:
                result_token = TOKEN(TOKEN_DEFINTION.DIGIT, float(result_string), tkn_data)
            else:
                raise Exception(f"Illegal digit '{result_string}'")            

        elif data[0].isalpha() or data[0] == unicode_poopie or data[0] == '"':
            result_string = self.get_next_word(data)
            
            match result_string.encode('unicode_escape'):
                case TOKEN_DEFINTION.BOOL.value:
                    result_token = TOKEN(TOKEN_DEFINTION.BOOL, bool, tkn_data)
                case TOKEN_DEFINTION.INT.value:
                    result_token = TOKEN(TOKEN_DEFINTION.INT, int, tkn_data)
                case TOKEN_DEFINTION.FLOAT.value:
                    result_token = TOKEN(TOKEN_DEFINTION.FLOAT, float, tkn_data)
                case TOKEN_DEFINTION.TRUE.value:
                    result_token = TOKEN(TOKEN_DEFINTION.TRUE, True, tkn_data)
                case TOKEN_DEFINTION.FALSE.value:
                    result_token = TOKEN(TOKEN_DEFINTION.FALSE, False, tkn_data)
                case TOKEN_DEFINTION.ADDITION.value:
                    result_token = TOKEN(TOKEN_DEFINTION.ADDITION, operator.add, tkn_data)
                case TOKEN_DEFINTION.SUBTRACTION.value:
                    result_token = TOKEN(TOKEN_DEFINTION.SUBTRACTION, operator.sub, tkn_data)
                case TOKEN_DEFINTION.MULTIPLICATION.value:
                    result_token = TOKEN(TOKEN_DEFINTION.MULTIPLICATION, operator.mul, tkn_data)
                case TOKEN_DEFINTION.DIVISION.value:
                    result_token = TOKEN(TOKEN_DEFINTION.DIVISION, operator.truediv, tkn_data)
                case TOKEN_DEFINTION.IS.value:
                    result_token = TOKEN(TOKEN_DEFINTION.IS, None, tkn_data)
                case TOKEN_DEFINTION.EQUALTO.value:
                    result_token = TOKEN(TOKEN_DEFINTION.EQUALTO, operator.eq, tkn_data)
                case TOKEN_DEFINTION.NOTEQUAL.value:
                    result_token = TOKEN(TOKEN_DEFINTION.NOTEQUAL, operator.ne, tkn_data)
                case TOKEN_DEFINTION.GREATERTHAN.value:
                    result_token = TOKEN(TOKEN_DEFINTION.GREATERTHAN, operator.gt, tkn_data)
                case TOKEN_DEFINTION.GREATERTHANOREQUALTO.value:
                    result_token = TOKEN(TOKEN_DEFINTION.GREATERTHANOREQUALTO, operator.ge, tkn_data)
                case TOKEN_DEFINTION.LESSTHAN.value:
                    result_token = TOKEN(TOKEN_DEFINTION.LESSTHAN, operator.lt, tkn_data)
                case TOKEN_DEFINTION.LESSTHANOREQUALTO.value:
                    result_token = TOKEN(TOKEN_DEFINTION.LESSTHANOREQUALTO, operator.le, tkn_data)
                case TOKEN_DEFINTION.LOGICALNOT.value:
                    result_token = TOKEN(TOKEN_DEFINTION.LOGICALNOT, operator.not_, tkn_data)
                case TOKEN_DEFINTION.LOGICALAND.value:
                    result_token = TOKEN(TOKEN_DEFINTION.LOGICALAND, operator.and_, tkn_data)
                case TOKEN_DEFINTION.LOGICALOR.value:
                    result_token = TOKEN(TOKEN_DEFINTION.LOGICALOR, operator.or_, tkn_data)
                case TOKEN_DEFINTION.IF.value:
                    result_token = TOKEN(TOKEN_DEFINTION.IF, result_string, tkn_data)
                case TOKEN_DEFINTION.ELSEIF.value:
                    result_token = TOKEN(TOKEN_DEFINTION.ELSEIF, result_string, tkn_data)
                case TOKEN_DEFINTION.ELSE.value:
                    result_token = TOKEN(TOKEN_DEFINTION.ELSE, result_string, tkn_data)
                case TOKEN_DEFINTION.WHILE.value:
                    result_token = TOKEN(TOKEN_DEFINTION.WHILE, result_string, tkn_data)
                case TOKEN_DEFINTION.PRINT.value:
                    result_token = TOKEN(TOKEN_DEFINTION.PRINT, result_string, tkn_data)
                case TOKEN_DEFINTION.RETURN.value:
                    result_token = TOKEN(TOKEN_DEFINTION.RETURN, result_string, tkn_data)
                case TOKEN_DEFINTION.SEMICOLON.value:
                    result_token = TOKEN(TOKEN_DEFINTION.SEMICOLON, result_string, tkn_data)
                case TOKEN_DEFINTION.LEFTROUNDBRACKET.value:
                    result_token = TOKEN(TOKEN_DEFINTION.LEFTROUNDBRACKET, result_string, tkn_data)
                case TOKEN_DEFINTION.RIGHTROUNDBRACKET.value:
                    result_token = TOKEN(TOKEN_DEFINTION.RIGHTROUNDBRACKET, result_string, tkn_data)
                case TOKEN_DEFINTION.LEFTSQUAREBRACKET.value:
                    result_token = TOKEN(TOKEN_DEFINTION.LEFTSQUAREBRACKET, result_string, tkn_data)
                case TOKEN_DEFINTION.RIGHTSQUAREBRACKET.value:
                    result_token = TOKEN(TOKEN_DEFINTION.RIGHTSQUAREBRACKET, result_string, tkn_data)
                case TOKEN_DEFINTION.LEFTANGLEBRACKET.value:
                    result_token = TOKEN(TOKEN_DEFINTION.LEFTANGLEBRACKET, result_string, tkn_data)
                case TOKEN_DEFINTION.RIGHTANGLEBRACKET.value:
                    result_token = TOKEN(TOKEN_DEFINTION.RIGHTANGLEBRACKET, result_string, tkn_data)
                case TOKEN_DEFINTION.LEFTCURLYBRACKET.value:
                    result_token = TOKEN(TOKEN_DEFINTION.LEFTCURLYBRACKET, result_string, tkn_data)
                case TOKEN_DEFINTION.RIGHTCURLYBRACKET.value:
                    result_token = TOKEN(TOKEN_DEFINTION.RIGHTCURLYBRACKET, result_string, tkn_data)
                case TOKEN_DEFINTION.COMMA.value:
                    result_token = TOKEN(TOKEN_DEFINTION.COMMA, result_string, tkn_data)
                case TOKEN_DEFINTION.STRING.value:
                    result_token = TOKEN(TOKEN_DEFINTION.STRING, str, tkn_data)
                # case TOKEN_DEFINTION.STRING_VALUE_START.value:
                #     result_token = TOKEN(TOKEN_DEFINTION.STRING_VALUE_START, result_string, tkn_data)
                case _:
                    if result_string.startswith('"'):
                        result_token = TOKEN(TOKEN_DEFINTION.STRING_VALUE_START, result_string.replace('"',''), tkn_data)
                    else:
                        result_token = TOKEN(TOKEN_DEFINTION.VARIABLE, result_string, tkn_data)
                
        # Check if first char in data is a space or a newline character
        # then change the TokenData accordingly and call this function recursively with the next char
        elif data[0].isspace():
            if data[0] == '\n':
                tkn_data = TOKEN_DATA(tkn_data.line_nr + 1, 1)            
            tkn_data = TOKEN_DATA(tkn_data.line_nr, tkn_data.char_pos + 1)
            return self.get_token_list(data[1:], tkn_data)
                
        # Check if result_string or result_token is None, then give an error message
        if result_string is None or result_token is None:
            raise Exception(f'Error: Invalid token: {result_string} or {result_token}')

        # First change token_data based on the result_string and then call this function recursively with the next char
        length_result_string = len(result_string)

        nw_tkn_data: TOKEN_DATA = TOKEN_DATA(tkn_data.line_nr, tkn_data.char_pos + length_result_string)

        return [result_token] + self.get_token_list(data[length_result_string:], nw_tkn_data)

if __name__ == '__main__':
    with open('FileExamples/poopies.moji', 'r', encoding="utf-8") as file:
       data = file.read()
    token_list = Lexer().get_token_list(data)
    for token in token_list:
        print(token.type)
