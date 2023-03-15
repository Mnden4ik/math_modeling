s = 3 + 4 # Объект / Имя s ссылается на значение 3 + 4
memory_id = id(s)
print(s, memory_id)

s = 5 # новая ссылка
print(s, id(s))