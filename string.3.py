# Strings are immutable (We cannot change the String)
a = "!!!Harry!! !!!!!!!!! Harry!!!!"
print(len(a))
print(a)
print(a.upper())  # is used for boolean true or false isupper
print(a.lower())
print(a.rstrip("!"))# remove right side!!
print(a.lstrip("!"))  # remove left side !!
print(a.replace("Harry", "John"))   # repleace(old,new)
print(a.split(" ")) # split (whital spaces par , a ajega )
blogHeading = "introduction tO jS"
print(blogHeading.capitalize()) # first letter capitale

str1 = "Welcome to the Console!!!"
print(len(str1.center(50)))  # len only find string ke ont find int
print(a.count("Harry"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))

str1 = "He's name is Dan. He is an honest man."
print(str1.find("ishh"))
# print(str1.index("ishh"))
print(str1.index("D"))

str1 = "WelcomeToTheConsole"
print(str1.isalnum())
str1 = "Welcome"
print(str1.isalpha())

str1 = "hello world"
print(str1.islower())

str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable())
str1 = "         "       #using Spacebar
print(str1.isspace())
str2 = "  "       #using Tab
print(str2.isspace())

str1 = "World Health Organization"
print(str1.istitle())  # in letter first Word is capital

str2 = "To kill a Mocking bird"
print(str2.istitle())

str1 = "Python is a Interpreted Language"
print(str1.startswith("Python"))

str1 = "Python is a Interpreted Language"
print(str1.swapcase())

str1 = "His name is Dan. Dan is an honest man."
print(str1.title()) # in letter first word is capital