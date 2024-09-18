# Crie um programa que receba um número inteiro e calcule o fatorial desse número usando uma estrutura de repetição.


numero = int(input("Digite o número: "))

resultado = 1

for n in range(1, numero +1):
    resultado = resultado * n

print('O resultado de {0}! é: {1}'.format(numero, resultado))


