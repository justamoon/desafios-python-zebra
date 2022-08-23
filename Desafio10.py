#Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show,
#que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(n, show):
    try:
        show = bool(int(show))
    except:
        show == False #aqui, considerei que ausência de resposta ou inputs inválidos serão lidos como falso, p garantir opção
    calc = int(n)
    fat = 1
    while calc > 0:
        fat = fat*calc
        if show == True:
            print('{} * {}'.format(fat,calc))
        calc -= 1
    return n, fat

f = fatorial(input('Digite um valor: '), input('Deseja visualizar o processo? \n 0 - não \n 1 - sim \n'))
print('O fatorial de {} é {}'.format(f[0], f[1]))