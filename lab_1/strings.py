#strings
print("Hello")
print('Hello')

#assign string to a variable
a = "Hello"
print(a)

#multiline strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#strings are arrays
a = "Hello, World!"
print(a[1])

#loopint through a string
for x in "banana":
  print(x)

  #string length
  a = "Hello, World!"
print(len(a))

#check string
txt="The best thing"
print("best" in txt)

txt="The best thing"
if "best" in txt:
    print("Yes,'best' in present")

#check if not
txt="The best thing"
print("good" not in txt)

txt="How are you"
if "good" not in txt:
    print("No,'good' is NOT present")

    #slicing strings
    b="Hello,world!"
    print(b[2:5])

    b="Hello,world!"
    print(b[:5])

    b="Hello,world!"
    print(b[2:])

    b="Hello,world!"
    print(b[-5:-2])

    #Modify strings
    #upper case
    a="Hello,world!"
    print(a.upper())

    #lower case
    a="Hello,world!"
    print(a.lower())

    #Remove whitespace
    a="Hello,world!  "
    print(a.strip())

    #Replace string
    a="Hello,world!"
    print(a.replace("H","J"))

    #split string
    a="Hello,world!"
    print(a.split(","))

    #string concatenation
    a="Hello"
    b="World"
    c=a+b
    print(c)

    a="Hello"
    b="World"
    c=a+" "+b
    print(c)

    #format strings
    age=36
    txt = "My name is John, and I am {}"
    print(txt.format(age))

    quantity = 3
    itemno = 567
    price = 49.95
    myorder="I want to pay {2} dollars for {0} pieces of item {1}."
    print(myorder.format(quantity, itemno, price))
    

