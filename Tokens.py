from enum import Enum

class TOKEN_DEFINTION(Enum):
    BOOL                    = ('💩' * 1 ).encode('unicode_escape')   # bool
    INT                     = ('💩' * 2 ).encode('unicode_escape')   # int
    FLOAT                   = ('💩' * 3 ).encode('unicode_escape')   # float
    STRING                  = ('💩' * 4 ).encode('unicode_escape')   # string
    TRUE                    = ('💩' * 5 ).encode('unicode_escape')   # true
    FALSE                   = ('💩' * 6 ).encode('unicode_escape')   # false
    ADDITION                = ('💩' * 7 ).encode('unicode_escape')   # +
    SUBTRACTION             = ('💩' * 8 ).encode('unicode_escape')   # -
    MULTIPLICATION          = ('💩' * 9 ).encode('unicode_escape')   # *
    DIVISION                = ('💩' * 10).encode('unicode_escape')    # /
    IS                      = ('💩' * 11).encode('unicode_escape')    # is
    EQUALTO                 = ('💩' * 12).encode('unicode_escape')    # ==
    NOTEQUAL                = ('💩' * 13).encode('unicode_escape')    # !=
    GREATERTHAN             = ('💩' * 14).encode('unicode_escape')    # >
    GREATERTHANOREQUALTO    = ('💩' * 15).encode('unicode_escape')    # >=
    LESSTHAN                = ('💩' * 16).encode('unicode_escape')    # <
    LESSTHANOREQUALTO       = ('💩' * 17).encode('unicode_escape')    # <=
    LOGICALNOT              = ('💩' * 18).encode('unicode_escape')    # !
    LOGICALAND              = ('💩' * 19).encode('unicode_escape')    # &&
    LOGICALOR               = ('💩' * 20).encode('unicode_escape')    # ||
    LEFTROUNDBRACKET        = ('💩' * 21).encode('unicode_escape')    # (
    RIGHTROUNDBRACKET       = ('💩' * 22).encode('unicode_escape')    # )
    LEFTSQUAREBRACKET       = ('💩' * 23).encode('unicode_escape')    # [
    RIGHTSQUAREBRACKET      = ('💩' * 24).encode('unicode_escape')    # ]
    LEFTANGLEBRACKET        = ('💩' * 25).encode('unicode_escape')    # <
    RIGHTANGLEBRACKET       = ('💩' * 26).encode('unicode_escape')    # >
    LEFTCURLYBRACKET        = ('💩' * 27).encode('unicode_escape')    # {
    RIGHTCURLYBRACKET       = ('💩' * 28).encode('unicode_escape')    # }
    COMMA                   = ('💩' * 29).encode('unicode_escape')    # ,
    SEMICOLON               = ('💩' * 30).encode('unicode_escape')    # ;
    IF                      = ('💩' * 31).encode('unicode_escape')    # if
    ELSEIF                  = ('💩' * 32).encode('unicode_escape')    # elseif
    ELSE                    = ('💩' * 33).encode('unicode_escape')    # else
    WHILE                   = ('💩' * 34).encode('unicode_escape')    # while
    PRINT                   = ('💩' * 35).encode('unicode_escape')    # print
    RETURN                  = ('💩' * 36).encode('unicode_escape')    # return
    VARIABLE                = ('💩' * 37).encode('unicode_escape')    # variable
    DIGIT                   = ('💩' * 38).encode('unicode_escape')    # digit
    EOF                     = ('💩' * 39).encode('unicode_escape')    # EOF
    COMMENT                 = ('@')                                   # COMMENT
    STRING_VALUE_START      = ('"')                                   # STRING_VALUE_START

from typing import NamedTuple

class TOKEN_DATA(NamedTuple):
    line_nr : int
    char_pos: int

class TOKEN(NamedTuple):
    type    : TOKEN_DEFINTION
    value   : any  # type: ignore
    tkn_data: TOKEN_DATA