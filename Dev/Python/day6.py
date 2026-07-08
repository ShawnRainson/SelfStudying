try:
    val = float(input("Введите сумму:"))
    print('Результат: ', val / 90)
except ValueError:
    print('Вы ввели не число с плавающей точкой!')