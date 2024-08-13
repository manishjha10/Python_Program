 # formatting is used for exampe 23.22455 this number is two decimal places tak chhea  use formattting
 # syntax of formatting is:  format(item,format_specifier) ,item is :(number or string),(format_specifier)is: that specifies how item is formatted
 # Make  use of format() function and display the area of triangle


radius = int(input("enter radius:"))
pi = 3.1428
area = pi * radius  * radius
print("Area of circle is:",format(area,".2f"))
#formatting string point number
print(format(10.3456,"10.2%")) # space create hojaega left ma 10 blocks hoga total including with space(10 blok hoga)
print(format(10,"10.2f"))
print(format(10.3245,"10.2f"))

# inter formatting
print(format(20,"10x")) # inter to hexa decimal format (>10.2f)
print(format(20,"<10x"))

# formatting string
print(format("Hello World!","25s"))# left justificationka example
print(format("Hello World!",">25"))# right justification ka example

# 10.2f => format floatting point number with precious 2 and width 10
# <10.2f => left justify the floating point number
# >10.2f => right justify the formatting item
# 10X = > format integer in hexa decimal with width 10
# 20s = > format string with width 20
#  10.2f = > format the number in decimal