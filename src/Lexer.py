from Token import TokenType, Token



class Scanner:
    __start : int = 0
    __current : int = 0
    __line : int = 1
    
    #---------- Contructor ------------
    
    def __init__(self, source):
        self.__tokens = []
        self.__source = source
    
    
    #---------- Helper Functions ------------
    
    @staticmethod
    def __isAlpha(char):
        return str.isalpha(char) or char == '_'
    
    @staticmethod
    def __isNumber(char):
        return str.isnumeric(char)
    
    @staticmethod
    def __isAlphaNumeric(char):
        return Scanner.__isAlpha(char) or Scanner.__isNumber(char)
    
    def __isAtEnd(self):
        return self.__current >= len(self.__source)
    
    def __advance(self):
        self.__current += 1
        return self.__source[self.__current : self.__current + 1]
    
    def __addToken(self, Type : TokenType, Literal = None):
        text = self.__source[self.__start : self.__current + 1]
        
        if str.startswith(text, '\n') == True:
            text = str.replace(text, ' ', '')
        
        self.__tokens.append(
            Token(Type, text, Literal, self.__line)
        )
    
    def __peek(self, amount = 1):
        if self.__isAtEnd() == True:
            return '\n'
        else:
            return self.__source[self.__current+amount : self.__current+amount+1]
    
    def __match(self, expected_char):
        if self.__peek() == expected_char:
            return True
        else:
            return False
    
    #---------- Lexer  ------------
    
    def _number(self):
        while str.isnumeric(self.__peek()) != False:
            self.__advance()
        if self.__peek() == '.' and str.isnumeric(self.__peek(2)) != False:
            self.__advance()
        
        while str.isnumeric(self.__peek()) != False:
            self.__advance()
        
        self.__addToken(TokenType.NUMBER, float(self.__source[self.__start + 1: self.__current + 1]))
    
    def _string(self):
        while self.__peek() != '"' and self.__peek() != "'" and not self.__isAtEnd() == True:
            if self.__peek() == '\n':
                self.__line += 1
            self.__advance()
        
        self.__advance()
        
        value = self.__source[self.__start + 2 : self.__current]
        self.__addToken(TokenType.STRING, value)
    
    def _identifier(self):
        while self.__isAlphaNumeric(self.__peek()):
            self.__advance()
        ident = self.__source[self.__start : self.__current + 1]
        
        if ident == 'true':
            self.__addToken(TokenType.TRUE)
        elif ident == 'false':
            self.__addToken(TokenType.FALSE)
        elif ident == 'null':
            self.__addToken(TokenType.NULL)
        else:
            self.__addToken(TokenType.IDENTIFIER)
    
    def _scan(self):
        char = self.__advance()
        
        match char:
            case '\n': self.__line += 1
            case '\t': pass
            case '': pass
            case ' ': pass
            
            case '(': self.__addToken(TokenType.LEFT_PAREN)
            case ')': self.__addToken(TokenType.RIGHT_PAREN)
            case '{': self.__addToken(TokenType.LEFT_BRACE)
            case '}': self.__addToken(TokenType.RIGHT_BRACE)
            case '[': self.__addToken(TokenType.RIGHT_BRACKET)
            case ']': self.__addToken(TokenType.LEFT_BRACKET)
            
            case ',': self.__addToken(TokenType.COMMA)
            case '.': self.__addToken(TokenType.DOT)
            case ':': self.__addToken(TokenType.COLON)
            case ';': self.__addToken(TokenType.SEMICOLON)
            case '~': self.__addToken(TokenType.TILDE)
            
            case '=': self.__addToken(TokenType.EQUAL)
            
            case '"': self._string()
            case "'": self._string()
            
            case _:
                if self.__isNumber(char):
                    self._number()
                elif self.__isAlpha(char):
                    self._identifier()
                else:
                    raise SyntaxError('Unexpected Symbol: ' + char)

    def scanSource(self) -> list[Token]:
        while not self.__isAtEnd() == True:
            self.__start = self.__current
            self._scan()
        
        self.__tokens.append(
            Token(
                TokenType.EOF,
                None,
                None,
                self.__line
            )
        )
        return self.__tokens