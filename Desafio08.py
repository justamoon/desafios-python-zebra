#Faça um programa que tenha uma função chamada maior(),que receba vários parâmetros com valores inteiros.
#Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(inteiros):
    maior = 0
    for numero in numeros:
        if numero > maior:
            maior = numero
        
    return maior


i = int(input('Quantos números inteiros? '))
numeros = []
for i in range(i):
    numeros.append(int(input('Digite um número: ')))

#Uma comprehensive list??

print('O maior maior número dessa sequência é o', maior(numeros))