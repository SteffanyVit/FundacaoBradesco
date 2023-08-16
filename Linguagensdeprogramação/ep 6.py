lavagem = int(input('digite 1 para lavagem simples ou 2 para lavagem completa: '))
pagamento = int(input('digite 1 para dinheiro ou 2 para cartão: '))

if( lavagem == 1):
    if( pagamento == 1):
        print(' lavagem simples pagamento em dinheiro, valor:R$ 30,00 reais')
    else:
        print('lavagem simples no cartão, valor: R$ 35,00 reais')
else:
    if (pagamento == 1):
        print(' lavagem completa pagamento em dinheiro, valor:R$ 50,00 reais')
    else:
        print('lavagem completa no cartão, valor: R$ 55,00 reais')
