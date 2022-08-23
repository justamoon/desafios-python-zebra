#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python,
#só que fazendo a validação para aceitar apenas um valor numérico.

def leiaInt(nume):
    if nume is not int(nume):
        print('Digite um valor numérico que seja inteiro')
        return None
    else:
        return nume

leiaInt(input('Digite um número: '))

#TODO: não finalizado