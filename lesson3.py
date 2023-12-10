height = float(input("Введите свой рост в сантиметрах: "))
weight = float(input("Введите свой вес в кг: "))
height = height / 100
BMI = weight / (height * height)
print("Ваш индекс массы тела равен: ", BMI)
scale = "20" + "=" * int(BMI - 20) + "|" + "=" * int(50 - BMI) + "50"
print(scale)