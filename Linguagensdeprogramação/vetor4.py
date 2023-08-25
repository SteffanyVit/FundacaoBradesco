altura = []
i = 0
soma = 0

while (i<3):
    altura.append(float(input('digite sua altura: ')))
    soma = soma + altura[i]
    i = i+1

media = soma / i

i = 0
print(f"alturas que exederam a média da turma:{media}")
while (i<3):
    if altura [i]>media:  
         print(altura[i])
    i=i + 1   