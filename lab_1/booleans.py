print(10>9) #true
print(9>10) #false
print(9==10) #false

a=20
b=10
if a>b:
  print("a is greater than b")
else:
  print("b is greater than a")

#evaluate values and variables
print(bool("hello"))
print(bool(12))

x="hi"
y=30
print(bool(x))
print(bool(y))

#the following will return false
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#the following also return false
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#functions can return a boolean
def myfunc():
    return True

print(myfunc())

def myfunc():
    return True
if myfunc():
    print("yes")
else:
    print("no")

#determine if an object is of a certain datatype
x=20
print(isinstance(x,int))

