#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da 
#estrutura na tela.

nome = input('Nome do aluno:')
media = float(input('Média do aluno:'))
if media >= 5 and media <= 10:
    situacao = 'Aprovado'
if media <5:
    situacao = 'Reprovado'
resultados_sala = {'Nome': nome.capitalize(), 'Média': media, 'Situação': situacao}  

print(resultados_sala)
