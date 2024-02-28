import sys
from stack import Stack
from if_statement import IfBlock

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
if_blocks = list()
if_block_open = None
line_counter = 0

for line in lines:
    line_counter += 1
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

    elif opcode == "SE":
        if if_block_open is not None:
            raise SyntaxError("Erro de sintaxe. Bloco SE iniciado, mas não fechado com SE.FIM")
        if splitted_command[1][-1] != ":":
            raise SyntaxError("Comando SE com a sintaxe incorreta. Se esqueceu do ':'?")
        
        dataCheck = splitted_command[1][:-1]
        if dataCheck[0] == '"':
            block = IfBlock(value = dataCheck[1:-1], startLine=line_counter)
        elif dataCheck.__contains__("."):
            block = IfBlock(value = float(dataCheck), startLine=line_counter)
        else:
            block = IfBlock(value = int(dataCheck), startLine=line_counter)
        
        if_block_open = block
    
    elif opcode == "SE.FIM":
        if if_block_open is None:
            raise SyntaxError("Erro, bloco SE não foi inicializado!")
        
        if_block_open.endLine = line_counter
        if_blocks.append(if_block_open)

        if_block_open = None

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
if_counter = 0
if_content_skip = False

while program[pc] != "PARE":
    opcode = program[pc]
    pc += 1

    if opcode == "SE.FIM":
        if_content_skip = False

    if if_content_skip is True:
        continue

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
        stack.push(b/a)
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
        if if_counter > len(if_blocks):
            raise SystemError("if_counter maior que if_blocks. Erro do programa.")
        
        block = if_blocks[if_counter]
        if block.value == stack.top(): # Se a condição for correta, continue
            if_counter += 1
        else: # Caso contrário, pule para o fim do bloco.
            if_counter += 1
            if_content_skip = True