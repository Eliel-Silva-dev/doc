import random

# valor = random.randint(1,20)

# print(valor)

#---------------------------------
# print('Rodar 5 vezes a função')

# for i in range(5):
#     n= random.randint(1,50)
#     print(f'Número gerado: {n}')

#---------------------------------

# valor = random.random() #gera numeros de ponto flutuante de 0,1

# print(f'Número gerado: {round(valor * 10, 2)}') # define casas decimais

#---------------------------------
# valor = random.uniform(1,100) #gera um numero de ponto flutuante mas é possivel especifiacar range
# print(f'número: {valor}')

#---------------------------------
L = [5,4,3,6,2,7,3,6,7,]

# n= random.choice(L) #extrai um valor aleatorio da lista

# print(f'Númeor escolhido: {n}')

# n2 = random.sample(L,3) #extrai 3 elementos da lista

# print(f'Numeros estraidos: {n2}')

#-------------------------------------
n3 = random.shuffle(L)
print(f'Lista embaralhada: {n3}')
