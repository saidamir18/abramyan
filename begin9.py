import math
a=int(input('Введите число: '))
if a<=0:
    print('Отрицательное число')

b=int(input('Введите число: '))
if b<=0:
    print('Отрицательное число')
c = math.sqrt(a*b)
print('Результат ' + str(c))