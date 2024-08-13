l = [1,2,1,2,3,5,6,7] # 1
fre ={}
m = len(l)
for i in range(m):
    if l[i] in fre:
        fre[l[i]] += 1
    else:
        fre[l[i]] = 1
n = [(key,value) for key,value in fre.items()]
res = dict(n) # tuples to dictionary
print(res)

d =[1,2,1,2,3,5,6,7]
fre= {}
for i in range(len(d)):
    if d[i] in fre:
        fre[d[i]] +=1
    else:
        fre[d[i]] = 1
s = 'abvchAHGak' # 3
n = s.upper()
res = list(n)
print(res)
# 4) short tuple
T = (1,4,2,6,3)
sort = sorted(T)  #  sorted in list form
res = tuple(sort)
print(res)
# 5 ) vowels .conson..count
s = 'aeifAou102n3'
c = 0
v = 0
d = 0
for i in range(len(s)):
    if s[i] in ['a','e','i','o','u','A','E','I',"O",'U']:
        v +=1
    elif  s[i] >='A' and s[i]<='Z' or s[i]>='a' and s[i] <='z':
        c +=1
    else:
        d +=1
print(v)
print(c)
print(d)
# 6)
s = 'Anshkasmn'
q = 'ka'
d = ''
w = ''
for i in range(len(s)):
    if s[i] == 'k':
        d = s[i]
for i in range(len(s)):
    if s[i] =='a':
        w = s[i]
print(d+w,"yes present")
# 7)
S = [2, 3, 56, 8, 5]
K = 45

result = {}   # make dictionary to strore numbers

for i in S:
    result[i] = i + K

print(result)
# 8 )
s = input("Enter strng:")
print(s[::-1])
s = input("l")
l = s.split()
for i in range(len(l)):
    res = l[::-1]
print(" ".join(res))

# 10)
s = input("Enter the string:")
l = s.split() # spilt in list
for i in range(len(l)):
    print(l[i][::-1],end=" ")
# 10 )
t = (1,4,5,6,7,23,78)
k = 68
l =list(t)
l.append(k)
k = tuple(l)
print(k)
# 11)
T = (2,4,33,6,5,98,45)
l = list(T)  # list
l.append(68) # append
l.sort()
l.reverse()
d = tuple(l)
print(d)
# 12)
# 11)
T = (2,4,33,6,5,98,45)
l = list(T)  # list
l.append(68) # append
l.sort()
l.reverse()
d = tuple(l)
print(d)
#12)
d= {1:2,4:56,5:2,6:8,8:24}
ans = 0
for i in d.values():
    ans = ans +i
print("sum of keys ",ans)
# 13 )
d = {'Name':'Ram','Age':23}
add_keys = {'City':'salem'}
d = {'a':1,'b':2}
d.update({'d':4,'c':5})
print(d)
# 14)
d = {'b':24,'a':23,'n':56}
quarry = input("Enetr the key whose to be check")
if quarry in d.keys():
    print("yes",quarry,"is found")
else:
    print("not found")
# 15 )
d = {'a':23,'v':35,'d':67,'f':46}
for i in d.keys():
    print(i,end= "")
#16)
l =[1,2,3,4,5,6,7]
l1 =[2,3,4,5,5,6,7]
not_common = set(l)^set(l1)  # ^ unique elememt
print(not_common)
# 1 )
