# o mesmo professor do desafio anterior quer sortear a oderm de apresentação de trablahos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostr a ordem sorteada.
from random import  shuffle

a1 = input('Nome primeiro aluno: ')
a2 = input('Nome segundo aluno: ')
a3 = input('Nome terceiro aluno: ')
a4 = input('Nome quarto aluno: ')

lista = [a1, a2 , a3, a4]
shuffle(lista)

print('Os escolhidos foram ')
print(lista)
