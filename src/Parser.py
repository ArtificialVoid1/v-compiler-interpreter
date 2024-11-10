from Token import TokenType, Token
from AST import *


class Parser:
    __current : int = 0
    __line : int = 1
    __MethodLevel = 0
    
    __scopes = []
    
    
    #--------- Constructor -------------
    
    def __init__(self, tokens):
        self.__tokens = tokens
        self.__program = program()
    
    #--------- Helper Functions -------------
    
    @staticmethod
    def __isAlpha(char):
        return str.isalpha(char) or char == '_'
    
    @staticmethod
    def __isNumber(char):
        return str.isnumeric(char)
    
    @staticmethod
    def __findVarInScope(varLexeme : str, scope : list[Any]):
        if varLexeme in scope:
            return True
        else:
            return False
    
    def __peek(self, amount = 1):
        return self.__tokens[self.__current + amount]
    
    def __advance(self):
        self.__current += 1
        return self.__peek(0)
    
    def __check(self, type):
        return self.__peek().Type == type
    
    def __isAtEnd(self):
        return self.__tokens[self.__current].Type == TokenType.EOF
    
    #--------- Parser Functions -------------
    
    def _parseExpression(self, expr : str, parent : Any):
        pass
    
    def _parse(self, parent):
        token = self.__peek(0)
        
        
        if token.Type == TokenType.IDENTIFIER: 
            
            #IDENTIFIER BLOCK
            
            
            if self.__check(TokenType.LEFT_PAREN): 
                
                # CALL
                
                identifier = token.Lexeme
                self.__advance() #consume identifier
                self.__advance() #consume (
                
                expectedLine = token.Line
                
                args = ""
                
                while self.__peek(0).Type != TokenType.RIGHT_PAREN and self.__peek(0).Line == expectedLine:
                    token = self.__peek(0)
                    args += token.Lexeme
                    self.__advance()

                    if self.__peek(0).Line != expectedLine:
                        raise SyntaxError('Invalid Syntax')
                
                exprArgs = args.split(',')
                
                newcall = Call(identifier, exprArgs, parent)
                return newcall
            
            
            
            
            if self.__check(TokenType.EQUAL):
                
                #Variable block
                
                varname = token.Lexeme
                self.__advance() #consume identifier
                self.__advance() #consume =
                
                finalValue = ""
                expectedLine = token.Line
                
                while self.__peek(0) != TokenType.SEMICOLON and self.__peek(0).Line == expectedLine:
                    token = self.__peek(0)
                    finalValue += token.Lexeme
                    self.__advance()
                
                expr = finalValue
                
                if self.__findVarInScope(varname, parent.scope):
                    newvar = VariableAssignment(varname, expr, parent)
                    return newvar
                else:
                    newvar = VariableDeclaration(varname, expr, parent)
                    return newvar
            
            
            
            
            
            elif token.Type == TokenType.NUMBER:
                pass
                # Expression Block
            
            elif token.Type == TokenType.STRING:
                pass
                # STRING Block
        
        
        
        elif token.Line != self.__peek().Line:
            self.__line += 1
            return None
    
    
    
    
    
    
    
    
    
    def parseTokens(self) -> program:
        
        while not self.__isAtEnd():
            statement = self._parse(self.__program)
            if statement != None:
                self.__program.add_statement(statement)
            self.__advance()
        
        self.__program.add_statement('EOF')
        return self.__program

