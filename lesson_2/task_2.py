# урок 2 задание 2

l = input('введите элементы списка через пробел')
l = l.split()
i = 0

if len(l) != 0:
    while i < len(l) - 1:
        l[i], l[i + 1] = l[i + 1], l[i]
        i += 2

#смотрим полученный список
print('преобразованный список ', l)
