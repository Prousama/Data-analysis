# # Iteration using for loop
a = ["Ironman","Thor","Captain america","Hulk"]
for b in a:
    print(b)

# Iteration using for loop and length function
for c in range(len(a)):
    print(a[c])

# Iteration using while loop:
d = 0
while d < len(a):
    print(a[d])
    d +=1

# Using short hand for loop:
[print(e) for e in a]
