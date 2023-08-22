v = []
i = 0
soma = 0

while (i<20):
    v.append(float(input('digite a nota: ')))
    i = i+1

i=0
print('notas>7.5:')
while(i<20):
    soma = soma + v
    media = soma / v
    print media
    if v[i]>7.5:
        print(v[i])
    i=i + 1