# São imutaveis
t1 = (1,2,3,4,5,6,5,5,5,7,8)

print(t1.count(5)) #retorna quantas occorencias existe na lista
print(3 in t1)

# Todos os metodos que alteram listas não podem ser usados em tublas
# - sort(), append(), pop(), reverse()...
#Uma observação a ser feita no uso de uma tupla é que se ela tiver um único item, é necessário colocar uma vírgula depois dele, pois caso contrário, o objeto que vamos obter é uma string, porque o valor do item é do tipo string.

#é possivel criar lista apartir de tublas:
grupo17 = list(t1)