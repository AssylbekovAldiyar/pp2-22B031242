# from functools import reduce

# my_list = [1, 2, 3, 4, 5]

# product = reduce(lambda x, y: x * y, my_list)

# print(product)
#2
# def solve(string):
#     upper = sum(1 for i in string if i.isupper())
#     lower = sum(1 for i in string if i.islower())
#     return (upper, lower)

# string = "IsaAldikMusik"
# result = solve(string)
# print(result)  


# #3
# def solve(string):
#     return string == string[::-1]

# string = "bibabobabib"
# result = solve(string)
# print(result)  


#4
# import time
# import math

# def kvadratmilisec(number, milisec):
#     time.sleep(milisec/1000)
#     return math.sqrt(number)
# # Функция sleep() модуля time приостанавливает выполнение вызывающего потока на указанное количество секунд secs .
# number = 25100
# milisec = 2123
# result = kvadratmilisec(number, milisec)
# print(f"Square root of {number} after {milisec} milisec is {result}")

# #5
# a = (True, True, False, True)
# b = (1==1, 2==2, 2<3, 1000<=pow(10,10)) 
# print(all(a), '\n', all(b),sep='')