# Сизов Дмитрий

# EASY
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# Учесть проверку на то что папка не пуста и на то, что такая папка уже существует
import os
def sozdat():
    for i in range (1,10):
        dir_path = os.path.join(os.getcwd(), f'dir_{i}')
        try:
             os.mkdir(dir_path)
        except FileExistsError:
            print(f'Папка dir_{i} уже существует')
def udalit():
    for i in range(1,10):
        dir_path2 = os.path.join(os.getcwd(), f'dir_{i}')
        try:
            os.rmdir(dir_path2)
        except OSError:
            print (f'В папке dir_{i} есть файлы')
sozdat()
udalit()

# Задача-2:
# Напишите скрипт, который выводит в консоль список файлов и папок в указанной директории.
import os
def put():
    print(os.listdir(os.getcwd()))
put()

# NORMAL

# Написать две программы:
# Одна принимает через argparse число N и текст S и в цикле N раз выводит S в консоль
# А вторая программа принимает через input число M
# И указанное кол-во раз спрашивает через input N и S и запускает первую программу через os.system
#
# Первая программа
import argparse
parser=argparse.ArgumentParser('Имя парсера')
parser.add_argument('n',type=int, help='Число N')
parser.add_argument('s',type=str, help='Текст S')
args=parser.parse_args()
for i in range(args.n):
    print(args.s)

# Вторая программа
import os
M=int(input('Введите число М: '))
for i in range(M):
    r=int(input('Введите число n: '))
    t = str(input('Введите текст s: '))
    command=f'python parse.py {r} {t}'
    os.system(command)

# HARD

# Написать программу для распаковки файлов в корневую из всех папок с расширениями (код взять с урока) и папки удалить

import os
BASE_PATH=r'D:\Archives\inside'
ext=set()
for i in os.listdir(BASE_PATH):
    if os.path.isfile(os.path.join(BASE_PATH,i)):
        ext.add(os.path.splitext(i)[1])
# print (ext)
for e in ext:
    if not os.path.exists(os.path.join(BASE_PATH,e)):
        os.mkdir(os.path.join(BASE_PATH,e))
for i in os.listdir(BASE_PATH):
    os.rename(os.path.join(BASE_PATH,i),os.path.join(BASE_PATH,os.path.splitext(i)[1],i))

dirs=set()
for i in os.listdir(BASE_PATH):
    dirs.add(i)
print (dirs)
if os.path.isdir(os.path.join(BASE_PATH,d)):
    os.rmdir(os.path.join(BASE_PATH,d))
for d in dirs:
    indirs = set()
    for ind in os.listdir(os.path.join(BASE_PATH,d)):
        os.rename(os.path.join(BASE_PATH,d,ind),os.path.join(BASE_PATH,ind))



