# > Estrutura de Listas

# Antes
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

# Com listas
notas = [7.9, 9.7, 8.2]


#Criando listas
lista = []
lista = list()
lista = [26, 'Andreson', 3.14159, False]
lista_de_listas = [10, [1, 2, 3]]


# Indexação
lista = [10, 'Andreson', 3.1415, True]

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])


# Slices (Fatiamento)
lista = [10, 50, 30, 40, 25, 60, 5]

print(lista[0:3])
print(lista[3:6])
print(lista[3:])
print(lista[2:6:2]) # Pula de 2 em 2


# Interações com FOR


# 1. Utilizando os próprios elementos da lista
for elemento in lista:
    print(elemento)

# 2. Utilizando os índices
print('Comprimento da lista:', len(lista))

for i in range(len(lista)):
    print(lista[i])


# > Métodos e Funções de Listas

lista = [1, 3, 12, 8, 2]

# append  - adicionar elementos no final da lista
print('Antes do append:', lista)

lista.append(3)

print('Depois do append:', lista)


# append  - escolelhe a posição do elementos e qual elemento vc quer adicionar

lista.insert(2, 10)

print('Depois do Insert:', lista)

# extend  - Juntar duas listas

lista2 = [1, 2, 3]

lista.extend(lista)
print('Depois do extend:', lista)

# pop  - remover o elemento especificado, caso não seja especificado elemento, ele removo o último elemento.

lista.pop()
print('Lista após o pop:', lista)

lista.pop(0)
print('Lista após o pop:', lista)

# remove  - diz qual valor quer remover
lista.remove(3)
print('Depois do remove:', lista)

# count - Conta a quantidade de vez de um elemento na lista
print('Depois do count:', lista.count(2))

# index - qual a posição do elemento
print('Depois do index:', lista.index(12))

# sort - ordenar a lista
lista.sort()
print('Lista após o sort:', lista)

lista.sort(reverse=True)
print('Lista após o sort2:', lista)

# FUNÇÕES PARA LISTAS

# len
print(len(lista))

# sum
print(sum(lista))

# max
print('Maior elemento da lista:', max(lista))

# min
print('Menor elemento da lista:', min(lista))



