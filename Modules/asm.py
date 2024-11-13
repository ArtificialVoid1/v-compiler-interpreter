from dataclasses import dataclass

# a class to hold the data for the code
@dataclass
class Code:
  language : str
  code : str
  ext : str

calls = {
  'syscall' : 'int 0x80',
  
  'sys_exit' : 'mov eax, 1',
  'sys_write' : 'mov eax, 4',
  

  'stdout' : 'mov ebx, 1'
}


def codegen(syntaxTree) -> Code:
  DATA = 'section .data\n'
  MAIN = '_start:\n'
  TEXT = 'section .text\n\tglobal _start'
  


  for statement in syntaxTree.statements:

    if statement.type == 'declaration':
      DATA += statement.name + ' db ' + str(statement.value) + '\n'

    elif statement.type == 'assignment':
      MAIN += 'mov [' + statement.name + '], ' + str(statement.value) + '\n'
      
    elif statement.type == 'call'

      if statement.callee == 'print':
        message = str.join(statement.arguments)
        messageLen = len(message)
        
        MAIN += 'mov edx, ' + messageLen + '\n'
        MAIN += 'mov ecx, ' + message + '\n'
        MAIN += calls.stdout + '\n'
        MAIN += calls.sys_write + '\n'
        MAIN += calls.syscall + '\n'

    elif statement == 'EOF':
      MAIN += calls.sys_exit + '\n'
      MAIN += calls.syscall


  code = Code('x86 Assembly', final_code, '.asm')
  return code
