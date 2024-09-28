nome = None

while True:
    print('Digite seu nome, ou x para terminar:')
    nome = input()
    if nome == 'x' or nome == 'X':
        break
    print(f'Bem vindo, {nome}')
print('Ate a proxima')