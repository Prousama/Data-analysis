phone = "Apple","Samsung","google","Redmi","Vivo"
print(phone[1:3])
print(phone[:3])
print(phone[::2])
print(phone[1::2])
print(phone[::-1])
print(phone[2::-1])

# With for loop
for i in phone:
    print(i)

# along with range and length loop
for a in range(len(phone)):
    print(phone[a])

# while loop
b = 0
while b<len(phone):
    print(phone[b])
    b +=1