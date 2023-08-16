opção = int (input('Digite a opção de ingresso desejado. 1 para vip ou 2 para standart : \n'))

pipoca = int (input( 'digite a opção de pipoca. 1 para sim e 2 para não: '))

if (opção == 1):
 #   print('ingresso vip sem pipoca valor: 80 reais' )

    if(  pipoca == 1):
        print('ingresso vip com pipoca valor: 110 reais')

    else:
        print('ingesso vip sem pipoca valor: 80 reais')


    if (pipoca == 1):
        print('ingresso stndart com pipoca valor: 70 reais')

else:
        print('ingesso standart sem pipoca valor: 40 reais')