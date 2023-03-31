n = int(input('Введите количество членов: '))
a_first = int(input('Введите первый член прогрессии: '))
q = int(input('Введите знаменатель прогрессии: '))

print(a_first)

a_prev = a_first

for i in range(1,n):
    a_cur = a_prev*q
    print(a_cur)
    a_prev = a_cur