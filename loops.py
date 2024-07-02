# For loop
for (i) in range (1,7):
    print(i)

for o in range (1,7,2): # for skipping/gapping
    print(o)

for (n) in range (0,8,2): # for evenly skipping
    print(n)

for (h) in range (1,5):
    print("hellow world")

# for multiplication or making a table
n = 9
# n =int(input("Enter your number here:"))

for t in range (1,11):
    print(n,"x",t,"=",n*t)

# While loop
l = 0
while l <= 7:
    print(l)
    l +=1 # incrementing with assigning operator

j = 0
while j <=11:
    print("\n",j)
    j +=2

# for multiplication or making a table with while loop
q = 1
w = 7
# w =int(input("Enter your number here:"))


while q<=10:
    print(w,"x",q,"=",w*q)
    q+=2

# While true
# while True:
#     print("hello") # infinite loop

# while True:
#      num = int(input("enter a number here: "))
#     print(num)
#
#      stop = input("If you want to stop the program type 'yes': ")
#     if stop == 'yes':
#         break

# Nested loop
for k in range (1,5):
    for g in range (1,11):
        print(g, end="") # use end for one liner print
    print()

# for pattern problem solving
for a in range (1,6):
    for b in range (1, a+1):
        print(b, end=" ")
    print()

# for loop with conditional statments
for s in range (1,6):
    if s == 3:
        print("add this nasheed to favs")
    else:
        print(s)

for f in range (1,101):
    if f % 8 == 0 and f % 12 == 0:
        print(f)

m=1
while m<=10:
    if m == 4:
        print("add this to the inbox")
    else:
        print(m)
    m+=1

# Continue and break statement:
for ns in range (1,11):
    if ns == 7:
        continue # loop skips when the value comes 7
    else:
        print(ns)


for pp in range (1,11):
    if pp == 5:
        break # loop stops when the value reaches 4
    else:
        print(pp)