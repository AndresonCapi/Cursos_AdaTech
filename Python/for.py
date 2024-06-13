# > Laços de Repetição (For)

# for variavel in range (5):
#     print(variavel)

# informa o valor iniciando pelo 1 até menor q 6.
# for variavel in range (1, 6):
#     print(variavel)

# informa o valor de início, valor de parada e qual é o passo
# for variavel in range (1, 12, 3):
#     print(variavel)


# nota1 = float(input('Informe sua nota 1:'))
# nota2 = float(input('Informe sua nota 1:'))
# nota3 = float(input('Informe sua nota 1:'))

soma = 0

for i in range(1, 4):
    nota = float(input(f'Informe sua nota {i}: '))

    soma = soma + nota

print(soma / 35)