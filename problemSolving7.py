names = ['osama','owais','abdullah','adeel']

# Program to swap elements position
names[0],names[3] = names[3],names[0]
print(names)

# Program to add an element on the second position
names.insert(1,"umer")
print(names)

# Program to delete an element on the third position
names.pop(2)
print(names)

num = [13,7,12,10]

# Program to multiply all the elements
mul = 1
for a in (num):
    mul*=a
print(mul)

# Program to find the largest number from the list
num.sort()
print(num)
print("The largest number is",num[-1])

# Program to find the smallest number from the list
print("The smallest number is",num[0])

