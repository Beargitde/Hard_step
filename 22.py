import math

a = input('Введение значение наибольшего основания а = ')
b = input('Введите значение меньшего основания b = ')
c = input('Введите значение угла а при наибольшем основании  ')
a = float(a)
b = float(b)
c = float(c)
c0 = math.radians(c)
corner = math.tan(c0)
c = math.degrees(corner)
S = (a**2 - b**2)/4 * corner
print('Площадь равнобочной трапеции S =',S)
