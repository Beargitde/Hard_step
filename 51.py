import math

a = float(input('Введите значение a = '))
b = float(input('Введите значение b = '))
c = float(input('Введите значение c = '))
if a == 0:
    print('Значение a должно быть больше нуля (а>0) ')
    exit(0)
D = b * b - 4 * a * c
if D > 0:
    t1 = (-b + D ** 1 / 2) / (2 * a)
    t2 = (-b - D ** 1 / 2) / (2 * a)
    x1 = math.sqrt(math.fabs(t1))
    x2 = math.sqrt(math.fabs(t2))
    print('x1 = ±', x1, 'x2 = ±', x2)
elif D == 0:
    t1 = -b / (2 * a)
    x1 = x2 = math.sqrt(t1)
    print('x1 = x2 = ±', x1)
elif D < 0:
    print('Корней нет.')
    


