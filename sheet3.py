#  #1) 1 to N even numbere
n= int(input("enter num:"))
i=1
while i<=n:
    if i%2==0:
        print(i)
    i =i+1
# # 2) odd numbers
n= int(input("enter num:"))
i=1
while i <= n:
    print(i)
    i =i+2
# 3) factors of num
n= int(input("enter num:"))
i=1
while i<=n:
    if n%i==0:
        print(i)
    i =i+1
# 5)sum of all natural numbers
n = int(input("Enter  number:"))
s = 0
while n>0:
    s=s+n
    n=n-1
print(s)
# # 6) even numbers which divisible by 2
n = int(input("Enter the some numbers:"))
i = 1
s =0
while i<=n:
    if i%2 ==0:
        s =s + i
        print(i,end =" ")
    i =i+1
print("sum is",s)
# # 7) odd numbers in range 1 to n
n = int(input("Enter the numbers:"))
i = 1
s=0
while i <= n:
    if i%2 != 0:
        s = s+i
    i = i+1
print("sum of odds =",s)
# 10) palindron numbers
n = int(input('Enter the number:'))
c=n
s =0
d = 0
while n>0:
     d = n%10
     s = (s*10) +d
     n = n//10
if s == c:
    print('Numberis pallindrom:')
else :
    print("No is not pallindron:")
# 12)table
n = int(input("Enter teh number:"))
for i in range(10):
    print("3 X ", i+1,"=",(i+1)*n)
# 13) power find
a= int(input("Enter the number for base:: "))
b = int(input("Enter the number for power :"))
p = 1
for i in range(b):
    p = p*a
print(p)

# grade display acciording to percentile
num = int(input("num"))
if num >= 91 and num < 100:
    print("A+")
elif num >= 81 and num < 91:
    print("A")
elif num >= 71 and num < 81:
    print("B+")
elif num >= 61 and num < 71:
    print("B")
elif num >= 51 and num < 61:
    print("C")
elif num >= 41 and num < 51:
    print("F")
else:
    print("FAIL :")


