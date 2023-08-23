notas = []
i = 0
while (i<20):
    notas.append(float(input('digite a nota: ')))
    i = i+1

i=0
print("notas>7.5:")
while(i<20):
    if notas[i]>7.5:
        print(V[i])
    i=i + 1