# Funções
# Modularização, Reuso de codigo, legibilidade

#def <node_func> (args):
#   <instruções>

#-------------------
# def mensagem():
#     print('Teste de função')
#     print('finalizado')
# mensagem()

#-------------------
# def soma(a, b):
#     print(a + b)
# soma(2, 5)

#-------------------
# def mult(x, y):
#     return x * y
# c = mult(5, 3)

#-------------------
# def div(k, j):
#     if j != 0:
#         return k / j
#     else:
#         return 'Impossivel dividir por zero'

#----------------------------

def quadrado(val):
    quadrados = []
    for x in val:
        quadrados.append(x ** 2)
    return quadrados

if __name__ == '__main__':
    valores = [2,4,6,2,4,6]
    resultados = quadrado(valores)
    for g in resultados:
        print(g)
