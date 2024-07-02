a = "hello"
b = "123hello"
c = "123456"
d = "HELLO"
e = " "
f = "Hello 123"
g = "1.234"
h = "The Harry Potter"

#isalnum() - returns 'True' if the value in string is alphanumeric
print(a,a.isalnum())
print(b,b.isalnum())
print(f,f.isalnum()) # False because of space in between
print(g,g.isalnum()) # False because of decimal

#isalpha() - returns 'True' if the value in string is alphabetic
print(a,a.isalpha())
print(b,b.isalpha())

#isdecimal() - returns 'True' if the value in string is in decimal
print(a,a.isdecimal())
print(g,g.isdecimal()) # False because the decimal is inside the strings
print(c,c.isdecimal())

#isdigit() - returns 'True' if the value in string are digits
print(b,b.isdigit())
print(c,c.isdigit())
print(g,g.isdigit())

#isnumeric() - returns 'True' if the value in string are numeric
print(a,a.isnumeric())
print(b,b.isnumeric())
print(g,g.isnumeric())

#islower() - check if the value of string is in lower case or not
print(a, a.islower())
print(d, d.islower())

#isupper() - check if the value of string is in upper case or not
print(a, a.isupper())
print(d,d.isupper())

#isspace() - check if the all value of string is of whitespaces
print(e, e.isspace())
print(f, f.isspace())

#istitle() - return 'True' if the string follows the title rules
print(d,d.istitle())
print(h,h.istitle())
print(f,f.istitle())



