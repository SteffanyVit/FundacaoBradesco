venda = []
i = 0

while (i<30):
    venda.append=(Strings(input('digite o produto vendido: ')))
    qtd_v = int(input('digite a quantidade de produtos vendidos: '))
    i = i+1

i = 0
while (i<30):

    if venda[i]>30:
        print("produtos que venderam mais de 100 unidades:")
        print(venda[i])
    i = i+1   