l = [] # empty list create  ,enter the list in user input
n = int(input("Enter the elements in list:"))
for i in range(1,n+1):
    ele = int(input("Enter no:"))
    l.append(ele)  # ele ma appent in l list
print(l)
arr = [1,2,3,4,5]  # 1
ans = 0
for i in arr:
    ans = ans + i   # in single number like 12345 print so (ans*10)+i
print(ans)
l=[1,7,6,10] # 10
n = len(l)
for i in range(len(l)//2):
   l[i],l[n-i-1] = l[n-i-1],l[i] # swapping case to reverse the list
print(l)
a=[1,2,3,2,1]
b=3
ans =[]          # 2
for i in a:
    ans.append(i+b)
print(ans)
n = [1,5,9,1]
ans = -float("infinity")    # 3 max
for i in n:
    if ans<i:
        ans = i
print("max",ans)
n = [1,5,9,1]
ans = +float("infinity")   # 3  min
for i in n:
    if ans>i:
        ans = i
print("min",ans)
4, 5
a = [1, 9, 5, 8, 5]  # 4
target = 5
counter = 0
for i in range(len(a)):
    if a[i] == target:
        print("Index number is  ", i)
        counter += 1
print("no of times repeat in list is,", counter)
A = [1, -5, 2, -8, -4]
ans = []
for i in range(len(A)):  # 5
    if A[i] < 0:
        print(A[i])
# find the difference of even and odd   in array 6)
a = [1, 2, 3, 4]
even_count = 0
odd_count = 0
for i in range(len(a)):
    if a[i] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
# to find the absoulte Difference Even And Odd
Absolute_Difference = (even_count - odd_count)
print(Absolute_Difference)

l=[1,2,3,4,5]# 7 even
ans = []
for i in range(len(l)):
    if l[i]% 2 == 0:
        ans.append(l[i])
print(ans)
l=[1,2,3,4,5]# 7 odd
ans = []
for i in range(len(l)):
    if l[i]% 2 != 0:
        ans.append(l[i])
print(ans)

a= [2,4,6,8]
ans =[]             #8
for i in a:
    ans.append(i*i)
print(ans)
a= [2,4,6,8]
ans =[]
for i in a:
    ans.append(i*i*i)       # 9
print(ans)
# a=[1,2,3,4]
# b=[5,6,7,8]
# ans =[]           #     11
# for i in range(len(a)):
#     ans = a[i]+b[i]
# print(ans)
l =[2,4,6,8,10,12,14,16,18,20]
print(l[:])
print(l[::])
print(l[2:5])
print(l[2:])
print(l[2::])
print(l[:2])
print(l[::2])
print(l[1::2])
print(l[2:10:2])
l=[1,3,5,7,9,11,13,15,17,19,21]
print(len(l))
print(l[-2:-5:-1])
print(l[-2:])
print(l[-2::])
print(l[-2:])
print(l[::-2])
print(l[::-1])
mylist =[1,4,2,3,4,5,'suyash']
mylist.reverse()
print(mylist)
s = "Hello everyone how are you"
print(s.split())
s = "Hello everyone-how are you"
print(s.split("-"))
word = 'suyash:chaudhary:Noida'
print(word.split(':'))
t= "23456"
print(t.split())
t = "2 3 4 5"
print(t.split())
l1 = [1,2,3,5,8,9]
l2 = [3,4,5,6,7,10]
result = l1 +l2
print(result)
result1 = l1 *3
print(result1)
#  1) given an array of integer a every element in repeated twice exect 1 find that uniqe number
l  = [1,2,10,20,5,3,10,20,3,1,2]
u =[]
for i in l:
    if l.count(i) == 1:
        u = i
print(u)
# 5 )
A = [1 ,-5, 2 ,-8 ,-4]
l = []
for i in range(len(A)):
    if A[i] > 0:
        continue
    elif A[i] < 0:
        l.append(A[i])
        re=A[i]
        print(re)









