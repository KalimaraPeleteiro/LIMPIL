import sys
from stack import Stack

# O arquivo a ser interpretado.
path = sys.argv[1]

if not path.endswith(".limpil"):
    print("Você não selecionou um arquivo .limpil.")
    sys.exit(0)

# Extraindo linhas.
lines = list()
with open(path, "r") as file:
    lines = [line.strip() for line in file.readlines()]

# Interpretando.
program = list()
token_counter = 0
label_tracker = {}

for line in lines:
    splitted_command = line.split(" ")
    opcode = splitted_command[0]

    if opcode == "":
        continue

    # Comentarios
    if opcode.startswith("--"):
        continue
    
    if opcode.endswith(":"):
        label_tracker[opcode[:-1]] = token_counter
        continue

    program.append(opcode)
    token_counter += 1

    if opcode == "ADICIONE":
        number = int(splitted_command[1])
        program.append(number)
        token_counter += 1
    elif opcode == "IMPRIMA":
        string = " ".join((splitted_command[1:]))[1:-1]
        program.append(string)
        token_counter += 1
    elif opcode == "PULE.SE.IGUAL.ZERO":
        label = splitted_command[1]
        program.append(label)
        token_counter += 1
    elif opcode == "PULE.SE.MAIORQUE.ZERO":
        label = splitted_command[1]
        program.append(label)
        token_counter += 1

stack = Stack(256)
pc = 0

while program[pc] != "PARE":
    opcode = program[pc]
    pc += 1

    if opcode == "ADICIONE":
        number = program[pc]
        pc += 1

        stack.push(number)
    elif opcode == "RETIRE":
        stack.pop()
    elif opcode == "SOMA":
        a = stack.pop()
        b = stack.pop()
        stack.push(a+b)
    elif opcode == "DIFERENCA":
        a = stack.pop()
        b = stack.pop()
        stack.push(b-a)
    elif opcode == "IMPRIMA":
        string_literal = program[pc]
        pc += 1
        print(string_literal)
    elif opcode == "LER":
        number = int(input())
        stack.push(number)
    elif opcode == "PULE.SE.IGUAL.ZERO":
        number = stack.top()
        if number == 0:
            pc = label_tracker[program[pc]]
        else:
            pc += 1
    elif opcode == "PULE.SE.MAIORQUE.ZERO":
        number = stack.top()
        if number > 0:
            pc = label_tracker[program[pc]]
        else:
            pc += 1