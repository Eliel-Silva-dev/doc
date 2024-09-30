print() #pular uma linha
print('======== Calculadora de IMC ========')
print() #pular uma linha

#Função que recebe 2 parâmetros, calcula o IMC e retorna o resultado
def CalcularIMC (altura, peso):

    #calculo do imc
    imc = peso / (altura ** 2)
    #retorna o imc calculado
    return imc

#Solicitação do peso
peso = float(input('Digite seu peso em quilogramas: '))
#Solicitação da altura
altura = float(input('Digite sua altura em metros (ex: 1.50): '))

#calculo de imc
calcIMC = CalcularIMC(altura,peso)

#Classificação do imc
classificacao = ''
#Observação segundo o valor do imc
observação = ''

print() #pular uma linha
#Mostrando o valor do imc na tela
print('Seu IMC é de:  {:.2f}'.format(calcIMC))

print() #pular uma linha

if calcIMC > 0: # Verifica se o imc é maior que zero
    if calcIMC < 18.5: # Verificação da faixa de imc
        classificacao = 'Abaixo do peso'
        observação = 'Magreza'
    elif 18.5 <= calcIMC < 24.9:
        classificacao = 'Peso normal'
        observação = 'Saudável'
    elif 25 <= calcIMC < 29.9:
        classificacao = 'Sobrepeso'
        observação = 'Excesso de peso'
    elif 30 <= calcIMC < 34.9:
        classificacao = 'Obesidade grau 1'
        observação = 'Obesidade'
    elif 35 <= calcIMC < 39.9:
        classificacao = 'Obesidade grau 2'
        observação = 'Obesidade severa'
    else:
        classificacao = 'Obesidade grau 3'
        observação = 'Obesidade mórbida, procure acompanhamento médico'
else:
    #Mensagem de erro em caso de imc zero
    print('Valores inválidos não foi possível calcular seu IMC')

print(f'Classificação: {classificacao}')
print() #pular uma linha

print(f'Observação: {observação}')
print() #pular uma linha
