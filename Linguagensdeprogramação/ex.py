contador = 0
soma = 0
print('sistema para média de alturas [5 pessoas]')

while contador < 5:
    altura = float(input('digite o valor da altura: '))
    soma = soma + altura
    contador = contador +1
media = soma / contador
print('a média das alturas é de: ', media)