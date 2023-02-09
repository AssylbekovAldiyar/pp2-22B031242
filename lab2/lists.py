list=["edil","adau"]
print(list)

#allow duplicates
list=["a","b","c","a"]
print(list)

#list length
list=["a","b","c"]
print(len(list))

#list item-data types
list1=["a","b","c"]
list2=[1,2,3]
list3=[True,False,False]
print(list1)
print(list2)
print(list3)

list4=["a",2,True]

#type()
mylist=["a","b","c"]
print(type(mylist))

#access items
thislist=["a","b","c"]
print(thislist[1])

#negative indexing
thislist=["a","b","c"]
print(thislist[-1])

#range of indexes
thislist=["a","b","c","s"]
print(thislist[1:3])
thislist=["a","b","c","d","e"]
print(thislist[:3])
thislist=["a","c","b","d","e"]
print(thislist[2:])
thislist=["a","b","c","d","e"]
print(thislist[-2:-4])

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

  #change item value
  list=["a","b","c"]
  list[1]="d"
  print(list)

#change a range of item value
list=["a","b","c","d"]
list[1:3]=["e","f"]
print(list)

list=["a","b","c"]
list[1:2]=["e","f"]
print(list)

#insert items
list=["a","b","c"]
list.insert(2,"e")
print(list)

#append items
list=["a","b","c"]
list.append("d")
print(list)

#extend list
thislist=["a","b","c"]
tropical=["d","e","f"]
thislist.extend(tropical)
print(thislist)

#add any iterable
thislist=["a","b","c"]
thistuple=("d","e")
thislist.extend(thistuple)
print(thislist)

#remove list items
thislist=["aa","bb","cc"]
thislist.remove("bb")
print(thislist)

#remove specified index
thislist=["a","b","c"]
thislist.pop(1)
print(thislist)

thislist=["a","b","c"]
thislist.pop()
print(thislist)

thislist=["a","b","c"]
del thislist[0]
print(thislist)

thislist=["a","b","c"]
del thislist

#clear the list
thislist=["a","b","c"]
thislist.clear()
print(thislist)

#loop through a list
list=["aa","bb","cc"]
for x in list:
  print(x)

#loop through the index numbers
list=["aa","bb","cc"]
for i in range(len(list)):
  print(list[i])

#using a while loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#looping using list comprehension
list=["a","b","c"]
[print(x) for x in list]

#list comprehension
fruits =["apple","banana","cherry","kiwi","mango"]
newlist=[]

for x in fruits:
  if "a" in x:
    newlist.append(x)
  
  print(newlist)

fruits=["apple","banana","cherry","kiwi","mango"]
newlist=[x for x in fruits if "a" in x]
print(newlist)

fruits=["aa","bb","cc"]
newlist=[x for x in fruits if x!="aa"]
print(newlist)

fruits=["aa","bb","cc"]
newlist=[x for x in fruits]
print(newlist)

#iterable
newlist=[x for x in range(10)]

newlist=[x for x in range(10) if x<5]

fruits=["apple","banana","cherry"]
newlist=[x.upper() for x in fruits]
print(newlist)

fruits=["aa","bb","cc"]
newlist=['hello' for x in fruits]
print(newlist)

fruits=["apple","banana","cherry"]
newlist=[x if x!="banana" else "orange" for x in fruits]
print(newlist)

 #sort lists
  #Sort List Alphanumerically
  thislist=["b","a","d","c"]
  thislist.sort()
  print(thislist)

  thislist=[100,5,34,43]
  thislist.sort()
  print(thislist)

#sort descending
thislist=["orange","mango","kiwi","pineapple","banana"]
thislist.sort(reverse=True)
print(thislist)

thislist=[10,23,45,66,33]
thislist.sort(reverse=True)
print(thislist)

def myfunc(n):
  return abs(n-50)

  thislist=[100,50,23,44,22]
  thislist.sort(key=myfunc)
  print(thislist)

#case insensitive sort
thislist=["banana","Orange","Kiwi","cherry"]
thislist.sort()
print(thislist)

thislist=["banana","Orange","Kiwi","cherry"]
thislist.sort(key=str.lower)
print(thislist)

#Reverse Order
thislist=["banana","Orange","Kiwi","cherry"]
thislist.reverse()
print(thislist)

#copy a list
thislist=["apple","banana","cherry"]
mylist=thislist.copy()
print(mylist)

thislist=["apple","banana","cherry"]
mylist=list(thislist)
print(mylist)

#join lists
#join two lists
list1=["a","b","c"]
list2=[1,2,3]

list3=list1+list2
print(list3)

list1=["a","b","c"]
list2=[1,2,3]

for x in list2:
    list1.append(x)

    print(list1)

list1=["a","b","c"]
list2=[1,2,3]
list1.extend(list2)
print(list1)

