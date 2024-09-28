from math import sqrt

if __name__ == "__main__":
    try:
        num = int(input(f'Digite um valor positivo: '))
        if num < 0:
            raise ArithmeticError
    except ArithmeticError:
        print(f'Você informou um numero negativo')
    else:
        print(f'A raiz quadrada de {num} é {round(sqrt(num),2)}')
    finally:
        print('fim do calculo')

