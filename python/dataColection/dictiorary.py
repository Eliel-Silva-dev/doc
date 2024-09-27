#Dicionarios

elemento = {
    'Z': 3,
    'nome': 'litio',
    'grupo': 'Metais alcalinos',
    'densidade': 0.534
}

print(f'Elemento: {elemento['nome']}')
print(f'Densidade: {elemento['densidade']}')
print(f'O dicionario possui {len(elemento)} elementos')

elemento['grupo'] = 'Metais'

#adicionar entradas
# se a propriedade existir ela será alterada, se não existir ela será criada.
elemento['periodo'] = 1
print(elemento['periodo'])

# #remover item da lista
# del elemento['periodo']
# print(elemento)

# #Limpar a lista
# elemento.clear()
# print(elemento)

# #deletar a lista
# del elemento
# print(elemento)

#itera cada item da lista execultando uma função
for i in elemento.items:
    print(i)

#itera cada chave da lista execultando uma função
for  i in elemento.keys:
    print(i)