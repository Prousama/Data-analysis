a = {"Ironman","Hulk","Captain america","spiderman"}
b = {"Superman","Batman","Wonder-woman"}
c = {"Hulk","spiderman","Thor"}

print(a.union(c))

print(a.difference(c)) # makes a new set with the value which is not same in the "a" set.

a.difference_update(c) # make changes in the existing set of "a".
print(a)

print(a.intersection(c)) # makes a new set with the value which is same in the "a" set.

a.intersection_update(c) # make changes in the existing set of "a".
print(a)

x = a.symmetric_difference(c) # removes the common element from the set and provides a new set.
print(x)

a.symmetric_difference_update(c) # removes the common element from the original set.
print(a)

