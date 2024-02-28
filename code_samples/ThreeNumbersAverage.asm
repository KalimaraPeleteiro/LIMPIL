; -- Headers --
bits 64         ; Modo de 64 bits
default rel     ; Usando endereços relativos
                  
; -- Variáveis --
section .bss
                  
; -- Constantes --
section .data
                  
; -- Lógica --
section .text
global main
extern ExitProcess
extern printf
extern scanf
                  
main:
	; Criando espaço para variáveis locais.
	PUSH rbp
	MOV rbp, rsp
	SUB rsp, 32
                  
	PUSH 3
	;PRINT não implementado.
	;PRINT não implementado.
	;PRINT não implementado.
	;PRINT não implementado.
