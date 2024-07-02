l1 = [10,20,30,40]
print(l1)

l2 = []
for i in l1:
    l2.append(i)
print(l2)

l3 = [a for a in l1]
print(l3)

l3 = [a for a in l1 if a >20]
print(l3)