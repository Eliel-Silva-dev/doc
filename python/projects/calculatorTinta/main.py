from calculadora_mod import Calculadora
calc = Calculadora()

from comodo import Comodo
comodo = Comodo(input('Qual a largura do comodo? '), input('Qual a profundidade do comodo? '))

#calc.area_parede = 2 * (largura + profundidade) * altura

print('A area das paredes é: ',
      calc.calcular_area_paredes(comodo), 'M²')

#calc.area_teto = largura * altura

print('A area do teto é: ',
      calc.calcular_area_teto(comodo), 'M²')

print('A litragem de tint necessaria é: ',
      calc.calcular_litragem_necessaria(), 'M²'
      )

# aula 7