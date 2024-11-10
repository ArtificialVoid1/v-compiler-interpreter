from enum import Enum
from typing import Any
from dataclasses import dataclass

class TokenType(Enum):
    LEFT_PAREN = 0
    RIGHT_PAREN = 1
    
    LEFT_BRACKET = 2
    RIGHT_BRACKET = 3
    
    LEFT_BRACE = 4
    RIGHT_BRACE = 5
    
    DOT = 26
    COMMA = 27
    HASH = 28
    DOLLAR = 29
    AMP = 30
    TILDE = 31
    PIPE = 32
    COLON = 33
    SEMICOLON = 35
    
    PLUS = 12
    MINUS = 13
    STAR = 14
    SLASH = 15
    CARAT = 16
    MOD = 17
    
    EQUAL = 18
    EQUAL_EQUAL = 19
    GREATER = 20
    GREATER_EQUAL = 21
    LESS = 22
    LESS_EQUAL = 23
    BANG = 24
    BANG_EQUAL = 25
    
    IDENTIFIER = 6
    STRING = 7
    NUMBER = 8
    
    TRUE = 9
    FALSE = 10
    NULL = 11
    
    EOF = 34
    

@dataclass
class Token:
    Type : TokenType
    Lexeme : str | None
    Literal : Any
    Line : int
    
    def __str__(self):
        return self.Type.name + ' ' + str(self.Lexeme) + ' ' + str(self.Literal) + ', Line: ' + str(self.Line)