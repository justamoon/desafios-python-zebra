#Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa 
#deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numero = int(input('Digite um número entre 0 e 20: '))

numeros_extenso = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze',
'quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

if numero <= 20 and numero >= 0:
    for i in numeros_extenso:
        if numero == numeros_extenso.index(i):
            print('O número digitado foi {}'.format(i))
            break

else:
    print('Número inválido!')
