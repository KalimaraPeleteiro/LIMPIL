<h2>LIMPIL</h2>

LIMPIL, ou *Linguagem Interpretada de Manipulação de Pilhas* é uma linguagem que fornece ao usuário uma interface para a interação com uma estrutura de pilha. 
A sintaxe e o interpretador são baseados em um [projeto similar](https://github.com/basvdl97/OLL-Interpreter) de [basvdl97](https://github.com/basvdl97). Eu
expandi a sua ideia original para abrangir novas operações e *features*, como o uso de comentários e outros tipos de dados.

A linguagem ainda está em desenvolvimento, mas já é possível construir alguns algoritmos básicos, como verificando se um número é par ou ímpar:
```
-- Verificando se um número é par ou ímpar
IMPRIMA "Insira o número"
LER.INTEIRO
PULE.SE.IGUAL.ZERO L1

LOOP:
ADICIONE.INTEIRO 2
DIFERENCA
PULE.SE.IGUAL.ZERO L1
PULE.SE.MAIORQUE.ZERO LOOP
IMPRIMA "É impar."
PARE

L1:
IMPRIMA "É par."
PARE
```

... ou calculando a área de um círculo.
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

Como já mencionado, todo código é apenas uma abstração de uma interação com uma grande estrutura de pilha, então estou trabalhando dentro destas limitações para trazer
outros elementos, como condicionais e outras operações.
