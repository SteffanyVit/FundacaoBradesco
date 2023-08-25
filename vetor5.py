idade = []
i = 0

while (i<5):
    idade.append(float(input('digite sua idade: ')))
    i = i+1

i = 0
while (i<5):
    if idade[i]<30:
        print('idades menores que 30:')
        print(idade[i])
    i=i + 1    