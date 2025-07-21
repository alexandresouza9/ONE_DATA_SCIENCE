"""# Manipulando dados

Vamos aprender sobre as variáveis no python, como elas são declaradas e utilizadas além de conhecer outros comandos dentro do Python. :D

## Variáveis

Em Data Science nós trabalhamos com vários dados e informações, então é essencial saber trabalhar com variáveis.

Criamos uma variável no python através da atribuição de um valor a ela.

Para fazer isso, colocamos o nome da variável um sinal de igual (`=`) e o valor que queremos atribuir
"""
idade = 5

print(idade)

idade = 10
print(idade)

idade = 15
idade

nome = 'Arthur'
nome

"""Nomes que **não** podemos definir para variáveis:
- **Nomes que começam com números**
  - Exemplos: `10_notas`, `2_nomes_casa`, etc.
- **Palavras separada por espaço**
  - Exemplos: `Nome escola`, `notas estudantes`, etc.
- **Nomes de funções do Python**
  - Exemplos: `print`, `type`, etc.

> Letras maiúsculas e minúsculas vão gerar diferentes variáveis. A varíavel `idade` é diferente de `Idade` que por sua vez também é diferente de `IDADE`:
``` Python
idade = 1
Idade = 2
IDADE = 3
_idade = 4
_idade_ = 5
print(idade, Idade, IDADE, _idade, _idade_)
1 2 3 4 5
"""