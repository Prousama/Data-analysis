# Take an input from the user as a string then reverse it
a = input("Enter anything here: ")
print(a[::-1]) # reverses the value

# Program to check if the string only contains digit
b = input("Enter anything here: ")
# print(b.isdigit()) # returns the value in boolean
c = b.isdigit()
if c == True:
    print("The value is only digit.")
else:
    print("The value is not only digit.")

# Program to check if the string is palindrome
d = input("Enter anything here: ")
rev = d[::-1]
if d == rev:
    print("The string is palindrome")
else:
    print("The string is not palindrome")

# Program to check the number of vowels in a string
e = input("Enter anything here: ")
vowels = 0
for i in e:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u": # Could be in capital letters as well
        vowels +=1
print("The number of times vowels occurring in a word or sentence is",vowels)

# Program to if every word in a string starts with the capital letter
f = input("Enter anything here: ")
print(f.istitle())

