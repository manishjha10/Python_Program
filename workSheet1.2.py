age=int(input("Enter voters age:"))  # 1
if age>=18:
    print("You can cast your vote!")
else :
    print("Sorry You are not eligible to vote!")
colour = str(input("Enter the colors :"))  # 2
if colour == 'green':
    print("Car is allowed to go")
elif colour == 'yellow' :
    print('Car has to wait')
elif colour =='red':
    print('Car has to Stop:')
else :
    print("unorganized signal ")
grade = str(input('Enter the grades of students:'))   # 3
if grade == 'A':
    print("Outstanding")
elif grade == 'B':
    print("Excellent:")
elif grade == 'c':
    print("Very Good:")
elif grade == 'D':
    print("Good")
elif grade == 'E':
    print("Satisfactory")
else :
    print('unorganized')
name = str(input("Enter the name of student:"))   # 4)
sub = int(input("Enter the marks for subject 1:"))
sub1 = int(input("Enter the marks for subject 2:"))
sub2 = int(input("Enter the marks for subject 3:"))
sub3 = int(input("Enter the marks for subject 4:"))
sub4 = int(input("Enter the marks for subject 5:"))
total_marks = sub + sub1 + sub2 + sub3 + sub4
percentage =  (total_marks/500)*100
print("Total marks",total_marks)
print("percentage",percentage)
# condition according to grade
if 0 < percentage <45 :
    print('fail')
elif 45<= percentage <60:
    print("pass")
elif 60 <= percentage <75 : # in between this so (<= and >)
    print("good")
elif 75 <= percentage <85:
    print("very good")
elif 85 <= percentage <100:
    print('excellent:')
else:
    print("Error:")
# x = "10"   # 5
# y = 5
# result = x + y
#print(result)   # error string not concate with integer
a =10
b=15
c=20
if a < b < c:# 1 cond. is true so age nhi chalega  c1 only
   print("Condition 1")  # 6
elif c > b > a:
     print("Condition 2")
else:
    print("Condition 3")
x = '56'  # 7 565656 ( three times return becoz x is string)
y = 3
z = x*y
print(z)
# 8) Give output as :59
x=56  # 56 as in integer form so we get desired output
y=3
z=x+y
print(z)
x='56'  # 9 string and integer (*) repeat the same string in multiply karega utine bar repeat kar dega
y=2
z=x*y
print(z)
# 10
for i in range(1500,2701):
    if i%7 == 0 and i % 5 == 0:
        print(i)
# 11) accept fahrenheit and calculate celsius :
fahrenheit = int(input("Enter temperature in fahrenheit"))
# convert fahrenheit into celsius using
celsius = (fahrenheit - 32)*(5/9)
print(format(celsius ,".0f"))
# convert celsius into fahrenheit
celsius = int(input("Enter temperature in celsius"))
fahrenheit = (9/5)*(celsius + 32)
print(format(fahrenheit,".0f"))
year = int(input("Enter the year:")) # 13
if year % 4 == 0 and year %100 != 0:
    print("Year is leap year:")
else :
    print("Year is not leap year:")
# WorkSheet 2
num = 10
print(type(num))
var = "Hello"      # 1
print(type(num))
print(type(5//2))  # integer  double modulus returns integer
print(type(5/2))  # float    # 3
a =3
b =1
print(a,b)
a, b = b, a
print(a, b)
# 2) indentation in python  # 5) do while not supported in python
# number = 5
# while number <= 5:  # infinite loop
#     if number < 5:
#         number+=1
#     print(number)
number = 0
while number <= 10:
    print("Number:",number)
    number += 1  #  8
for x in [0,1,2,3]:
    for y in [0,1,2,3,4]:  # 20
        print("*")
s = 0
for i in range(1,5): # 9
    s = s+i
print(s)
for letter in 'python':
    if letter == 'h':  # except h all are print
        continue
    print(letter)
l = [1,2,3,4,5]  # 11
s = 0
for i in l :
    if i %2 != 0:
        s = s+ i
print("sum of odd numbers in given array is:",s)
l = [1,2,4,5,8,10,45,89,86]
count = 0          # 12
n = len(l)
for i in range(len(l)):
    if i <= n :
        count +=1
print(count)
n=int(input("Enter the number:"))
fact =1            # 13
for i in range(n):
    fact = fact*n
    n = n-1
print("Factorial is",fact)  # 14
Str = 'mynamies'
for char in str:  # str(string)  not iterable but in this Str so 4 times print loop is working
    if char == "i":
        break
    elif char == "a":
        continue
    else:
        print("loop is working:")