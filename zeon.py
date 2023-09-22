# c = list([[1, 2], [2, 3], [4, 5]])
# print(c[:1])


# print(''10%3)


# a = [2, 17, 9, 22, 17, 24, 8, 11, 27]
# a = [x for x in a[::2] if x%2==0]
# print(a)


# def a(nums):
#     max_n = float("-inf")
#     for num in nums:
#         if num > max_n:
            
#     return max_n




# z = set('abc')
# z.add('san')
# z.update(set(['p', 'q']))
# print(z)


# f = None
# for i in range(5):
#     with open('app.log', 'w') as f:
#         if i >2:
#             break
# print(f.closed)


# def add(c, k):
#     c.test = c.test + 1
#     k = k + 1
# class Plus:
#     def __init__(self):
#         self.test = 0

# def main():
#     p = Plus()
#     index = 0
#     for i in range(0, 25):
#         add(p, index)

#     print("p.test=", p.test)
#     print("index=", index)
# main()




# candidates = [
#  {"name": "Vasya",  "scores": {"math": 58, "russian_language": 62, "computer_science": 48}, "extra_scores":0},
#  {"name": "Fedya",  "scores": {"math": 33, "russian_language": 85, "computer_science": 42},  "extra_scores":2},
#  {"name": "Petya",  "scores": {"math": 92, "russian_language": 33, "computer_science": 34},  "extra_scores":1}
# ]
# def find_top_20(candidates):
#     for i in candidates:
        
#         for v in i.values():
#             new_=[]
#             new_.append(v)
#             print(new_)

           
#                 # s = [i for i in v.values() ]
#                 # a = sum(s)
                 
# find_top_20(candidates)



#  sudo apt install gnome-tweaks
# важныо при установки горячих клавиш

# a = input()
# print('Этот файл имеет раширение', (a.split('.'))[1])


# a = input('Write: ')
# print(a.center(100)) #center(width) move on width  

# a =input()
# print(a.replace(a, 'okey')) #change first word on new word




# a = 'привет как 15 я тут типо сижу и не могу понять как это работает'
# print(a.split(' ')))





# a = ['js', 'python', 'java']

# ln = input('Which kind of languages do you know?: ')
# age = int(input('How old are you?: '))
# exp = int(input('How many years have you experiance?: '))
# p = int(input('How many do you want to get money?: '))

# if (ln in a) and ((18 < age) and (age < 65)) and (exp > 3):
#     print('You are can work with me. Welcome.')
# else:
#     print('sorry we can not work with you. Bye')


# print('Выберите действие:\n 1. Добавить новый город\n 2. Отобразить список городов\n 3. Заменить город\n 4. Удалить город\n 5. Выход')
# a = [1, 2, 3, 4, 5]

# list_ = []
# man = int(input())

# # first
# if man == a[0]:
#     city = input('City: ')
#     if city in list_:
#         print('we have this city')
#     else:
#         list_.append(city)
#         print(list_)
# # secound
# elif man == a[1]:
#     print(list_)
# # третий
# elif man == a[2]:
#     city = input('old city')
#     ncity = input('new city')
#     if city in list_:
#         list_.replace(city, ncity)
#         print('we chanced')
#     else: 
#         print('okey')
# # четвертый
# elif man == a[3]:
#     dell = input('Введит город которую надо удалить: ')
#     for i in list_:
#         if i == dell:
#             list_.remove(dell)
#         elif i == dell.isalnum():
#             print('Некорректное название')
#         else:
#             print('Такой город отсутствует')
# # пятый   
# else:
#     print('bye')









'''Даны координаты двух точек на плоскости, требуется определить,
лежат ли они в одной координатной четверти или нет (все координаты
отличны от нуля). Вводятся 4 числа: координаты первой точки (x1, y1) и
координаты второй точки (x2, y2).'''

# x1 = int(input())
# x2 = int(input())
# y1 = int(input())
# y2 = int(input())





# a = ['a', 'b', 'c', 'd']
# for i in range(len(a)):
#     print(i+1, a[i])
    
# a = 7 
# for i in range(1, 5):
#     i = 7
#     a = a * i
#     print(a)



# for i in range(1, 11):
#     print(i, end = ' ')
#     if i == 10:
#         while i > 0:
#             i -= 1
#             print(i, end= ' ')


# a = 10
# while a > 0:
#     a -= 1

#     print (a, end = ' ')

# a = 'l'
# a = a * 1

# print(len(a))
    

# # 1
# a = '*'
# for i in range(1, 6):
#     print(a * i)

# # 2
# a = '*'
# for i in range(1, 11):
#     s = a * i
#     print(' ', s)
# b = len(s)

    
# if b == 10:
#     while b > 1:
#         b -= 1
#         print(a * b)
          







i = 1
while i <= 10:    
    j = 1
    k = 1
    while k <= 10-i:
        print(' ',end = '') 
        k += 1
    while j <= i:
        print('*', end=' '*1) 
        j += 1
    print('\n')
    i += 1
while i <= 10-1:    
    a = 10+1
    b = 10-1
    while a <= i:
        print(' ', end='')
        a += 1
    while b >= i:
        print('*', end=' ')
        b -= 1
    print('\n')
    i += 1

        