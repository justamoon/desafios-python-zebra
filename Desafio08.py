#Faça um programa que tenha uma função chamada maior(),que receba vários parâmetros com valores inteiros.
#Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(inteiros):
    maior = 0
    for numero in numeros:
        if numero > maior:
            maior = numero
        
    return maior

i = int(input('Quantos números inteiros? '))
numeros = [ int(input('Digite um número: ')) for j in range(i)]

print('O maior número dessa sequência é o', maior(numeros))