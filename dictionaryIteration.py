student = {"name":"john","class":"7th","rollno":22}
print(student["class"])

# Iteration in dictionary
# Printing all the key names of dictionary
for x in student:
    print(x)

# Printing all the key values of dictionary
for x in student:
    print(student[x])

# using value funtion
for x in student.values():
    print(x)

# using items funtion for printing both
for x,y in student.items(): # "x" will keep the keys and "y" will keep the values
    print(x,":",y)
