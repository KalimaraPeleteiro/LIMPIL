import sys
from stack import Stack

# ==== Acessando o arquivo e coletando o conteúdo. ====
path = sys.argv[1]

if not path.endswith(".limpil"):
    print("Você não selecionou um arquivo .limpil.")
    sys.exit(0)

lines = list()
with open(path, "r") as file:
    lines = [line.strip() for line in file.readlines()]


# ==== Separando os comandos para interpretação. ====
program = list()
token_counter = 0
label_tracker = {}

for line in lines:
    splitted_command = line.split(" ")
    opcode = splitted_command[0]

    if opcode == "":
        continue

    if opcode.startswith("--"): # Comentários
        continue
    
    if opcode.endswith(":"):
        label_tracker[opcode[:-1]] = token_counter
        continue

    program.append(opcode)
    token_counter += 1

    if opcode == "ADICIONE.INTEIRO":
        number = int(splitted_command[1])
        program.append(number)
        token_counter += 1
    elif opcode == "ADICIONE.DECIMAL":
        number = float(splitted_command[1])
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

# ==== Interpretando os comandos ====
stack = Stack(256)
pc = 0      # program_counter


while program[pc] != "PARE":
    opcode = program[pc]
    pc += 1

    if opcode == "ADICIONE.INTEIRO":
        number = program[pc]
        pc += 1
        stack.push(number)
    elif opcode == "ADICIONE.DECIMAL":
        number = program[pc]
        pc += 1
        stack.push(number)
    elif opcode == "RETIRE":
        stack.pop()
    elif opcode == "RETIRE.E.IMPRIMA":
        number = stack.pop()
        print(number)
    elif opcode == "SOMA":
        a = stack.pop()
        b = stack.pop()
        stack.push(a+b)
    elif opcode == "DIFERENCA":
        a = stack.pop()
        b = stack.pop()
        stack.push(b-a)
    elif opcode == "MUL":
        a = stack.pop()
        b = stack.pop()
        stack.push(a*b)
    elif opcode == "DIV":
        a = stack.pop()
        b = stack.pop()
        stack.push(a/b)
    elif opcode == "POTENCIA.QUADRADO":
        a = stack.pop()
        stack.push(a * a)
    elif opcode == "IMPRIMA":
        string_literal = program[pc]
        pc += 1
        print(string_literal)
    elif opcode == "TOPO":
        stack.top()
    elif opcode == "LER.STRING":
        string = str(input())
        stack.push(string)
    elif opcode == "LER.INTEIRO":
        number = int(input())
        stack.push(number)
    elif opcode == "LER.DECIMAL":
        number = float(input())
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
    elif opcode == "SE":
        if program[pc] == stack.top():
            pass # Fazer algo aq
        else:
            pc += 1 # Caso contrário, passar para o próximo estágio
