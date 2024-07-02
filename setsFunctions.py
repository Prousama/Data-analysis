a = {"Ironman","Hulk","Captain america","spiderman"}

# Functions
a.add("Thor")
print(a)

a.pop() # pops random value
print(a)

a.remove("Hulk")
print(a)

a.discard("Thor") # works same as remove
print(a)

b = a.copy()
print(b)