pont = []
i = 0

while (pont<=15):
    pont.append(float(input('digite a pontuação: ')))
    i = i+1

i = 0
print("pontuações que excederam 20 pontos:")
while (pont<=15):
    if pont[i]>20:
        print(pont[i])
    i=i + 1    