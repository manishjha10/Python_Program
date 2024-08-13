# 1 by pythagorus theorem.
def square(num):
    return (num *num)
def pythagorus(num,y):
    return (square(num)+square(y))
ans  = pythagorus(3,4)
print(ans)


def pythagorus(a,b):# para
    square_a = a*a
    square_b = b*b
    return (square_a+square_b)# calling
ans  = pythagorus(3,4)# argu
print(ans)# str print
# # 2)
def square(num):
   ans = num*num
   print(ans)
square(8)

def su_m(x,y):  # Sum of numbers
    s=0
    for i in range(x,y+1):
        s+=i
    print(s)
su_m(1,26)# 1-25 (sum)
su_m(1,5)


def ma_x(x,y): # maximum of numbet
    if x>y :
        print('x is greater')
    else:
        print('y is greater')
ma_x(4,5)


def hello(s,g):  # f-String
    print(f"Hello {s}and your age is ,{g}")
hello("manish",22)

# # Area of circle
def area_of_Circle(radius):
    area = 3.14*(radius*radius)
    print('Area of Circle is ',area)
area_of_Circle(25)
#  #

def Demo():  # sum of odd numbers
    n = int(input("Enter the number:"))
    s = 0
    for i in range(1,n+1):
        if i%2 != 0:
            s =s +i
    print(s)

def factorial():  # factorial
    fact = 1
    num = int(input("enter the number"))
    for i in range(1,num+1):
        fact = fact*i
    print(fact)
factorial()


def facb(num):  # Facbonacci Series
    a = 1
    b = 1
    s = 0
    for i in range(1,num):
        s = a + b
        a = b
        b = s
    print(s)
facb(9)


#ci = (p*(1+r/t)**(t*n))- p
def CI(p,r,n,t):  # Ci
   t = 1
   return (p*(1+r/t)**(t*n))- p
ans = CI(10000,0.05,7,1)
print(format(ans,'.2f'))


# # square root find
def perfect_square_root(num):
    square_root = num ** 0.5
    if square_root.is_integer():
        return int(square_root)
    else:
        return -1
num = 64
ans = perfect_square_root(num) # calling
print("square root of",num,"is",ans)

# # square  root define
import math
def is_perfect_square(num):
    square_root = math.sqrt(num)
    return square_root.is_integer()

# num = int(input("Enter the number: "))

if is_perfect_square(num):
    print("The number is a perfect square.")
else:
    print("The number is not a perfect square.")

#16)filter even numbers:

def fun(a):
    if a % 2 == 0:
        return True
    else :
        return False
l = [1,2,3,4,5.0,6.3]
ans = list(filter(fun,l)) # filter(function , iterable(list,tuple,dictionary))
print(ans)

# # 17 ) filter even odd using lambda funtion
l =[1,2,3,4,5,6,7,8]
ans = list(filter(lambda x:x%2 == 0,l))
print(ans)

# 18) filter number greater than 60
l=[45,65,69,89,10,12,1,3,14,1,5,60,63]
ans = list(filter(lambda x : x > 60,l))
print(ans)
18 ) 2) add 10  to each element of a list using map and lambda function
arr = [1,2,3]
ans =  list(map(lambda x : 10 +x,arr))
print(ans)

# 19 ) convert number to lowercase using map lambda function
# names = ["APPLE","BANANA","LEMON",'PAPAYA',"MANGO"]
# ans = list(map(lambda X: X.lower(),names))
# print(ans)

# 20) python program using map,filter and lambda Functions
# l = [1,2,3,4,5,6]
# ans =  list(map(lambda x:x*x,l))
# special_num = 2
# result =  list(filter(lambda x : x% special_num ==0,ans))
# print(result) # 4,16,36

# fabonacci series using recursion method
def fabonacci(n):
    if n<=1 :
        return n
    else:
        return fabonacci(n-1) + fabonacci(n-2)
def print_fabonacci_series(count):
    if count <=0:
        print("enter a positive number")
    else:
        print("fabonacci series")
        for i in range(count):
            print(fabonacci(i),end= " ") # calling (2)

num_terms = 10
print_fabonacci_series(num_terms) # calling (1)









