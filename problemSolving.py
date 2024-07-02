# swapping variables values
x = 12
y = 13

temp = x
print(temp)
x = y
print(x)
y = temp
print(y)

print("The value of x is",x)
print("The value of y is",y)

# method 2
a = 30
b = 20

a,b = b,a
print(b)
print(a)

# type-casting float into integer
a = 12.7
a = int(a)
print(type(a))
print(a)