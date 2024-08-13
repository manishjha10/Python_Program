# list compreshension  l = [i for i in range() condotion ]
# 1) even numbers in the list
arr = [1,2,3,4,5,6,7,8,9,10,11]
lst = [i for i in arr if i%2 == 0]
print("even Number list is:", lst)
# 2) odd numbers in the list
arr = [1,2,3,4,5,6,7,8,9,10,11]
lst = [i for i in arr if i%2 != 0]
print("odd number list is:",lst)
# 3) accept elements in list more than 4
name = ['manish','jha','saharukh','khan','mohammad','jafer','sameer']
with_morefour = [i for i in name if(len(i)>6)]
print(with_morefour)
# 4) accept items in the small r in the new list
name = ['manish','jha','saharukh','khan','mohammad','jafer','sameer']
include_with_name = [i for i in name if 'r' in i]
print(include_with_name)
# 5) count no repeat in list
arr = [5,4,[10,9],5,25]
target = 5
count = 0
for i in arr:
    if target == i:
       count += 1   # increment when condition is true
print(count)
# 6) sum of list print
arr = [1,2,3,4,5]
ans = 0
for i in arr:
    ans = ans + i   # in single number like 12345 print so (ans*10)+i
print(ans)
# 7) add numbers in list
arr = [1,2,3,4,5]
inc = 10
for i in  range(len(arr)):
    print(i)
#8) condition statement check in list
arr = [1,2,3,4,5,'jha']
if  'yes' in  arr:
     print('Yes:')
else:
    print('NO:')
l = [1,2,3,4,5]  # 9) copy() function
m=l.copy()   # copy function copy the matrix
print("copy",m)
l = [1,2,3,4,55]
m = l.reverse() # 10)reverse the matrix
print(l)
l =[-5,2,8,6,-10]
l.sort()   # 11) sort method arrange in asscending order matrix
print(l)
l = [1,2,5,-8,55,100]
m = l.count(5) # 12) count no . repetations in list  store than print
print(m)
l = [1,2,5,-8,55,100]
l.sort(reverse = True)# 13) reverse the list
print(l)
# concatination two list  with + operator
l = [1,5,6,9,8]
m = [5,8,3,6,4]
concat = l + m
print(concat)
# string with (*)
l = [1,2,3] # print 123 with two times
m = l*2
print(m)
# 1)adion of two elements in string
l =[1,2,3,4]
m =[4,5,6,8]
ans = []
for i in range(len(l)):
    ans.append(l[i]+m[i])
print(ans)
l =[1,2,3,4]
m =[4,5,6]
ans = []
for i in range(len(m)):# we taken len(l) gives an error l =4,m=3
    ans.append(l[i]+m[i])
print(ans)
# 1) revers ein list
l = [1,2,3,4]
print(l[::-1])
print(l[:-1])  # len(4)-1 => max-1(3-1)=> 2(0,1,2)index ans =1,2,3
# 2)
l=[1,7,6,10]
n = len(l)
for i in range(len(l)//2):
   l[i],l[n-i-1] = l[n-i-1],l[i] # swapping case to reverse the list
print(l)
