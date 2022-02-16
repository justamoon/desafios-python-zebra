# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais 
# ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

Kms_carro = float(input("Informe a quantidade de Km percorridos pelo carro: "))
Dias_carro = int(input("Informe a quantidade de dias pelos quais o carro foi alugado: "))

Preço = 60*Dias_carro + 0.15*Kms_carro

print('O valor a pagar é de R$ {:.2f}'.format(Preço))