section .data
  lookUpDig: db "0123456789"

section .text
  global printf
  type printf,@function

IntToStrLoop:
  mov ebx, rdx
  div ebx, 10
  mov ebp, [lookUpDig + edx]
  

printf:
  pop rdx ; get argument
  pop rdi ; get arg length

  

  mov edx, rdi
  mov ecx, rdx
  mov eax, 4
  mov ebx, 1
  int 0x80
  ret
