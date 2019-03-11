# Дмитрий Сизов
# EASY
# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

# import random
# list = [random.randint(0,9) for _ in range (10)]
# list2 = [e ** 2 for e in list[:]]
# print(list)
# print(list2)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

# list1=['банан','яблоко','апельсин','киви','лимон']
# list2=['виноград','яблоко','слива','киви','персик']
# together=[]
# for i in list1:
#     if i in list2:
#         together.append(i)
# print (together)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

# import random
#
# list = [random.randint(-100, 200) for _ in range(100)]
# final=[]
# for i in list:
#     if i%3==0 and i>0 and not i%4==0:
#         final.append(i)
# print (final)


# NORMAL
# Задание-1:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.
# import random
# f=open('data.txt','w')
# a=[random.randint(0,9) for _ in range (2500)]
# f.write(f'{"".join([str(i) for i in a])}')
# f.close()
# with open ('data.txt','r') as f:
#     per=str(f.read())
#     print (per)
#     count=1
#     lin=1
#     for i in range(len(per)):
#         if int(per[i])==int(per[i-1]):
#             count+=1
#             if count>lin:
#                 lin=count
#                 cifra=per[i]
#         else:
#             count=1
#     print(f'самая большая длина {lin} соответствует цифре {cifra}')


# Задание-2
# Сформировать квадратную матрицу, в каждой строке которой находится ровно один ноль на случайном месте, остальные элементы тоже рандомные. Пользователь вводит размер
# H
# import random
# razmer=int(input('введите размер матрицы: '))
# matrix=[] #объявляем матрицу списком
# for i in range(razmer):
#     matrix.append([]) #объявляем каждый i-й элемент матрицы списком
#     for j in range(razmer): # создаем случайные списки в i-м элементе длиной "размер"
#         matrix[i].append(random.randint(-10,10))
#     proof=0
#     count=0
#     for _ in range(razmer): #если в созданном списке есть ноль то проверка "proof" меняется на единиццу, и ведется счетчик количества нулей в линии
#         if matrix[i][_]==0:
#             proof=1
#             count+=1
#             if count>1: #если счетчик перевалил за единицу, то все последующие нули меняются на случайное число от 1 до 10
#                 matrix[i][_]=random.randint(1,10)
#     if proof==0: #если в линии не оказалось нулей, то случайному элементу списка присваивается ноль
#         matrix[i][random.randint(0,razmer)]=0
# for line in matrix:
#     print (line)

# HARD

# Задание-1
# Куб состоит из n^3 прозрачных и непрозрачных элементарных кубиков. Имеется ли хотя бы один просвет по каждому из трех измерений?
# Если это так, вывести координаты каждого просвета. Куб задается трехмерной матрицей из 0 и 1.

# import random
#
# razmer = int(input('введите размер матрицы: '))
# matrix = []  # объявляем матрицу списком
# for i in range(razmer):
#     matrix.append([])
#     for j in range(razmer):
#         matrix[i].append([])
#         for k in range(razmer):
#             matrix[i][j].append([random.randint(0, 1)])
# for i in range(razmer):  # проверка плоскости i,j
#     for j in range(razmer):
#         summa = 0
#         for k in range(razmer):
#             summa = sum(matrix[i][j][k]) + sum(matrix[i][j][k - 1])
#         if summa == 0:
#             print(f'в измерении i{i}-j{j} имеется просвет')
#
# for i in range(razmer):  # проверка плоскости i,k
#     for k in range(razmer):
#         summa = 0
#         for j in range(razmer):
#             summa = sum(matrix[i][j][k]) + sum(matrix[i][j - 1][k])
#         if summa == 0:
#             print(f'в измерении i{i}-k{k} имеется просвет')
#
# for k in range(razmer):  # проверка плоскости k,j
#     for j in range(razmer):
#         summa = 0
#         for i in range(razmer):
#             summa = sum(matrix[i][j][k]) + sum(matrix[i - 1][j][k])
#         if summa == 0:
#             print(f'в измерении k{k}-j{j} имеется просвет')

# for i in range(razmer):
#     for j in range(razmer):
#         print (str(matrix[i][j])+str(i)+str(j))
# Задание-2
# Дан pwd.txt с логинами и паролями. Найдите топ10 самых популярных паролей.
#

# Задание-3
# Пользователь вводит положительное целое число больше 1
# Нужно создать квадратную матрицу этого размера и по спирали заполнить её числами

# 5
#  1  2  3  4 5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 13 12 11 10 9

# 3
# 1 2 3
# 8 9 4
# 7 6 5
