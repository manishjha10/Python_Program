# function def --
#1 )write a prm to find a factorial using functions
# def fact():  # function
#     n = 5
#     fact = 1
#     i = 1
#     while n > 0:
#         fact =fact *i
#         n = n-1
#         i += 1
#     print(fact)
# fact() #function calling
# # 2)  prime num:
# def prime_num():
#     count = 0
#     num = int(input("Enter the number:"))
#     for i in range(1,num+1):
#         if num%i == 0:
#             count+=1
#     if count == 2:
#         print('prime')
#     else:
#         print('not prime')
# prime_num()
# def sum():  # define function
#     a = eval(input("enter 1:"))
#     b = eval(input('enter num 2:'))
#     sum = a+b
#     print(sum)
# sum()# calling function
# 4 ) geometric mean
def calculate(a,b): # define calculate
    mean = (a*b)/(a+b)
    print(mean)
def isgreater(a,b):  # Define greater
    if a >b:
        print("a is greater")
    else:
        print("b is greater")
def islower(a,b):  # define lower
    if a<b:
        print("a is lesser:")
    else:
        print("b is  lesser:")
def sum_num(a,b):
    pass # no error generate without pass error generate.

# one We Define the function and Calling Multiple Times
# pass => No Error Generate. It use when We Define the code  After Some Time.
a = 5
b = 10
calculate(a,b)# calling
isgreater(a,b)
islower(a,b)
c = 25
d = 30
calculate(c,d)  #calling
isgreater(c,d)
islower(c,d)

# Functions Arguments.
# 1) Default Arguments. => in this default value is run example
def average(a=10,b=2):
    print("Average is=",(a+b)/2)
average()# 6.0
average(5) # default a = 5 , b=2 (average)
average(5,3) # a= 5,b =3 (average)
# 2) Keyword Arguments. => order no matter:
def average(a=2,b=7):
    print("average is ",(a+b)/2)
average(a=3,b=6)# 4.5
average(b=5,a=1) # no matter whatever first
average(b=5)# a= 1,b=5 (average)
average(a=2) # a=2,b=7(average) 4.5
# 3 )Required Argument.
def average(a,b=2):
    print('average',(a+b)/2)
average(a=1)# b default value

def average(a,b,c=5):
    print('average',(a+b)/2)
average(2,3)
def average(*numbers):  # As a Tuple form ma aega
    # print(type(numbers))
    s = 0

    for i in numbers:
        s = s + i
        print('average', s / len(numbers))


average(1, 4, 5, 7, 9)


def name(**name):  # nam eas a dictionary
    print(type(name))
    print('Hello', name['fname'], name['mname'], name['lname'])


name(mname='Buchuman', lname='Barnes', fname='james')
# return Function is used to return the expression
def average(*numbers):
    s = 0
    for i in numbers:
        s = s+i
        return s/len(numbers)
c = average(5,6,7)
print(c)
# questions basic

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
# factorial progrem
def factorial(num):
    fact = 1

    while num >0:
        fact = fact * num
        num = num - 1
    print(fact)
factorial(5)
# keyword argument
def display_function(name,age):
    print("name = ",name, "age= ",age)
display_function(name = 'manish',age = 22)# calling
def square(num):  # 1)
    ans = num * num
    print(ans)
square(5)

def square_number(x,y):
    ans = 1
    for i in range(x,y+1):
        ans = ans *i
    print(ans)
square_number(3,16)


def f(n):  # fabonacci with recursion
    if n <= 1:
        return 1
    return f(n - 1) + f(n - 2)  # function call itself


n = 5  # indexing start from 0
ans = f(n)
print(ans)
for i in range(1, n + 1):  # series
    print(f(i), end=" ")


