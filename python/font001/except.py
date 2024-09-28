#Exceção é um objeto que erpresenta um erro que ocorreu ao execultar o programa
#Blocos try ... except

def div(x, y):
    return round(x / y, 2)

if __name__ == '__main__':
    while True:
        try:
            n1 = int(input('Digite um dividendo: '))
            n2 = int(input('Digite um divisor: '))
            break
        except ValueError:
            print(f'Não foi possivel ler o valor digitado, tente novamente!!')

    try:
        r = round(n1 / n2, 2)
    except ZeroDivisionError:
        print(f'Não é possivel dividir por zero, tente novamente')
    except:
        print(f'Ocorreu um erro desconhecido')
    else:
        print(f'O valor da divisão de {n1} por {n2} é {r}')
    finally:
        print(f'\nFim do calculo!!')