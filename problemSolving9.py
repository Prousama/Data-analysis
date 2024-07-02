# python program to sort a dictionary by values
a = {"a":22,"b":12,"c":7,"d":10,"e":77}
a = sorted(a.values())
print(a)

# python script to print a dictionary where the keys are numbers between 1 and 15 and values are square of the keys
b = {}
for c in range (1,16): # "c" keeps the keys
    b[c] = c**2 # these are the values
print(b)

# Program to multiply all the items in the dictionary
d = {"a":1,"b":2,"c":3,"d":4,"e":5}
product = 1
for e in d:
    product *= d[e] # fetch all the items for dict
print(product)

# python program to sort a dictionary by keys
f = {"c":22,"e":12,"a":7,"d":10,"b":77}
f = sorted(f.keys())
print(f)


