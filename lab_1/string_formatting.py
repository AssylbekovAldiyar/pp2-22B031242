price=50
txt="The price is {} dollar"
print(txt.format(price))    

price=49
txt="The price is {:.2f} dollars"
print(txt.format(price))

a=10
b=20
c=30
txt="I want to buy {} pencils,and {} ereasers,and pay {:.2f} dollars"
print(txt.format(a,b,c))

#Index numbers
a=10
b=20
c=30
txt="I want to buy {1} pencils,and {0} ereasers,and pay {2:.2f} dollars"
print(txt.format(a,b,c))

age=24
name="Lisa"
txt="Her name is {1},{1} is {0} years old"
print(txt.format(age,name))

#named indexes
myorder="My name is {a},I am {b} years old"
print(myorder.format(a="Adau",b={"19"}))
