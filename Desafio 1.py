## Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira

## Ex: Digite um número: 6.127
## O Número 6.127 tem a parte inteira 6

import math

n = float(input('Digite um número Real(Ex: 2.57): '))
a = math.trunc(n)
print('O número {} tem a parte inteira de {}'.format(n, a))

# ====================================================================

# =================  forma sem utilizar uma segunda variável ==========================

# n = float(input('Digite um número Real(Ex: 2.57): '))
# print('O número {} tem a parte inteira de {}'.format(n, math.trunc(n)))