from Token import TokenType, Token



class Scanner:
    __start : int = 0
    __current : int = 0
    __stop : int = 1
    
    def __IsAtEnd(self):
        
    
    
    
    def __init__(self, source):
        self.__tokens = []
        self.__source = source
        
        
    def scanSource(self, source):
        