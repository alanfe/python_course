seconds = int(input("введите время в секундах"))

timeH = seconds // 3600
timeM = (seconds - timeH * 3600) // 60
timeS = seconds - (timeH * 3600 + timeM * 60)

print("Точное время " + f"{timeH:02d}" + ":" + f"{timeM:02d}" + ":" + f"{timeS:02d}")
