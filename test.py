a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
"""1. Нужно вернуть список, который состоит из элементов, общих для этих двух списков."""
# c = []
# for i in a:
#     for e in b:
#         if i == e:
#             c.append(i)
# print(c)

# result = [i for i in a if i in b]
# result = list(set(a) & set(b))
# print(result)


"""2. Отсортируйте словарь по значению в порядке возрастания и убывания."""
# a = [1, 2, 5, 7, 9, 12, 50, 0]
# print(sorted(a))  
# print((sorted(a))[::-1])

# d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# print(sorted(d)) 
# print((sorted(d))[::-1])


"""3. Напишите программу для слияния нескольких словарей в один."""

# dict_a = {1:10, 2:20}
# dict_b = {3:30, 4:40}
# dict_c = {5:50, 6:60}

# dict_d = {}

# for i in dict_a, dict_b, dict_c:
#     dict_d.update(i)
# print(dict_d)
# result = {**dict_a, **dict_b, **dict_c}


"""4. Найдите три ключа с самыми высокими значениями в словаре """

# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}

# result = sorted(my_dict, key=my_dict.get, reverse=True)[:3]
# print(result)


'''очень странно но работает'''
# print(int('ABC', 16))


'''5. Напишите проверку на то, является ли строка палиндромом. Палиндром — это слово или фраза, которые одинаково читаются слева направо и справа налево.'''
# a = input()
# if a[::] == a[::-1]:
#     print('полиндром')
# else:
#     print('не полиндром')


'''6. Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.'''

# a = 3635

# print(f'days: {d} hours: {h} minutes: {m} secund: {s}')


"""Задача 10
Вы принимаете от пользователя последовательность чисел, разделённых запятой. Составьте список и кортеж с этими числами."""

# a = input('vod: ')
# t = tuple(a.split(','))
# l = a.split(',')
# print(t)
# print(l)

'''Задача 11
Выведите первый и последний элемент списка.  lst = [1, 2, 3, 4, 5]'''
# lst = [1, 2, 3, 4, 5]
# print(f'{lst[0]}, {lst[-1]}')




'''Задача 12
Напишите программу, которая принимает имя файла и выводит его расширение. Если расширение у файла определить невозможно, выбросите исключение'''
# try:
#     a = input()
#     b = a.split('.')
#     print(b[1])
# except IndexError:
#     print('Невозможно определить раширение')


'''Задача 13
При заданном целом числе n посчитайте n + nn + nnn.'''

# n = 5
# print(n + n*n + n*n*n)


'''Задача 14
Напишите программу, которая выводит чётные числа из заданного списка и останавливается, если встречает число 237.'''


'''Задача 15
Напишите программу, которая принимает два списка и выводит все элементы первого, которых нет во втором.
set_1 = set(['White', 'Black', 'Red'])
set_2 = set(['Red', 'Green'])'''



# print(set_1)
# print(set_2)

'''Задача 17
Сложите цифры целого числа.'''

# a = 5
# if len(str(a)) > 0:
#     b = a//10
#     c = a % 10
#     summa = b + c
#     print(summa)
# else:
#     print(a)


'''Задача 21
Нужно проверить, все ли числа в последовательности уникальны.'''
# a = [1, 5, 6, 78, 98 ,2, 3]
# if len(set(a)) != len(a):
#     print('not uniqe')
# else:
#     print('uniqe')


'''Задача 22
Напишите программу, которая принимает текст и выводит два слова: наиболее часто встречающееся и самое длинное.'''


'''Задача 20
С помощью анонимной функции извлеките из списка числа, делимые на 15.'''



# n = 1000
# c = 0
# for i in range(n):
#     for j in range(n):
#         if i == j or i + j == n - 1:
#             c += 1
#             print(1, end= ' ')
            
#         else:
#             print(0, end= ' ')
#     print() 
# print(c)

# for i in range(10):
#     for j in range(10):
#         if (i + j)% 2 == 1:
#             print(1, end= ' ')
#         else:
#             print(0, end= ' ')






import phonenumbers
from phonenumbers.phonenumberutil import (
    region_code_for_country_code,
    region_code_for_number,
)

pn = phonenumbers.parse(input('введите номер телефона: '))
print(region_code_for_country_code(pn.country_code))


















