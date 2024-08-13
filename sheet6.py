# t = int(input("Eneter the num:"))  #
# for i in range(0,t):
#     count = 0
#     vow = 0
#     inp = input().lower()
#     for i in inp:
#           if i == 'a' or i == 'e' or i == 'o' or i =='i' or i == 'u':
#                vow+=1
#           else :
#                count+= 1
#     print(count)
#     print(vow)
# l  = [1,2,10,20,5,3,10,20,3,1,2]  # 2
# u =[]
# for i in l:
#     if l.count(i) == 1:
#         u.append(i)  # list form
# print(i)
#  # 2
# s = " python"
# n = len(s)
# print(l)
# 3 )
# t = int(input("enter the number:"))
# for i in range(0,t):
#     s = input()
#     rev = s[::-1]
#     result =  rev.lower()
# if s == result :
#     print("1")
# else:
#     print("0")
# # 4
# A="**h*e*l*lo"
# print(A.strip())
# print(A.lstrip())
# print(A.rstrip())
# # 7
# s = "manish "
# l = s.split()
# rev = l.reverse()
# result = " ".join(rev)
# print(result)
# 10)
s = "manish jha"
l = s.split()
for i in range(len(l)):
    rev = l[::-1]
print(" ".join(rev))

# s = 'PythoN'
# s.lower()
# print(s)
# s = 'PythoN'
# s.upper()
# print(s)
# s = "pYthON"
# s.isalnum()  # for alphabets chaeck return boolean
# print(s)
# 13

# s = "python"
# s.isalpha()
# print(s)
# # 14)

# A = "aabbcc"
# B = 98
# c = chr(B)
# count = 0
# for i in range(len(A)):
#     if A[i] == c :
#         count+=1
# print(count)
# # pallindrom
# s = str(input("Enter string"))
# rev = s[::-1].lower()
# result = "".join(rev)
# if result == s :
#     print("1")
# else:
#     print("0")
# 16)  count occurence
a = input()
n = len(a)
c = 0
for i in range(n-2):
    if a[i] == 'b' and a[i+1] == 'o' and a[i+2] == 'b' :
        c+=1
print(c)
# 15) first occurence of word

a = input()
b = input()
if b not in a:
    print("-1")
else:
    x = a.find(b)
    print(x)
# 14 )
a = "aabbcc"
b = 98
count=1
c = chr(b)
if c in a:
    count=count+1
print(count)

#   9)
# Define the original string
s = "manish jha"

# Split the string into two parts based on the space
parts = s.split()

# Initialize empty strings to store the reversed substrings
reversed_part1 = ""
reversed_part2 = ""

# Reverse the first part
for i in parts[0]:  # it refers the  part[0] -> manish
    reversed_part1 = i + reversed_part1

# Reverse the second part
for i in parts[1]:  # it refers the  part[1] -> jha
    reversed_part2 = i + reversed_part2
    print(reversed_part2)
# Concatenate the reversed substrings with a space in between
reversed_string = reversed_part1 + " " + reversed_part2

# Print the reversed string
print("The reversed string is:", reversed_string)

# 17) string opretaion

a = input()
a = a+a  # concatination
res = ""
n = len(a)
for i in range(n):
    if a[i] >= "A" and a[i] <= "Z" :
        continue
    elif a[i] in ['a','e','i','o','u']:
        res+="#"
    else:
        res+=a[i]
print(res)


# 9 ) revers the string
st = "Welcome To Console"
li = s.split()  # list convert
nli =[]
for i in range(len(li)):
    nli.append(li[i][::-1])    # list i  element reverse
print(" ".join(nli)) # sting convert
s = "My name is"  # 9
l = s.split()  # list convert
res =[]   # empty lidt createv
for i in range(len(s)):
    res =l[::-1]
print(" ".join(res))
s  = "My name is Tonny"   # 10)
r = s.split() # list convert
l =[]
for i in range(len(r)):
   l.append(r[i][::-1])
print(" ".join(l))
# 11)
T = (2,4,33,6,5,98,45)
l = list(T) # tuple to list
so = sorted(l)  # sorted list
so.reverse() # reverse list
res = tuple(so)  # reverse list convert tuple
print(res)
D = {1: 2, 4: 56, 5: 2, 6: 8, 8: 24}  # 12)

total_sum = sum(D.values())

print(total_sum)
# 9) Best Reverse Logic Ever
s ="Hello World ! Welcome to Python"
l=s.split()
for i in range(len(l)):
    print(l[i][::-1],end=" ")

n = len(l)
print(n)

# 14 )
A = "aabbcc"
B = 98
d = chr(B)
print(A.find(d))
# 15 )
A = "aabababaa"
B = "ba"
if B in A :
    print(A.find(B))
# find find no of times  character present in the string



