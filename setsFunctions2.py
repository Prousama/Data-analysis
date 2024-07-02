a = {"Ironman","Hulk","Captain america","spiderman"}
b = {"Superman","Batman","Wonder-woman"}
c = {"Hulk","spiderman","Thor"}

print(a.isdisjoint(b)) # Check if the sets have any same value or not

print(c.issubset(a)) # check if the given set variable in the function contains any same value

print(a.issuperset(c))

a.update(c)
print(a)

a.clear()
print(a)
