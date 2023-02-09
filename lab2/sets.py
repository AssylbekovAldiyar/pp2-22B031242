myset={"apple","banana","cherry"}
print(myset)
#sets are used to store multiple items in a single variable
# a set is a collection which is unordered,unchangeable,and unindexed

#set items
#set items are unordered,unchangeable,and do not allow duplicate values
#unordered
#unordered means that the items in a set do not have a defined order
"""
Set items can appear in a different order every time you use them, 
and cannot be referred to by index or key.
"""

"""
Once a set is created, you cannot change its items, 
but you can remove items and add new items.
"""
#duplicates not allowed
#Sets cannot have two items with the same value.

#Duplicate values will be ignored:
thissets={"a","b","c","a"}
print(thissets)

#get the length of a set
thisset={"a","b","c"}
print(len(thisset))

#set items-data types
#set can be of any data types:
#string,int,boolean
set1={"aa","bb","cc"}
set2={1,2,3}
set3={True,False,True}

#A set can contain different data types:
set1={1,"a",True}

#type()
myset={"apple","banana","cherry"}
print(type(myset))

#the set() constructor
thisset=set(("apple","banana","cherry"))
print(thisset)

"""
Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""

#access set items
thisset={"apple","banana","cherry"}
for x in thisset:
    print(thisset)

#Check if "banana" is present in the set:
thisset={"apple","banana","cherry"}
print("banana" in thisset)

#add set items
#Add an item to a set, using the add() method:
thisset={"a","b","c"}
thisset.add("d")
print(thisset)

#add sets
#To add items from another set into the current set, use the update() method.
thisset={"a","b","c"}
myset={"d","e","f"}
thisset.update(myset)
print(thisset)

#add any iterable
thisset={"a","b","c"}
mylist=["d","e"]
thisset.update(mylist)
print(thisset)

#remove set items
#To remove an item in a set, use the remove(), or the discard() method.
thisset={"a","b","c"}
thisset.remove("b")
print(thisset)

thisset={"a","b","c"}
thisset.discard("b")
print(thisset)

#using pop method:
myset={"a","b","c"}
x=thisset.pop()
print(x)
print(thisset)

#The clear() method empties the set:
myset={"a","b","c"}
myset.clear()
print(myset)

#loop sets
#You can loop through the set items by using a for loop:
thisset={"a","b","c"}
for x in thisset:
    print(x)

#join sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3=set1.union(set2)
print(set3)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#Both union() and update() will exclude any duplicate items.

#keep only the duplicates
#The intersection_update() method will keep only the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z=x.intersection(y)
print(z)

#Keep All, But NOT the Duplicates
"""
The symmetric_difference_update() method will 
keep only the elements that are NOT present in both sets.
"""
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z=x.symmetric_difference(y)
print(z)

#set exersizes
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")