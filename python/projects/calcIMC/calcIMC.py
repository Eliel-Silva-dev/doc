print()
print('======== Calculadora de IMC ========')
print()

#Função que recebe 2 parametros, calcula o IMC e retorna o resultado
def CalcularIMC (altura, peso):

    #calculo do imc
    imc = peso / (altura ** 2)
    #retorna o imc calculado
    return imc

peso = float(input('Digite seu peso em quilogramas: '))
altura = float(input('Digite sua altura em metros (ex: 1.50): '))

calcIMC = CalcularIMC(altura,peso)

print('Seu IMC é de:  {:.2f}'.format(calcIMC))