proceeds = float(input("Выручка фирмы? "))
costs = float(input("Издержки фирмы? "))

if proceeds > costs:
    print("Фирма работает с прибылью. Рентабельность выручки " + f"{proceeds / costs:.2f}")
    employees = int(input("Сколько сотрудников работает в фирме? "))
    print("Прибыль в расчете на одного сотрудника: " + f"{(proceeds - costs) / employees:.2f}")

elif proceeds == costs:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")
