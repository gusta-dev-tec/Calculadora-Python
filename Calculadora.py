# Função para somar
def somar(a, b):
    return a + b

# Função para subtrair
def subtrair(a, b):
    return a - b

# Função para multiplicar
def multiplicar(a, b):
    return a * b

# Função de divisão
def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return 'Erro divisão por zero!'

# Função de potenciação
def potenciacao(a, b):
    return a ** b

# Lista do histórico
historico = []

# Para pedir números
def pedir_numero():
    try:
        a = float(input('1 número: '))
        b = float(input('2 número: '))
        return a, b
    except:
        print('Erro, valor inválido!')
        return None, None

# Menu de opções
def menu():
    print('-----Calculadora-----')
    print('1 - Somar')
    print('2 - Subtrair')
    print('3 - Multiplicar')
    print('4 - Dividir')
    print('5 - Potenciação')
    print('6 - Histórico')
    print('7 - Sair')

while True:
    menu()
    e = input('Escolha uma opção: ')

    if e in ['1', '2', '3', '4', '5']:
        a, b = pedir_numero()

        if a is None:
            continue

        if e == '1':
            resultado = somar(a, b)
            print('Resultado:', resultado)
            historico.append(f'{a} + {b} = {resultado}')

        elif e == '2':
            resultado = subtrair(a, b)
            print('Resultado:', resultado)
            historico.append(f'{a} - {b} = {resultado}')

        elif e == '3':
            resultado = multiplicar(a, b)
            print('Resultado:', resultado)
            historico.append(f'{a} x {b} = {resultado}')

        elif e == '4':
            resultado = divisao(a, b)
            print('Resultado:', resultado)
            historico.append(f'{a} / {b} = {resultado}')

        elif e == '5':
            resultado = potenciacao(a, b)
            print('Resultado:', resultado)
            historico.append(f'{a} ** {b} = {resultado}')

    elif e == '6':
        print('----- HISTÓRICO -----')

        if len(historico) == 0:
            print('Nenhuma conta feita.')
        else:
            for item in historico:
                print(item)

    elif e == '7':
        print('Saindo...')
        break

    else:
        print('Erro, digite uma opção válida!')
