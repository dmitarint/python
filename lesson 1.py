#ФИО: Сизов Дмитрий Владимирович

#Дз от Пака
#
#EASY
#Задача-1: Дано произвольное целое число (число заранее неизвестно).
#Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
#Подсказки:
#* постарайтесь решить задачу с применением арифметики и цикла while;
#* при желании решите задачу с применением цикла for.

#ВЫПОЛНЕНИЕ ЗАДАНИЯ:
#number=str(input ("введите число "))
#count = len(str(number))
#i=0
#while i<count:
#    print (number[i])
#    i+=1

#Задача-2: Исходные значения двух переменных запросить у пользователя.
#Поменять значения переменных местами. Вывести новые значения на экран.
#Подсказка:
#* постарайтесь сделать решение через дополнительную переменную
#или через арифметические действия
#Не нужно решать задачу так:
#print("a = ", b, "b = ", a) - это неправильное решение!

#ВЫПОЛНЕНИЕ ЗАДАНИЯ:
#a=input ('Введите первое значение: ')
#b=input ('Введите второе значение: ')
#per = a
#a = b
#b = per
#print ('Первое значение теперь такое: '+a)
#print ('Второе значение теперь такое: '+b)

#Задача-3: Запросите у пользователя его возраст.
#Если ему есть 18 лет, выведите: "Доступ разрешен",
#иначе "Извините, пользование данным ресурсом только с 18 лет"

#ВЫПОЛНЕНИЕ ЗАДАНИЯ:
#age = int(input('Сколько тебе лет? '))
#if age>=18:
#    print ('Доступ разрешен')
#else:
#    print('Извините, пользование данным ресурсом только с 18 лет')

#NORMAL
#Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
#Например, дается x = 58375.
#Нужно вывести максимальную цифру в данном числе, т.е. 8.
#Подразумевается, что мы не знаем это число заранее.
#Число приходит в виде целого беззнакового.
#Подсказки:
#* постарайтесь решить задачу с применением арифметики и цикла while;
#* при желании и понимании решите задачу с применением цикла for.

#ВЫПОЛНЕНИЕ ЗАДАНИЯ:
#number=str(input ("введите число "))
#count = len(str(number))
#i=0
#highnumber=0
#while i<count:
#    if int(number[i])>highnumber:
#        highnumber=int(number[i])
#    i+=1
#print ('Самое большая цифра: '+ str(highnumber))

#Задача-2: Исходные значения двух переменных запросить у пользователя.
#Поменять значения переменных местами. Вывести новые значения на экран.
#Решите задачу, используя только две переменные.
#Подсказки:
#* постарайтесь сделать решение через действия над числами;
#* при желании и понимании воспользуйтесь синтаксисом кортежей Python.
#a = input("Input a: ")
#b = input("Input b: ")
#a,b = b,a

#ВЫПОЛНЕНИЕ ЗАДАНИЯ:
#a=int (input ('Введите первое значение: '))
#b=int (input ('Введите второе значение: '))
#a=int(a*b)
#b=int(a/b)
#a=int(a/b)
#print ('Первое значение теперь такое: '+str(a))
#print ('Второе значение теперь такое: '+str(b))

#Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
#ax² + bx + c = 0.
#Коэффициенты уравнения вводятся пользователем.
#Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
#import math
#math.sqrt(4) - вычисляет корень числа 4

#ВЫПОЛНЕНИЕ ЗАДАНИЯ:
#import math
#a=int (input('введите коэффициент а; '))
#b=int (input('введите коэффициент b; '))
#c=int (input('введите коэффициент c; '))
#D=b**2-4*a*c
#if a==0:
#    print ('уравнение не является квадратным')
#elif D<0:
#    print('оба корня являются комплексными числами')
#else:
#    x1 = (-b + math.sqrt(D))/(2*a)
#    x2 = (-b - math.sqrt(D))/(2*a)
#    print (str(x1))
#    print (str(x2))

#HARD
#Задание-1:
#Пользователь вводит число определите, является ли данное число простым.
# Делится только на себя и на единицу

#ВЫПОЛНЕНИЕ ЗАДАНИЯ:
#import math
#simple=int(input ('введите число: '))
#simple=int(math.fabs(simple))
#i=0
#prostoe=0
#for i in range(simple):
#        if i==0 or i==1:
#            continue
#        est=simple%i
#        if est==0:
#            print ('число %s не является простым'% (str(simple)))
#            prostoe=1
#            break
#if prostoe==0:
#    print('число %s является простым' % (str(simple)))

#Задание-2
#Найдите n-ое число Фибоначчи
#ВЫПОЛНЕНИЕ ЗАДАНИЯ:
#n=int(input('введите номер числа Фибоначчи: '))
#f0=0
#f1=1
#if n==0:
#    print ('Число Фибоначи под номером %s равно: '%(n), str(f0))
#elif n==1:
#    print('Число Фибоначи под номером %s равно: ' % (n), str(f1))
#else:
#    for i in range(2,n+1):
#        f2=f0+f1
#        f0=f1
#        f1=f2
#    print ('Число Фибоначи под номером %s равно: '%(n), str(f2))

#Задание-3
#Вывести на экран:
#AAABBBAAABBBAAABBB
#BBBAAABBBAAABBBAAA
#AAABBBAAABBBAAABBB
#(таких строк n, в каждой строке m троек AAA)

#НЕ ПОНЯЛ ЗАДАЧИ!