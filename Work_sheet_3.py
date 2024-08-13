# 2
n = 5
a = 1
for i in range(1, n + 1):

    for j in range(1, i):
        print(a, end=" ")
        a = a + 1
    print(a)
s1 = "listen"
s2 = "silent"
ss1 = sorted(s1)
ss2 = sorted(s2)
if ss1 == ss2 :
    print("yes")
else:
    print("no")
a = [2,3,4,5,8,10,6]
b = 4
N = len(a)
if b not in a:
    print("-1")
else:
    c = 0
    for  i in range(N):
        if a[i] >b:
            c+=1
print(c)
a = 'ABCGAG'
count = 0
result = 0
n = len(a)
for i in range(n-1, -1, -1):
    if a[i] == 'A':
        count += 1
    if a[i] == 'G':
        result += count
print(result)
# best REverse logic ever
s ="Hello World ! Welcome to Python"
l=s.split()
for i in range(len(l)):
    print(l[i][::-1],end=" ")










