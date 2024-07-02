# Fibonacci numbers
a = 0
b = 1
print(a)
print(b)
for i in range (2,11):
    c = a+b
    a = b
    b = c
    print(c)

a = 0
b = 1
n = int(input("enter the number here: "))
if n == 1:
    print(1)
else:
    print(a)
    print(b)
    for i in range (2,n):
        c = a+b
        a = b
        b = c
        print(c)

# If a number is prime or not
num = int(input("Enter a number here: "))
if num <=1:
    print("It is not a prime number")
else:
    for i in range (2,num):
        if num % i == 0:
            print("It is not a prime number")
            break
    else:
        print("It is a prime number")


# If a number is palindrome or not
num = int(input("Enter a number here: "))
temp = num
rev = 0
while num>0:
    dig = num % 10
    rev = rev*10 + dig
    num = num//10
if rev == temp:
    print("It is palindrome")
else:
    print("It is not palindrome")


# creating area calculator
print("*****AREA CALCULATOR*****")
while True:
    print("""Type 1 to get the area of square
    Type 2 to get the area of rectangle
    Type 3 to get the area of circle
    Type 4 to get the area of triangle""")

    type =int(input("Enter the number between 1 to 4: "))

    if type == 1:
        while True:
            side = float(input("Enter the length of one side: "))
            area = side**2 #side*sid
            print("The area of square is", area)
            repeat = input("Do you want to calculate the area of square again? ")
            if repeat == "no":
                break

    elif type == 2:
        while True:
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            area = length*width
            print("The area of rectangle is", area)
            repeat = input("Do you want to calculate the area of rectangle again? ")
            if repeat == "no":
                break

    elif type == 3:
        while True:
            radius = float(input("Enter the radius of circle: "))
            area = ((3.14)*(radius**2))
            print("The area of circle is", area)
            repeat = input("Do you want to calculate the area of circle again? ")
            if repeat == "no":
                break

    elif type == 4:
        while True:
            base = float(input("Enter the base of triangle: "))
            height = float(input("Enter the height of triangle: "))
            area = 0.5*base*height
            print("The area of rectangle is", area)
            repeat = input("Do you want to calculate the area of triangle again? ")
            if repeat == "no":
                break

    repeat1 = input("Do you want to repeat the menu again? ")
    if repeat1 == "no":
        break

