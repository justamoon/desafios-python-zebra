#Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados
#e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

import random

num_jogos = int(input('Informe o número de jogos que deseja: '))
i = 0
jogos = []
#jogo = []

while i < num_jogos:
    num = list(random.randint(1,60) for n in range(0,6))
    jogos.append(num)
    i += 1
    num = []

print(jogos)