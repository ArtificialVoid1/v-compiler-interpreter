section .text
  global printf
  type printf,@function

printf:
  pop rdx ; get argument
  pop rdi ; get arg length

  mov edx, rdi
  mov ecx, rdx
  mov eax, 4
  mov edi
