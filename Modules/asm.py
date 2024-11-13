from dataclasses import dataclass

# a class to hold the data for the code
@dataclass
class Code:
  language : str
  code : str
  ext : str

def codegen(syntaxTree) -> Code:
  final_code = ""

  for statement in syntaxTree.statements:
    


  code = Code('x86 Assembly', final_code, '.asm')
  return code
