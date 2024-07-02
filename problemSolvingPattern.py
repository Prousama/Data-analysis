for a in range (1,6): #rows
    for b in range (1, a+1): #columns
        print(b, end=" ")
    print()

for a in range (1,6):
    for b in range (1, a+1):
        print("*", end=" ")
    print()

for c in range (1,6):
    for d in range (1, c+1):
        print(c, end=" ")
    print()

for e in range (1,6):
    for f in range (6,e,-1):
        print(e, end=" ")
    print()

for g in range (1,6):
    for h in range (5,g,-1):
        print(" ", end=" ")
    for i in range (g):
        print("*", end=" ")
    print()

for j in range (1,6):
    for k in range (j,0,-1):
        print(k, end=" ")
    print()

for l in range (1,6):
    for m in range (1,l+1):
        print("*", end=" ")
    print()
for n in range (5, 0, -1):
    for o in range (0, n-1):
        print("*", end=" ")
    print()

for p in range (1,11):
    for q in range (1,p+1):
        print(p*q, end=" ")
    print()