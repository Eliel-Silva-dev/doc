# Recursividade

# Formula geral para o fatorial
# fatorial(num) = 1, se num = 0 ou se num = 1 'caso-base'
# fatorial(num) = num * fatorial(num -1), para num > 1 'caso recursivo'
# 4! = 4 * fatorial(3) = 4 * 3 * fatorial(2) = 4 * 3 * 2 * fatorial(1)
# 4! = 4 * 3 * 2 * 1 = 24

def fatorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * fatorial(num -1)

if __name__ == '__main__':
    numero = int(input('Digite um numero inteiro positivo: '))

    try:
        res = fatorial(numero)
    except RecursionError:
        print('O numero informado é muito grande ou negativo')
    else:
        print(f'O fatorial de {numero} é {res}')
    finally:
        print('\nFim do calculo')