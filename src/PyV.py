from Lexer import Scanner
from Parser import Parser


def __GenerateSyntaxTree(source : str):
    scanner = Scanner(source)
    tokens = scanner.scanSource()
    
    parser = Parser(tokens)
    SyntaxTree = parser.parseTokens()
    
    for statement in SyntaxTree.statements:
        print(statement)

def compile(source : str):
    Ast = __GenerateSyntaxTree(source)
    #generate assembly
    
def interpret(source : str) -> None:
    Ast = __GenerateSyntaxTree(source)
    #run code
    
__GenerateSyntaxTree('print(a, b, c)')