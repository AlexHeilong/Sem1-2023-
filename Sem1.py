### Семинар 1. Повторение - мать учения

# Задача 1
# За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров?
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
#
# **Input:**
# n = 700
# m = 750
# **Output:**
# 2

# Вариант 1
# import math
#
# per_day = int(input('Введите сколько машина проезжает за день: '))
# total_distance = int(input('Введите сколько машина должна проехать всего: '))
#
# print(f'На маршрут {total_distance} км машина потратит {math.ceil(total_distance/per_day)} дня')

# Вариант 2
#
# per_day = int(input('Введите сколько машина проезжает за день: '))
# total_distance = int(input('Введите сколько машина должна проехать всего: '))
# days = (total_distance + per_day - 1)//per_day  # // деление нацело
# print(f'На маршрут {total_distance} км машина потратит {days} дня')

#_______________________
# Задача 2
# #В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них
# новыми партами. За каждой партой может сидеть два учащихся.
# Известно количество учащихся в каждом из трех классов.
# Выведите наименьшее число парт, которое нужно приобрести для них.
# **Input:**
# 20
# 21
# 22
# **Output:**
# 32

# class_one = 20
# class_two = 21
# class_three = 22
#
# class_one_desks = (class_one + 1)//2
# class_two_desks = (class_two + 1)//2
# class_three_desks = (class_three + 1)//2
#
# print(f'Для трех классов нужно приобрести {class_one_desks + class_two_desks + class_three_desks}')
# #___________________________

# Задача 3

# Вагоны в электричке пронумерованы натуральными числами,
# начиная с 1 (при этом иногда вагоны нумеруются от «головы» поезда,
# а иногда – с «хвоста»; это зависит от того, в какую сторону едет электричка).
# В каждом вагоне написан его номер. Витя сел в i-й вагон от головы поезда и обнаружил,
# что его вагон имеет номер j. Он хочет определить, сколько всего вагонов в электричке.
# Напишите программу, которая будет это делать или сообщать,
# что без дополнительной информации это сделать невозможно.

# i = int(input('Введите вагон по счету: '))
# j = int(input('Введите номер вагона: '))
# if i != j:
#     print(f'количество вагонов в поезде {j + (i - 1) }')
# else:
#     print(f'недостаточно информации')
#
# ____________________________________________

# Задача 4

# Дано натуральное число. Требуется определить, является ли год с данным номером високосным.
# Если год является високосным, то выведите YES, иначе выведите NO.
# Напомним, что в соответствии с григорианским календарем, год является високосным,
# если его номер кратен 4, но не кратен 100, а также если он кратен 400.
# **Input:**
# 2016
# **Output:**
# YES

year = int(input('Введите год: '))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'{year} год - високосный')
else:
    print(f'{year} год - невисокосный')
