numeros = [1,4,7,9,12,21]

# quadrados = list(map(lambda num: num**2, numeros))
# quadrados = [num ** 2 for num in numeros]
# print(quadrados)

# pares = [num for num in range(11) if num % 2 == 0]
# print(pares)

frase = 'A lógica é apenas o principio da sabedoria e não o seu fim'
vogais = ['a','A','e','i','o','u','á','é','í','ó','ú']

lista_vogais = [v for v in frase if v in vogais]

print(f'A frase possui {len(lista_vogais)} vogais: ')
print(lista_vogais)