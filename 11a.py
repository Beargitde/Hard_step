import math
x = input('Введите значение x = ')
y = input('Введите значение y =')
z = input('Введите значение z =')
x = float(x)
y = float(y)
z = float(z)
a = ((abs(x - 1))**1/2 - (abs(y))**1/3)/(1+(x**2/2)+(y**2/4))
print('a =',a)
z0 = math.radians(z)
z1  = math.atan(z0)
z = math.degrees(z1)
b = x * (z + math.e**-(x+3))
print('b =',b)




