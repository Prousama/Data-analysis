a = "Shahrukh Khan"

#endswith() - returns True if the string ends with the given value
print(a.endswith("n"))
print(a.endswith("a"))
print(a.endswith("h",0,8))

#startswith() - returns True if the string starts with the given value
print(a.startswith("s"))

#swapcase() - lower cases becomes upper case and vice versa
print(a.swapcase())

#strip() - removes the whitespaces from the value of string
b = "  lionel messi   "
print(b)
print(b.strip())

c = "***** Neymar Jr ....."
print(c.strip("*, "))

#split() - splits the string at the specified separator, and returns a list
emails = "osama@gmail.com, adeel@gmail.com, owais@gmail.com"
print(emails.split(","))

#ljust - returns a left justified version of the string
movie = "Intestaller"
# fav = movie.ljust(20)
fav = movie.ljust(20,"*")
print(fav, "is my fav movie.")

#rjust - returns a right justified version of the string
book = "48 powers of law"
fav1 = book.rjust(25) #consider the value of variable as well in the number
print(fav1, "is my fav book")

#replace - returns a string where a specified value is replaced variable specified value
about = "my name is osama. osama likes to play circket"
print(about)
print(about.replace("osama",'owais'))

#rindex - searches the string for a specified value and returns the last position of where it was found
mov = "Kabhi khushi kabhi gum"
print(mov.rindex("gum"))
print(mov.rindex("Kabhi"))

#rfind - searches the string for a specified value and returns the last position of where it was found
mov1 = "Kabhi khushi kabhi gum"
print(mov1.rindex("kabhi"))
print(mov1.rindex("hi", 12,30))



