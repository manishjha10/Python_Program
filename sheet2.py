# 1)for voting
age = int(input("Enter the age:"))
if(age>=18):
    print("You are eligilble for vote:")
else:
    print("You are noy eligible for vote:")
# div by 7
num = int(input("Enter the number:"))
if num%7==0:
    print("num is divisible by 7")
else:
    print("Num is Not Divisible By 7:")
#2) check last digit is 4
num = int(input("Enter the number:"))
if num %10==4:
    print("num last digit is 4")
else:
    print("last digit is not 4:")
# 3) div by 3 and last digit is 4
num= int(input("Enter the number:"))
if(num%3==0 and num%10==4):
    print("DIv is 3 and Last digit is 4")
#4) divisible by 3 or 4
num = int(input("Enter the number:"))
if num%3 == 0 or num%10 == 4:
    print("NUM is div 3 and last digit is 4")
# 5)div by 5 and 11
num = int(input("Enter the number:"))
if num%5==0 and num%11==0:
    print("num is divisible by 5 and 11:")
#6) take 3 input user and  print greater in them :
a = int(input("enter the number a:"))
b = int(input("enter the num b"))
c = int(input("enter the number c:"))
if a>b and a>c :
    print("A is greater")
elif b>c:
    print(" B is greter")
else :
    print("C is greater:")
# 7)print triangle is acute or right angle or obtuse:
a = int(input("Enter the number:"))
b = int(input("Enter the number:"))
c = int(input("Enter the number:"))
if a==90 or b==90 or c==90:
    print("Triangle is Right triangle:")
elif a>90 or b >90 or c>90:
    print("Obtuse triangle:")
else:
    print("Acute triangle:")
#8) triable is valid or nor
a = int(input("Enter the number:"))
b= int(input("Enter the number:"))
c = int(input("Enter the number:"))
if a+b+c == 180:
    print("Triangle is valid:")
else :
    print("Triangle is not Valid :")
#  7 div ld =5
num =int(input("enter "))
if (num%7==0 or num%10==0):
    print("num is divisible by 7 and last digit is 5")
# 11 )
a,b,c,d,e =10,20,30,40,50
d = (a+b+b+d+e)//5
print("Average is :",d)
#13
a = int(input("enewte rthe number:"))
b = int (input("enete rthe number:"))
if (a>b):
    print(a)
else:
    print(b)
# 14)
a = int(input("eneter the number:"))
b = int(input("enete the number:"))
c= int(input("enete the number:"))
if a<b and a<c:
    print(a)
elif b<c:
    print(b)
else:
    print(c)
#15,12 10,9,
#15
num = int(input("Enter the number:"))
if (num <= 25):
    print("D")
if (25 <= num < 45):
    print("C")
if (45 <=num < 65):
    print("B")
if (65 < num < 85):
    print("A")
if num > 85:
    print("A+")
    #12
a= int(input("enter t a"))
b = int(input("enter t a"))
c= int(input("enter t a"))
d = a+b+c
if(d==180):
    print("Triangle is valid:")
else :
    print("Triangle is not valid:")
#10
num = int(input("Enter the nubers in between 1 to 7:"))
if 1>num<7:
    print("enter a valid day")
match num:
    case 1:
        print("Sunday:")
    case 2:
        print("MOnday:")
    case 3:
        print("tuesday:")
    case 4:
        print("wednesday:")
    case 5:
        print("thursday:")
    case 6:
        print("friday:")
    case 7:
        print("saturday:")
# 9
num = int(input("enter the number:"))
if num%4==0 and num%100:
    print("num i s year.")
else :
    print("num is not leap year:")