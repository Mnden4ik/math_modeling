import numpy as np

a = [1, 2, 4]

b = np.array(a) #  Создание массива из списка

print(type(a))
print(type(b))

print(b * b)
print(b / b)
print(b - b)

print(b[-1]) # Вызов последнего эллемента массива