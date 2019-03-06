# EASY

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

# def skruglenie(a, b):
#     b=int(b)
#     razd = a.split('.')
#     print ('razd ',razd)
#     desyatie = str(razd[1])
#     print('desyatie ', desyatie)
#     if int(desyatie[b+1]) < 5:
#         result=f'{razd[0]}.{desyatie[0:b]}'
#     else:
#         result=f'{razd[0]}.{int(desyatie[0:b])+1}'
#     return result
# number = input('введите число: ')
# znaki = input('введите количество знаков после запятой: ')
# print(skruglenie(number,znaki))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

# def proverka(a):
#     a=str(a)
#     if int(a[0])+int(a[1])+int(a[2])==int(a[3])+int(a[4])+int(a[5]):
#         result=True
#     else:
#         result=False
#     return result
#
# proof=False
# while proof==False:
#     bilet=input('Введите шестизначный номер билета ')
#     if len(bilet)==6 and bilet.isdigit():
#         proof=True
#
# if proverka(bilet)==True:
#     print ('Ваш билет выиграл!')
# else:
#     print ('Ваш билет проиграл. Может повезет в следующий раз')

# NORMAL

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

# def fibonachi(n, m):
#     a = [1, 1]
#     for i in range(1, m + 1):
#             a.append(a[i] + a[i - 1])
#     print(a[n-1:m])
#
# n = int(input('введите номер первого числа Фибоначчи: '))
# m = int(input('введите номер последнего числа Фибоначчи: '))

# fibonachi(n, m)

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()
#
# def sorting(a):
#     for j in range(len(a)):
#         for i in range(1, len(a) - j):
#             if a[i - 1] > a[i]:
#                 a[i - 1], a[i] = a[i], a[i - 1]
#     print(a)
#
#
# spisok = []
# c = 0
# while c == 0:
#     a = input('Введите число. Для окончания цикла введите Enter ')
#     if a == '': break
#     spisok.append(int(a))
#
# sorting(spisok)

# HARD

# Задание-1

# Написать консольное меню вида:

# 1. Добавить
# 2. Удалить
# 3. Распечатать
# 4. Посчитать
# 5. Выйти

# Надо чтобы
# а) Можно было удобно менять порядок меню и\или добавлять\удалять пункты меню
# б) Каждое действие (добавить, удалить и тд) должно быть функцией
# в) У пользователя надо спросить номер команды
# г) Программа не должна завершаться пока не введется команда Выйти
# д) Проверять на ввод ошибочных данных, там где они могут появиться

database = []


def add():
    global database
    data = input('введите данные: ')
    database.append(data)


def delete():
    global database
    print(f'Выберите номер компонента, который необходимо удалить')
    for i, m in enumerate(database, start=1):
        print(f'{i}. {m}')
    delt = input()
    if delt.isdigit()==False or int(delt) >= len(database) or int(delt) < 1:
        print("неверно выбран элемент в списке")
    else:
        delt=int(delt)
        del database[delt-1]



def print_data():
    global database
    for i in database:
        print(i)


def calculate():
    global database
    calc = 0
    for i in range(len(database)):
        try:
            int(database[i])
        except Exception:
            continue
        calc = calc + int(database[i])
    print('Сумма чисел в базе равна: ', calc)


def print_menu(menu):
    for i, m in enumerate(menu, start=1):
        print(f'{i}. {m}')


def get_command(menu):
    command = input('Input command: ')
    try:
        int(command)
    except Exception:
        return -1
    if 1 <= int(command) <= len(menu):
        return int(command)-1
    else:
        return -1


menu = ['Add', 'Delete', 'Print', 'Calculate', 'Exit']
commands = [add, delete, print_data, calculate, exit]
truth=True
while truth == True:
    print_menu(menu)
    command = get_command(menu)
    if command == -1:
        print('wrong command!')
        continue
    commands[command]()
