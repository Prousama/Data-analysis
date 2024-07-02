# checking datatypes of variable
name = "umer"
age = 25
print(type(name))
print(type(age))

# Implicit conversion
a = 123
b = 1.23
c = a+b
print(c)
print(type(c))

# Explicit conversion
a = "123"
b = 1.23
a = int(a)
print("After conversion",type(a))
c = a+b
print(c)
print(type(c))