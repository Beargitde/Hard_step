import math
x = float(input('Введите значение x = '))
y = float(input('Введите значение y = '))
z = float(input('Введите значение z = '))
min = (x + y + z / 2) + 1
if (x * y * z) < min:
    min = x * y * z
print(min**2)


