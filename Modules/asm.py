from dataclasses import dataclass

# a class to hold the data for the code
@dataclass
class Code:
  language : str
  code : str
  ext : str

#--------------- Keywords

MOV = 'mov '
JMP = 'jmp '
CALL = 'call '
PUSH = 'push '
POP = 'pop '
RET = 'ret '

#---------------- System calls

SYSCALL = 'int 0x80'

SYS_EXIT = 'mov eax, 1'
SYS_WRITE = 'mov eax, 4'

STDOUT = 'mov ebx, 1'



#-------
nl = '\n'

def recursive_gen(statement) -> str:

  if statement.type == 'declaration':
    return statement.name + ' db ' + str(statement.value) + '\n'

  elif statement.type == 'assignment':
    return MOV + '[' + statement.name + '], ' + str(statement.value) + '\n'



  #-------------------- functions

  elif statement.type == 'return':
    MAIN = ''
    MAIN += PUSH + 'eax' + nl
    MAIN += RET + '\n'
    return MAIN

  elif statement.type == 'function':
    MAIN = ''
    MAIN += statement.name + ':\n'

    for parameter in statement.parameters:
      pass
      #pop stack

    for part in statement.body:
      MAIN += recursive_gen(part) + '\n'
    return MAIN
      
  elif statement.type == 'call'
    
    if statement.callee == 'print':
      MAIN = ''
      message = str.join(statement.arguments)
      messageLen = len(message)
        
      MAIN += MOV + 'edx, ' + messageLen + '\n'
      MAIN += MOV + 'ecx, ' + message + '\n'
      MAIN += STDOUT + '\n'
      MAIN += SYS_WRITE + '\n'
      MAIN += SYSCALL + '\n'
      return MAIN

    
    else:
      MAIN = ''
      for arg in statement.arguments:

        MAIN += MOV + 'eax, ' + argument + nl
        MAIN += PUSH + 'eax' + nl
        
      
      MAIN += CALL + statement.callee + nl
      MAIN += POP + 'eax' + nl
      return MAIN
      
    
  #--------- END OF FILE

  elif statement == 'EOF':
    MAIN = ''
    MAIN += SYS_EXIT + '\n'
    MAIN += SYSCALL
    return MAIN

data_types = ['declaration']
bss_types = []
text_types = []
outer_types = ['function']
main_types = ['call', 'assignment']

def codegen(syntaxTree) -> Code:
  DATA = 'section .data\n'
  MAIN = '_start:\n'
  TEXT = 'section .text\nglobal _start'
  BSS = 'section .BSS\n'
  OUTER = ''

  for statement in syntaxTree.statements:

    if statement.type in data_types:
      DATA += recursive_gen(statement)
    elif statement.type in bss_types:
      BSS += recursive_gen(statement)
    elif statement.type in text_types:
      TEXT += recursive_gen(statement)
    elif statement.type in outer_types:
      OUTER ++ recursive_gen(statement)
    elif statement.type in main_types:
      MAIN += recursive_gen(statement)

  final_code = DATA + BSS + TEXT + OUTER + MAIN
      

  code = Code('x86 Assembly', final_code, '.asm')
  return code
