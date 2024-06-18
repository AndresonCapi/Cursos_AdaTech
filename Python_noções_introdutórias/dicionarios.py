#> DICIONÁRIOS

# Criando dicionários

dicionario = {}  # dicionários vazio
dicionario = dict()  # dicionários vazio

dicionario = {'nome': 'Andreson', 'idade': 48, 'altura': 1.80}



# Adicionando elementos em um dicionário
dicionario['programador'] = True

print(dicionario)

# Iterando sobre um dicionário - percorrendo por todo o dicionário

for chave in dicionario:
    print(chave, dicionario[chave])


# Testando a existência de uma chave

print('peso' in dicionario)
print('altura' in dicionario)






