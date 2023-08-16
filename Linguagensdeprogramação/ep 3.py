sabor = int(input('digite o sabor desejado, 1 para chocolate ou 2 para morango: '))
qtd = int(input('digite a quantidade de bolar desjada: '))

if(sabor == 2):
    print('sorvrte sem desconto')
else:
    if (qtd > 3):
        print('vc tem direito a um desconto de 10% ')
    else:
        print('vc tem direito a um desconto de 5%')


