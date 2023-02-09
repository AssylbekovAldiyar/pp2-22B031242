# # 1.
# class SampleClass:
#     def getString(self):
#         self.string = input("Enter a string: ")
    
#     def printString(self):
#         print(self.string.upper())

# get = SampleClass()
# get.getString()
# get.printString()

# # 2.
# class Shape:
#     def __init__(self):
#         pass

#     def area(self):
#         return 0

# class Square(Shape):
#     def __init__(self, length):
#         self.length = length

#     def area(self):
#         return self.length * self.length


# shape = Shape()
# print(shape.area()) 

# square = Square(5)
# print(square.area())


# 3. 
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

# rectangle = Rectangle(5, 10)
# print(rectangle.area()) 


# # 4.
# import math

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def show(self):
#         print("Point({}, {})".format(self.x, self.y))

#     def move(self, x1, y2):
#         self.x += x1
#         self.y += y2

#     def dist(self, other):
#         x1 = self.x - other.x
#         y2 = self.y - other.y
#         return math.sqrt(x1**2 + y2**2) #** умножение в степень

# p1 = Point(0, 0)
# p2 = Point(3, 4)

# p1.show() 
# p2.show() 

# p1.move(1, 1)
# p1.show() 

# print("Distance between p1 and p2:", p1.dist(p2)) 

# # 5.
# class Account:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print("деньги приняты,ваш баланс: ${}".format(self.balance))

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("средства недостуны!")
#         else:
#             self.balance -= amount
#             print("снятие потверждено,отстаток: ${}".format(self.balance))

# acct = Account("Isa", 100)

# acct.deposit(50) # Deposit Accepted. Current balance: $150
# acct.withdraw(75) # Withdrawal Accepted. Current balance: $75
# acct.withdraw(200) # Funds Unavailable!




# # 6. 
# numbers = [1,2,3,4,5,6,7,8,9,10,11]

# prime = lambda x: all(x % i != 0 for i in range(2, x))

# result_it = filter(prime, numbers)
# result_list = list(result_it)

# print(result_list)
