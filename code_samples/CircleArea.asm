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
                  
	;PRINT não implementado.
	;LEITURA não implementado.
	PUSH 3.14
	;PRINT não implementado.
	JMP exit_label
exit_label:
	xor rax, rax       ; Zerando RAX
	CALL ExitProcess
