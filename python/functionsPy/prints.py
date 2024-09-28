#sintaxe print()
#print(objeto, argumentos)

#nome = input('Digite seu nome: ')

#print('Ola ' + nome + ' seja bem vindo!')

print('Imprimi a mensagem e muda de linha')
print('Imprimi a mensagem e permanece na mesma linha ', end='')
print('Continuo na mesma linha')

nome = 'Maria'
idade = 30
msg_format = 'O nome dela é {0} e sua idade é {1} anos!'.format(nome, idade)

print(msg_format)
print(f'O nome dela é {nome} e sua idade é {idade} anos!')

valor = 125.579637
print(f'o valor da variavel é \'{valor:.2f}\'')

