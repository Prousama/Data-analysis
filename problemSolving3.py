# Program to find the sum of even numbers up to 50
sum = 0
for i in range (1,51):
    if i % 2 == 0:
        sum += i
print("The sum of the even numbers up to 50 is",sum)

# Program to write first number and their squared values
for a in range (1,21):
    print(a, a**2)

# Program to find the sum of first 10 odd numbers using while loop
sum = 0
b = 0
while b <=20:
    if b % 2 != 0:
        sum += b
    b += 1
print("The sum of first 10 odd numbers is",sum)

# Program to check a number is divisible by 8 and 12, until 100 number
for c in range (1,101):
    if c % 8 == 0 and c % 12 == 0:
        print(c)

# Program to create a billing system for supermarket
while True:
    name = input("Enter your name here: ")
    total = 0
    while True:
        print("Enter the amount and quantity")
        amount = float(input("Enter the amount: "))
        quantity = float(input("Enter the quantity: "))
        total += amount*quantity
        repeat = input("Do you want to add more items? (yes/no): ")
        if repeat == "no" or repeat == "No":
            break
    print("-"*40)
    print("Name:",name)
    print("Total:",total)
    print("-"*40)
    print("*****Happy Shopping*****")
    repeat1 = input("Do you want add any other customer details? (yes/no): ")
    if repeat1 == "no" or repeat1 == "No":
        break
