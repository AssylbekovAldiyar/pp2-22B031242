x=5
y="Adau"
print(y)

x=4
print(x)

k=str(3)
y=int(3)
z=float(3)
print(k)
print(y)
print(z)

x=5
x="Adau"
print(type(x))
print(type(y))

a=4
A="Sally"
print(a)
print(A)

#variable names
myVariableName = "John"
MyVariableName = "John"
my_variable_name = "Jo"

#Assign Multiple Values
x=="Orange",y=="Banana",z=="Cherry"
print(x)
print(y)
print(z)

x=y=z="Orange"
print(x)
print(y)
print(z)

fruits=["apple","banana","cherry"]
x,y,z=fruits
print(x)
print(y)
print(z)

#output variables
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#Global Variables
x="someone"
def myfunc():
    print("Python is " + x)

myfunc()

x="awesome"
def myfunc():
    x="fantastic"
    print("python is "+ x)

myfunc()

print("python is "+ x)

x="awesome"

def myfunc():
    global x
    x="fantastic"

myfunc()

print("python is "+x)
    