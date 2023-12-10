height = float(input("Введите свой рост в сантиметрах: "))
weight = float(input("Введите свой вес в кг: "))
height = height / 100
BMI = weight / (height * height)
print("Ваш индекс массы тела равен: ", BMI)
scale = "18.5" + "=" * int(BMI - 18.5) + "|" + "=" * int(24.9 - BMI) + "24.9"
print(scale)

weight = 80.4
height = 181

BMI 