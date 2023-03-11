import os
import shutil


#1Напишите программу на Python, чтобы перечислить только каталоги, файлы и все каталоги, файлы по указанному пути.
def list_files(specified_path) :
    if not os.path.exists(specified_path):
        print("путь не существует.")
        return
#Этот блок кода проверяет, существует ли указанный путь с помощью os.path.exists()функции.
# Если путь не существует, функция печатает сообщение и возвращается, ничего не делая.

    for root, dirs, files in os.walk(specified_path):
#Эта строка использует os.walk()функцию для перебора всех каталогов и файлов по указанному пути.
        print(f"путь: {root}")
        if dirs:
            print("кталоги: ")
            for dir_name in dirs:
                print(dir_name)
        if files:
            print("файлы: ")
            for file_name in files:
                print(file_name)

#\Users\Алдияр\Desktop\Proggrams\pp2\lab6\

path = input("введите путь к листу: ")
list_files(path)


# #2 Напишите программу Python для проверки доступа к указанному пути. 
# #Проверить существование, читаемость, возможность записи и исполняемость указанного пути
# def check_access(specified_path) :
#     if not os.path.exists(specified_path):
#         print("Path does not exist.")
#         return
# #Функция сначала проверяет, существует ли указанный путь с помощью функции os.path.exists().
# #Если путь не существует, функция выводит сообщение об ошибке и возвращает управление.
#     print(f"Checking access for {specified_path}")

#     exists = os.path.exists(specified_path)
#     readable = os.access(specified_path, os.R_OK)
#     writable = os.access(specified_path, os.W_OK)
#     executable = os.access(specified_path, os.X_OK)

#     print(f"существует: {exists}")
#     print(f"четается: {readable}")
#     print(f"записывается: {writable}")
#     print(f"исполняется: {executable}")
# #Затем функция вызывает функцию os.access() с аргументом specified_path и флагами os.R_OK, os.W_OK и os.X_OK, чтобы проверить,
# #имеет ли пользователь доступ к этому пути на чтение, запись и выполнение 
# # Результаты проверок сохраняются в соответствующие переменные типа bool.

# # \Users\Алдияр\Desktop\Proggrams\pp2\lab6\
# path = input("введи путь шоб проверить ")
# check_access(path)



# #3 Напишите программу на Python, чтобы проверить, существует ли данный путь или нет.
# # Если путь существует, найдите имя файла и часть каталога данного пути.
# def path_info(specified_path) :
#     if not os.path.exists(specified_path):
#         print("пути нет.")
#         return
# #Функция сначала проверяет, существует ли указанный
# #пользователем путь с помощью функции os.path.exists().

#     print(f"проверка пути {specified_path}")
#     dir_name, file_name = os.path.split(specified_path)
#     print(f"папка: {dir_name}")
#     print(f"имяфайла: {file_name}")
# #Затем функция вызывает функцию os.path.split() с аргументом specified_path,
# #чтобы разбить путь на путь к папке и имя файла.

# #\Users\Алдияр\Desktop\Proggrams\pp2\lab6\dir.py
# path = input("введи путь шоб узнать: ")
# path_info(path)


# #4 Напишите программу на Python для подсчета количества строк в текстовом файле.
# def count_lines(specified_path) :
#     if not os.path.exists(specified_path):
#         print("пути не существует.")
#         return

#     if not os.path.isfile(specified_path):
#         print(f"{specified_path} не файл.")
#         return

#     result: int = 0
#     with open(specified_path, "r") as file:
#         for i in file:
#             result += 1
#     return result

# ##\Users\Алдияр\Desktop\Proggrams\pp2\lab6\dir.py

# file_path = input("введи путь для суммы строк ")
# num_lines = count_lines(file_path)
# print(f"количество линий {file_path}: {num_lines}")


# #5 Напишите программу Python для записи списка в файл.
# def solve(specified_path, list_data) :
#     with open(specified_path, "w") as file:
#         for i in list_data:
#             file.write(i + "\n")


# file_path = input("введи путь для нового файла ")
# data = input("Введите список элементов, разделенных пробелами: ").split()
# # \Users\Алдияр\Desktop\Proggrams\pp2\lab6\txt.py
# solve(file_path, data)
# print(f"записано в {file_path}.")


# # #6 Напишите программу Python для создания 26 текстовых файлов с именами A.txt, B.txt и т. д. до Z.txt.
# def generate_files() :
#     for i in range(ord("A"), ord("Z") + 1):
#         #ord() преобразует букву в число по аски коду
#         letter = chr(i)
#         # аски код преобразуется обратно в символ с помощью функции chr()
#         filename =  f"C:\\Users\\Алдияр\\Desktop\\Proggrams\\pp2\\lab6\\papka\\{letter}.txt"
#         with open(filename, "w") as file:
#             file.write(letter)

# # \Users\Алдияр\Desktop\Proggrams\pp2\lab6\papka\

# generate_files()

# # 7 Напишите программу Python для копирования содержимого файла в другой файл.
# def copy_file(source_path, dest_path):
#     if not os.path.exists(source_path):
#         print("не существует")
#         return

#     if not os.path.isfile(source):
#         print("это не файл")
#         return

#     with open(source_path) as file:
#         with open(dest_path, "w") as new_file:
#             new_file.write(file.read())


# source = input("напиши путь с которого нужно скопировать: ")
# dest = input("путь в которой введётся: ")
# copy_file(source, dest)


# #8 Напишите программу Python для удаления файла по указанному пути. Перед удалением проверьте доступ и существует ли указанный путь.
# def delete_file():
#     path = input("Введите путь к файлу, который нужно удалить: ")
#     if not os.path.exists(path):
#         print("Файл не существует.")
#         return
#     if not os.access(path, os.W_OK):
#         print(f"Невозможно удалить файл {path}. Нет прав на запись.")
#         return
#     os.remove(path)
#     print(f"Файл {path} удален.")

# delete_file()