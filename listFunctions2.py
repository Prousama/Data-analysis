a = ["Ironman","Thor","Captain america","Hulk","Thor"]
# Function to create a copy of list
b = []
print(b)
b = a.copy()
print(b)

# Function to access index of an element
print(a.index("Hulk"))

#Function to extend a list
c = ['Spiderman','Vision']
a.extend(c)
print(a)

#Function to reverse the value of list
a.reverse()
print(a)

#Function to sort a list ascendingly
a.sort()  # also works with the number values
print(a)

#Function to clear a list
a.clear()
print(a)


