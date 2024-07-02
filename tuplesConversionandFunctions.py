# Converting tuple into list
a = ("OnePlus","Samsung","Vivo")
print(type(a))

a = list(a)
print(type(a))

# Adding one more element
a.append("Nokia")
print(a)

# Converting back to tuple
a = tuple(a)
print(a)

# Funtions
a = ("OnePlus","Samsung","Vivo")
print(a.count("Vivo"))
print(a.index("Samsung"))


