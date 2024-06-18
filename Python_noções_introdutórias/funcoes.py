# > FUNÇÕES

# 1. O que é funções e por que utilizalas?
'''

'''

# Funções que ja utilizamos anteriormente...
'''
print() # - Imprimir uma mensagem (int, float, str) no console (terminal, cmd)
input() # - Retorna um dado informado pelo usuário (entrada padrão) e pode receber uma string
len()   # - Recebe uma lista e retorna o tamanho dessa lista
max()   # - Retorna o maior valor de uma lista
'''

# 2. Criação de funções

# Função inicial
def saudacao():
    print('Seja bem-vindo(a)!')
    print('Olá, é um prazer ter você fazendo parte desse curso!')

saudacao()

# Função com parâmetro
def saudacao(nome, curso):
    print(f'Seja bem-vindo(a), {nome}!')
    print(f'Olá, é um prazer ter você fazendo parte desse curso de {curso}!')

saudacao('Andreson', 'Pyhton')


# Função com parâmetros default
def saudacao(nome, curso= 'python'):
    print(f'Seja bem-vindo(a), {nome}!')
    print(f'Olá, é um prazer ter você fazendo parte desse curso de {curso}!')

saudacao('Andreson')


# Função com retorno
def soma(num1, num2):
    return num1 + num2

resultado = soma(5, 7)

print('O resultado da soma é', resultado)

def calculadora(num1, num2, operacao= '+'):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        return num1 / num2

resultado1 = calculadora(10, 20)
print('Seu resultado é:', resultado)

resultado2 = calculadora(10, 20, '-')
print('Seu resultado é:', resultado2)