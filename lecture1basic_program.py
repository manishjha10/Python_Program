print("Hello World")
num = int(input("Enter the number:"))
if(num%2==0):
    print("Even:")
else:
    print("ODD:")
num = int(input("Enter the number:"))
if(num>2):
    print(num)
else:
    print("Condition is not satisfied:")
num = int(input("Enter the number:"))
if num > 0: # there is no such requirnment to use parenthesis in written as if(num>0) , we simply wriitten if num > 5:
    print("+ve")
elif num == 0:
    print("0")
else:
    print("-ve")
# calculate circumference of a Circle
radius =int(input("Enter the Radius:"))
pi = 3.1428
Area = 2 * pi * radius
print(Area)
# callculate area of circle, rectangle, triangle
l = int(input("Enter the number:"))
breath= int(input("Enter the number:"))
a = print(l*breath)
radius= int(input("Enter the radius:")) # area of circle :
pi = 3.1428
area = pi * radius * radius
print(area)
base= int(input("Enter the base :")) # area of triangle :
height= int(input("Enter the number:"))
area  = 1/2 * base * height
print(area)
# use of end=" ", it is parameter  use for in same line ma lane ka lia
print("manish",end=" ")
print("age =20",end =" ")
print("Hello",end =" ")
# sum of N numbers
n = 6
s=0
while n>0:
    s = s +n
    n=n-1
print(s)
