a = int(input("Результаты пробежки в первый день?"))
b = int(input("Желаемый результат?"))
days = 1
result = a
while result < b:
        a = 1.1 * a
        days += 1
        result = result + a
print(f"Спортсмен достигнет требуемых результатов на %.d день" % days)
