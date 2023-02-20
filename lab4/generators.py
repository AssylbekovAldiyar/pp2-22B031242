
# 1. Создайте генератор, который генерирует квадраты чисел до некоторого числа N.

# def squares(n):
#     i = 0
#     while i <= n:
#         yield i ** 2
#         i += 1

# N = int(input())
# for square in squares(N):
#     print(square)




# 2. Напишите программу, использующую генератор, для вывода четных чисел от 0 до nв форме, разделенной запятыми, где nввод осуществляется с консоли
# def even_numbers(n):
#     i = 0
#     while i <= n:
#         if i % 2 == 0:
#             yield i
#         i += 1

# n = int(input("введите n "))
# even_nums = even_numbers(n)

# print(*even_nums, sep=", ")
#Звездочка (*) перед переменной even_nums в функции print используется для распаковки элементов генератора в качестве отдельных аргументов функции print.
#Без звездочки \была бы передана в функцию print в качестве одного аргумента - кортежа 



# # 3.Определите функцию с генератором, который может перебирать числа, которые делятся на 3 и 4, между заданным диапазоном от 0 до n.
# def div34(n):
#     for i in range(n+1):
#         if i % 3 == 0 or i % 4 == 0:
#             yield i

# n=int(input())
# for num in div34(n):
#     print(num)



# # 4.Реализуйте генератор, вызываемый
# # squaresдля получения квадрата всех чисел от (a) до (b). Протестируйте его с помощью цикла
# # for и распечатайте каждое из полученных значений.

# def squares(a, b):
#     for i in range(a, b+1):
#         yield i**2

# a=int(input())
# b=int(input())
# for num in squares(a,b):
#     print(num)



# # 5.Реализуйте генератор, который возвращает все числа от (n) до 0.

# def countdown(n):
#     while n >= 0:
#         yield n
#         n -= 1

# n=int(input())
# for num in countdown(n):
#     print(num)