# Задача 10
import random

n = int(input('Введите количество монет: '))

i = 0 # Счетчик переворотов монеток

list_coins = [] # Массив с монетками

# Заполняем массив элементами от 0 до 1, где 0 - орел, 1 - решка
for _ in range(n):
    coin = random.randint(0, 1)
    list_coins.append(coin)
print(list_coins)

 #Перебор массива с монетками
for coin in list_coins:
    if coin == 0:
        i += 1
print("Колличество монеток, котторые необходимо перевернуть =", i)

# Задача 12
def find_numbers(S, P):
    for x in range(1, 1001): # перебираем значения от 1 до 1000 для числа X
        if P % x == 0: # проверяем, что x является делителем P
            y = P // x # вычисляем значение числа Y
            if x + y == S: # проверяем, что сумма x и y равна S
                return (x, y) # возвращаем найденную пару чисел
    return None # в случае, если подходящая пара чисел не найдена

# Пример
print("Загадайте два числа")
S = int(input('Введите сумму этих чисел: '))
P = int(input('Введите произведение этих чисел: '))
result = find_numbers(S, P)
if result:
    x, y = result
    print(f"Числа: {x}, {y}")
else:
    print("Пара чисел не найдена")

# Задача 14

n = int(input("Введите число N: "))
print("Целые степени двойки, не превосходящие число N:")
power = 0
result = 1
while result <= n:
    print(result)
    power += 1
    result = 2 ** power

# Задача 1 сложная
def sum_of_digits(number):
    # Преобразуем число в положительное целое, чтобы обрабатывать отрицательные значения
    number = abs(number)

    # Инициализируем сумму цифр
    digit_sum = 0

    # Пока число не равно нулю, извлекаем последнюю цифру и добавляем ее к сумме
    while number != 0:
        digit = number % 10
        digit_sum += digit
        number //= 10

    return digit_sum

# Пример использования
number = int(input("Введите число: "))
total_sum = sum_of_digits(number)
print("Сумма цифр числа:", total_sum)
