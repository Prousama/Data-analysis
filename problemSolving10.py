#Program to find min and max in a set
num = {77,43,56,2,99}
max = max(num)
min = min(num)
print("The maximum value of this set is", max)
print("The minimum value of this set is", min)

# Program to find the common element in lists using sets
a = [1,2,3,5,7,9]
b = [2,7,4,6,8,10]
c = [2,3,7,10]
print(set(a)& set(b)& set(c))

# Program to find the difference between two sets
a = {1,2,3,5,7,9}
b = {2,7,4,6,8,10}
print(a.difference(b))

# Program to remove an element from the set
b = {2,7,4,6,8,10}
b.discard(10)
print(b)

# Program to check if a set is a subset of another set
a = {1,2,3,4,5}
b = {3,4,5}
print(b.issubset(a))
