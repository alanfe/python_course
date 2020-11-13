number = int(input("введите число"))

M = number % 10

while number > 0:
    number = number // 10
    if number % 10 > M:
        M = number % 10

print("Максимальное цифра в этом числе: " + str(M))
