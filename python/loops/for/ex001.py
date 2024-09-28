# lista = [2,6,9,5,3,8,6]
# palavra = 'Boson'

# for letra in palavra:
#     print(letra)

# for numero in range(1,11):
#     print(numero)

# nome = input('Digite seu nome: ')

# for x in range(10):
#     print(f'{x+1} {nome}')

# range(Valor_inicial, valor_final, incremento)

# for x in range(20,2,-2):
#     print(x)

# for cont_ex in range(1,6):
#     print(f'\nRodada: {cont_ex}')
#     for cont_in in range(5,0,-1):
#         print(f'Valor: {cont_in}')

# print('fim dos laços')

# import random

# for A in range(1,6):
#     print(f'Conjunto {A}')
#     for B in range(5):
#         num = random.randint(1,100)
#         print(f'Valor: {num}')

#--------------------------------
pedras = ('rubi', 'esmetaldo', 'quartzo', 'diamante')

for pedra in pedras:
    if pedra == 'quartzo':
        continue
    print(pedra)