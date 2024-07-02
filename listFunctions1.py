a = ["Ironman","Thor","Captain america","Hulk","Thor"]
print(a)
# Function to find the length of a list
print(len(a))
# Function to find the times of occurrence of an element
print(a.count("Thor"))
# Funtion to add an element to a list
a.append('Spiderman') # adds the value to end of a list
print(a)

# Funtion to add an element to a list at a specific location
a.insert(1,"Vision")
print(a)

# Function to remove an element from list
a.remove("Hulk")
print(a)

# Function to remove an element from list from a specific location
print(a.pop(1))
print(a)
