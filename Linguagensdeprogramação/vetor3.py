venda = []
i = 0

while (i<20):
    venda.append(float(input('digite a quantidade de produtos vendidos: ')))
    i = i+1

i = 0
print("produtos que venderam mais de 100 unidades:")
while (i<20):
    if venda[i]>30:
        print(venda[i])
    i=i + 1    