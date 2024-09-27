n1 = [1,2,3,5,6]
n2 = [7,8,9,10,11,12,13]
valores = n1 + n2

valores[0] = 14

print(valores[2:4]) #começando na segunda posição e trazendo 3 valores
print(valores[-2:]) #começando na posição -2 e trazendo os 2 ultimos valores

print(len(valores)) # retorna a quantidade de items da lista
print(sorted(valores)) # retorna a  mesma lista em forma ordenada
print(sorted(valores, reverse=True)) # retorna a  mesma lista em forma desordenada
print(sum(valores)) #retorna o valor acumulado da lista
print(min(valores)) #retorna o menor valor da lista
print(max(valores)) #retorna o maior valor da lista
print(17 in valores) # verifica se existe o valor 17 dentro da lista valores

valores.append(13) #acrescenta um valor na lista na ultima posição
valores.remove() # para a remoção pelo valor informado no parâmetro
valores.pop() #retira um valor da lista, se não for passado parametros retira sempre o ultimo elemento. ao passar o parametro ele retira o elemento na posoção declarada.
valores.insert(3,21) #insere um valor dentro da lista. primeiro_valor = posição inicial, segundo_valor = conteudo que será inserido na lista.

bebidas = []

for i in range(5):
    print('Digite uma bebida favorita: ')
    bebida = input()
    bebidas.append(bebida)

bebidas.sort()

print(f'Lista de bebidas favoritas: {bebidas}')
