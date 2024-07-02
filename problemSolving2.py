# checking the value of a variable if it is positive or not
num = int(input("Enter the number: "))
if num >0:
    print("it is positive")

# checking whether the number is even or odd
num = int(input("Enter the number: "))
if num % 2 == 0:
    print("This is even")
else:
    print("This is odd")

# creating area calculator
print("*****AREA CALCULATOR*****")
print("""Type 1 to get the area of square
Type 2 to get the area of rectangle
Type 3 to get the area of circle
Type 4 to get the area of triangle""")

type =int(input("Enter the number between 1 to 4: "))
if type == 1:
    side = float(input("Enter the length of one side: "))
    area = side**2 #side*sid
    print("The area of square is", area)

elif type == 2:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length*width
    print("The area of rectangle is", area)

elif type == 3:
    radius = float(input("Enter the radius of circle: "))
    area = ((3.14)*(radius**2))
    print("The area of circle is", area)

elif type == 4:
    base = float(input("Enter the base of triangle: "))
    height = float(input("Enter the height of triangle: "))
    area = 0.5*base*height
    print("The area of rectangle is", area)

else:
    print("Invalid input")

# checking whether a letter is vowel or not
letter = str(input("Enter the letter: "))
if letter in "aeiou" or letter in "AEIOU":
    print("This is vowel")
else:
    print("This is not a vowel")

# checking if the number is a single digit number, double digits number or so on...
num = int(input("Enter the number up to 5 digits: "))
if num >=0 and num <=9:
    print("This is single digit number")
elif num>=10 and num <=99:
    print("This is double digits number")
elif num >=100 and num <=999:
    print("This is triple digits number")
elif num >=1000 and num <=9999:
    print("This is four digits number")
else:
    print("This is five digits number")











