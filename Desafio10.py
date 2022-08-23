#Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show,
#que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(n, show):
    try:
        show = bool(int(show))
    except:
        show == False #aqui, considerei que ausência de resposta ou inputs inválidos serão lidos como falso, p garantir opção
    fat = 1
    for f in range(n, 0, -1):
        if show == True:
            print(f, end = '')
            if n > 1:
                print(' * ', end='')
            else:
                print(' = ', end = '')
        fat *= f
    return n, fat

f = fatorial(int(input('Digite um valor: ')), input('Deseja visualizar o processo? \n 0 - não \n 1 - sim \n'))
print('O fatorial de {} é {}'.format(f[0], f[1]))