#4 built-in data types in python:
#set,list,tuples,dictionary

thistuples=("apple","banana","cherry")
print(thistuples)

#allow duplicates
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#tuple length
thistuple=("apple","banana","cherry")
print(len(thistuple))

#create tuple with one item
thistuple=("apple",)
print(type(thistuple))

#tuple items-data type
tuple1=("apple","banana","cherry") #string
tuple2=(1,2,3,4,5) #int
tuple3=(True,False,True) #boolean

#a tuple with string,int,boolean values
tuple1=("abc",34,True)

#type()
mytuple=("apple","banana","cherry")
print(type(mytuple))

#the tuple constructor
thistuple=tuple(("apple","banana","cherry"))
print(thistuple)

"""
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""

#access tuple items
thistuple=("apple","banana","cherry")
print(thistuple[1])

#negative indexing
thistuple=("apple","banana","cherry")
print(thistuple[-1])

#range of indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#This will return the items from position 2 to 5.

#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

#range of negative indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

#check if item exist
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

#update tuples
x=("apple","banana","cherry")
y=list(x)
y[1]="kiwi"
x=tuple(y)
print(x)

#add items
thistuple=("apple","banana","cherry")
y=list(thistuple)
y.append("orange")
thislist=tuple(y)

#add tuple to tuple
thistuple=("apple","banana","cherry")
y=("orange",)
thistuple +=y
print(thistuple)

#remove items
thistuple=("a","b")
y=list(thistuple)
y.remove("a")
thistuple=tuple(y)

#unpack tuples
fruits=("apple","banana","cherry")
(a,b,c)=fruits
print(a)
print(b)
print(c)

#using asterisk
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(a,*b,c)=fruits
print(a)
print(b)
print(c)

#loop tuples
#You can loop through the tuple items by using a for loop
mytuple=("apple","banana","cherry")
for x in mytuple:
  print(x)

#loop through the index number
#use the range() and len() functions to create a suitable iterater.
mytuple=("apple","banana","cherry")
for i in range(len(mytuple)):
  print(mytuple[i])

#Using a while loop
#You can loop through the tuple items by using a while loop
thistuple=("apple","banana","cherry")
i=0
while i<len(thistuple):
  print(thistuple[i])
  i=i+1

#Join tuples
#To join two or more tuples you can use + operator
tuple1=("apple","banana","cherry")
tuple2=(1,2,3)

tuple3=tuple1+tuple2
print(tuple3)

#multiply tuples
fruits=("apple","banana","cherry")
mytuple=fruits*2
print(mytuple)

#tuple methods
#Python has two built-in methods that you can use on tuples
#count()  #Returns the number of times a specified value occurs in a tuple
#index()  #Searches the tuple for a specified value and returns the position
         # of where it was found


#tuple exercises
fruits = ("apple", "banana", "cherry")
print(fruits[0])


