#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
#retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(ano):
    situacao = None
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        situacao = 'NEGADO'
    if (idade >= 16 and idade < 18) or idade >= 65:
        situacao = 'OPCIONAL'
    if idade >= 18 and idade < 65:
        situacao = 'OBRIGATÓRIO'
    
    return (situacao, idade)

print(voto(int(input('Ano de nascimento: '))))