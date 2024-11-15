section .data

section .BSS
  v: resb 8

section .text
  global _start
  
_add:
  pop rsi
  pop rdi
  add rsi, rdi
  push rsi
  ret

_start:
  mov rdx, 1
  push rdx
  mov rdx, 2
  push rdx
  call _add
  pop rdx
  mov [v], rdx

  mov rdx, [v]
  push rdx
  call _printf

  
  mov rdx, 4
  push rdx
  mov rdx, 5
  push rdx
  call _add
  pop rdx

  push rdx
  call _printf

  

  
  mov eax, 1
  push eax
  mov eax, 2
  push eax
  call _add
  pop rdx
