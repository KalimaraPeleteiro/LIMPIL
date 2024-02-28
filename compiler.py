import sys
import os

path = sys.argv[1]

if not path.endswith(".limpil"):
    print("Você não selecionou um arquivo .limpil!")
    sys.exit(0)

file_lines = list()
with open(path, "r") as file:
    file_lines = [line.strip() for line in file.readlines()]


# ===== PARSING =====
print("[CMD] Transformando o código...")

program = list()
for line in file_lines:
    splitted_command = line.split(" ")
    opcode = splitted_command[0]

    if opcode == "":                # Linha em branco
        continue
    if opcode.startswith("--"):     # Comentário
        continue

    program.append(opcode)

    # Comandos
    if opcode == "ADICIONE.INTEIRO":
        number = int(splitted_command[1])
        program.append(number)
    if opcode == "ADICIONE.DECIMAL":
        number = float(splitted_command[1])
        program.append(number)
    if opcode == "IMPRIMA":
        string = " ".join((splitted_command[1:]))[1:-1]
        program.append(string)
    

# ===== COMPILING =====
print("[CMD] Transformando em Assembly...")

# Removendo os 07 últimos caracteres (.limpil)
assembly_path = path[:-7] + ".asm"
asm_program = open(assembly_path, "w")

asm_program.write("""; -- Headers --
bits 64         ; Modo de 64 bits
default rel     ; Usando endereços relativos
                  
""")

asm_program.write("""; -- Variáveis --
section .bss
                  
""")

asm_program.write("""; -- Constantes --
section .data
                  
""")

asm_program.write("""; -- Lógica --
section .text
global main
extern ExitProcess
extern printf
extern scanf
                  
main:
\t; Criando espaço para variáveis locais.
\tPUSH rbp
\tMOV rbp, rsp
\tSUB rsp, 32
                  
""")

pointer = 0
while pointer < len(program):
    opcode = program[pointer]
    pointer += 1

    if opcode == "ADICIONE.INTEIRO":
        number = int(program[pointer])
        pointer += 1
        asm_program.write(f"\tPUSH {number}\n")
    if opcode == "ADICIONE.DECIMAL":
        number = float(program[pointer])
        pointer += 1
        asm_program.write(f"\tPUSH {number}\n")
    if opcode == "IMPRIMA":
        string_index = program[pointer]
        pointer += 1
        asm_program.write("\t;PRINT não implementado.\n")
    if opcode == "LER.DECIMAL":
        string_index = program[pointer]
        pointer += 1 
        asm_program.write("\t;LEITURA não implementado.\n")
    if opcode == "PARE":
        asm_program.write("\tJMP exit_label\n")

asm_program.write("exit_label:\n")
asm_program.write("\txor rax, rax       ; Zerando RAX\n")
asm_program.write("\tCALL ExitProcess\n")

asm_program.close()


# ===== ASSEMBLING =====
print("[CMD] Compilando Assembly...")
os.system(f"nasm -f elf64 {assembly_path}")