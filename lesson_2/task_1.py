# урок 2 задание 1

l = [None, False, 1, 'два', 3.0, []]
l.append([4, "пять"])

for i in range(len(l)):
    print("Элемент списка {} с порядковым номером {} имеет тип {}".format(l[i], i + 1, type(l[i])))
