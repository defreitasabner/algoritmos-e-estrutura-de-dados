global _start

section .data
    msg db "Hello World!", 0x0a
    len equ $ - msg

section .text
_start:
    mov eax, 4      ; código para chamada do sistema (sys_write)
    mov ebx, 1      ; stdout file descriptor
    mov ecx, msg    ; bytes que serão escritos
    mov edx, len    ; quantidade de bytes que serão escritos
    int 0x80        ; chamada de sistema do tipo interrupção (interrupt)