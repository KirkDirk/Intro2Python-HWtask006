# Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

numfloat = str(input('Введите вещественное число: '))
sumdigit = 0
for i in range(len(numfloat)):
    if numfloat[i] != '.' and numfloat[i] != ',':
        sumdigit += int(numfloat[i])
print(sumdigit)
