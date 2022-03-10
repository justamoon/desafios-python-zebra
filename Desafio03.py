#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nota_1 = float(input('Insira a primeira nota do aluno: '))
nota_2 = float(input('Iasira a segunda nota do aluno: '))

media = (nota_1 + nota_2) / 2
print('A nota final do aluno é {:.2f}'.format(media))