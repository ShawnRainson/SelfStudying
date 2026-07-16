def convert_currency(rubles, rate):
    res = rubles / rate
    return res

result = convert_currency(10000, 90)
print(f'Результат: {result}')