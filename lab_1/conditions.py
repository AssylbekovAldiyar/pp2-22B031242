a = 33
b = 200
if b > a:
  print("b is greater than a")

  a=10
  b=20
  if b>a:
    print("b is greater than a")
  elif a>b:
    print("a is greater than b")

    a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

  #short hand if
  if a>b: print("a is greater than b ")

a=1
b=2
print("A") if b>a else print("B")

a=2
b=2
print("A") if a>b else print("=") if a==b else print("B")


a=2
b=1
b=3
if a>b and c>a:
    print("Both conditions are true")

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

  #Nested if
  x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#the pass statement
a=1
B=3
if b>a:
    pass

