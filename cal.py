# Calculadora em Python usando funções
print('*********** CALCULADORA PYTHON **********')

# Declarando as funções
def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

# Bloco usuário
print('Selecione o número da operação desejada: ')
print('1 -> Soma')
print('2 -> Subtração')
print('3 -> Multiplicação')
print('4 -> Divisão')

# Entrada do usuário
escolha = input("Digite sua opção (1 - 2 - 3 - 4): ")
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Bloco Condicional
if escolha == '1':
    print('----****----')
    print(num1, '+', num2, '=', add(num1, num2))
    print('----****----')

elif escolha == '2':
    print('----****----')
    print(num1, "-", num2, "=", subtract(num1, num2))
    print('----****----')

elif escolha == '3':
    print('----****----')
    print(num1, "*", num2, "=", multiply(num1, num2))
    print('----****----')

elif escolha == '4':
    print('----****----')
    print(num1, "/", num2, "=", divide(num1, num2))
    print('----****----')

else:
    print('<<----------------------------***********------------------------>>')
    print('Operação inválida, por favor digite somente os números disponíveis.')
    print('<<----------------------------***********------------------------>>')