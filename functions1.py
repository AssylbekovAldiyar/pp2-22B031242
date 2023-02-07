import random
import itertools


# # 1.
# def convert(grams: float) :
#     ounces: float = 28.3495231 * grams
#     return ounces

# grams=int(input())
# print(convert(grams))


# # 2.
# def celsius(f: float) :
#     c: float = (5 / 9) * (f - 32)
#     return c

# f=int(input())
# print(celsius(f))


# # 3.
# def solve(numheads: int, numlegs: int) :
#     for chickens in range(0, numheads + 1):
#         rabbits = numheads - chickens
#         if numlegs == (chickens * 2 + rabbits * 4):
#             return chickens, rabbits
#     return 0, 0

# numlegs=94
# numheads=35
# print(solve(numheads,numlegs))


# # 4.
# def prime(numbers: list) :
#     if_prime = lambda x: all(x % i != 0 for i in range(2, x))
#     result_it = filter(if_prime, numbers)
#     result_list = list(result_it)
#     return result_list

# numbers=[]
# for i in range(10):
#     x=int(input())
#     numbers.append(x)
# print(prime(numbers))


# # 5.
# def permutations(string: str) :
#     print([x for x in itertools.permutations(string, len(string))])

# string = input()
# permutations(string)

# # 6.
# def reverse_words(sentence: str) :
#     reversed_words: list = reversed(sentence.split())
#     return " ".join(reversed_words)

# sentence = input()
# print(reverse_words(sentence))


# # 7
# def has_33(nums: list) :
#     for i in range(len(nums) - 1):
#         if nums[i:i + 2] == [3, 3]:
#             return True
#     return False


# numbers = [1, 2, 3, 4, 5, 6, 7] 
# print(has_33(numbers))  


# # 8.
# def spy_game(nums):
#     code = [0, 0, 7, "x"]
#     for num in nums:
#         if num == code[0]:
#             code.pop(0)  
#     return len(code) == 1


# print(spy_game([1,2,4,0,0,7,5])) # True
# print(spy_game([1,0,2,4,0,5,7])) # True
# print(spy_game([1,7,2,0,4,5,0])) # False


# 9.
# def sphere_volume(radius: float) :
#     return (4 / 3) * (3.14 * (radius ** 3))

# radius = int(input())
# print(sphere_volume(radius))



# 10.
# def unique_list(numbers: list) :
#     result = []
#     for num in numbers:
#         if num not in result:
#             result.append(num)
#     return result

# numbers = [1,2,3,3,3,4,5,6,7,8,5,3,2]
# print(unique_list(numbers))



# # 11. 
# def is_palindrome(string: str) :
#     return string == string[::-1]

# string = input()
# print(is_palindrome(string))



12. 
def histogram(numbers: list) :
    for num in numbers:
        print('*' * num)

histogram([4, 9, 7])


# # 13. 
# def game():
#     print("Hello! What is your name?")
#     name = input()
#     print("Well,", name, "I am thinking of a number between 1 and 20.")
#     number = random.randint(1, 20)
#     i = 1
#     guess=-1
#     while guess != number:
#         print("Take a guess.")
#         guess = int(input())
#         if guess < number:
#             print("Your guess is too low.")
#         elif guess > number:
#             print("Your guess is too high.")
#         i = i + 1   
#     print("Good job,", name, "! You guessed my number in", i, "guesses!")

# game()