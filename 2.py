from math import log10


N=int(input('Введите N: '))

for i in range(1, N+1):
    if i == i**2 % 10**(int(log10(i))+1):
        print(i)