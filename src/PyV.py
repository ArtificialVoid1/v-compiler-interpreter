from Lexer import Scanner


def __GenerateSyntaxTree(source : str):
    scanner = Scanner(source)
    tokens = scanner.scanSource()
    
    for token in tokens:
        print(token)

def compile(source : str):
    Ast = __GenerateSyntaxTree(source)
    #generate assembly
    
def interpret(source : str) -> None:
    Ast = __GenerateSyntaxTree(source)
    #run code