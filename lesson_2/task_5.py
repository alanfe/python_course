# урок 2 задание 5

l = [7, 5, 3, 3, 2]
print ('начальный рейтинг', l)
n = int(input('введите натуральное число (для выхода введите 0)'))

while n != 0:
    for i in range(len(l)):
        if l[i] == n:
            l.insert(i + 1, n)
            break
        elif l[0] < n:
            l.insert(0, n)
        elif l[-1] > n:
            l.append(n)
        elif l[i] > n and l[i + 1] < n:
            l.insert(i + 1, n)
    print(f"текущий список - {l}")
    n = int(input('введите натуральное число (для выхода введите 0)'))
    