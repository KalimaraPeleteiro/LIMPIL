<h2>LIMPIL</h2>

LIMPIL, ou *Linguagem Interpretada de Manipulação de Pilhas* é uma linguagem que fornece ao usuário uma interface para a interação com uma estrutura de pilha. 
A sintaxe e o interpretador são baseados em um [projeto similar](https://github.com/basvdl97/OLL-Interpreter) de [basvdl97](https://github.com/basvdl97). Eu
expandi a sua ideia original para abrangir novas operações e *features*, como o uso de comentários e outros tipos de dados.

A linguagem ainda está em desenvolvimento, mas já é possível fazer uso das novas *features*, como a leitura
de outros tipo de valores, uso de comentários e outras operações matemáticas nativas...
```
-- Calculando Área de um Círculo
IMPRIMA "Insira o raio do círculo"
LER.DECIMAL
POTENCIA.QUADRADO
ADICIONE.DECIMAL 3.14
MUL
IMPRIMA "A área do círculo é"
RETIRE.E.IMPRIMA
PARE
```

... e até mesmo blocos condicionais com `SE` e `SE.FIM`
```
--- Calculadora
IMPRIMA "================================"
IMPRIMA "Programa de Calculadora"
IMPRIMA "================================"

IMPRIMA "Escolha sua opção!"
IMPRIMA ""
IMPRIMA "A - ADIÇÃO"
IMPRIMA "B - SUBTRAÇÃO"
IMPRIMA "C - MULTIPLICAÇÃO"
IMPRIMA "D - DIVISÃO"
IMPRIMA ""
LER.STRING
IMPRIMA ""

SE "a":
IMPRIMA "Qual o primeiro número?"
LER.INTEIRO
IMPRIMA "Qual o segundo número?"
LER.INTEIRO
SOMA
IMPRIMA "A resposta da soma é:"
RETIRE.E.IMPRIMA
SE.FIM

SE "b":
IMPRIMA "Qual o primeiro número?"
LER.INTEIRO
IMPRIMA "Qual o segundo número?"
LER.INTEIRO
DIFERENCA
IMPRIMA "A resposta da subtração é:"
RETIRE.E.IMPRIMA
SE.FIM

SE "c":
IMPRIMA "Qual o primeiro número?"
LER.INTEIRO
IMPRIMA "Qual o segundo número?"
LER.INTEIRO
MUL
IMPRIMA "A resposta da multiplicação é:"
RETIRE.E.IMPRIMA
SE.FIM

SE "d":
IMPRIMA "Qual o primeiro número?"
LER.INTEIRO
IMPRIMA "Qual o segundo número?"
LER.INTEIRO
DIV
IMPRIMA "A resposta da divisão é:"
RETIRE.E.IMPRIMA
SE.FIM

PARE
```

Como já mencionado, todo código é apenas uma abstração de uma interação com uma grande estrutura de pilha, então estou trabalhando dentro destas limitações para trazer outros elementos.