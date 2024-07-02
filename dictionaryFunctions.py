student = {"name":"john","class":"7th","rollno":22}

# Functions
a = student.get("name")
print(a)

b = student.items()
print(b) # prints the values in the form of tuple

c = student.keys()
print(c)

d = student.values()
print(d)

e = student.copy()
print(e)