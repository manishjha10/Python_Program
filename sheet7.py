# dictionary works on KEY :VALUE
# make pallindrom rearrange the characters
# all conditions are satisfies this pallindrom. 3)
s = input().lower()
fre = {}  #empyt dictionary
for i in s:
    if i in fre:
        fre[i] += 1
    else :
        fre[i] =1
odd = 0  # check for odd conditons
for i in fre.values(): # targeted in fre values
    if i%2 != 0:    # if fre valus -> odd inc
        odd+=1
if odd <= 1: # odd less or equal to 1 pallindrom
    print(1)
else:
    print(0)

# unique non repeating element
l = [1,2,3,1,3,5,4,2,4]   # 2
fre = {}  # empty dist create
for i in l:
    if i in fre:
        fre[i]+=1  # if present inc with 1
    else :
        fre[i] = 1 # intialise with 1
for i in l :      # iterate till the end of l
    if fre[i] ==1 : # find non-repeatinf value in fer[i]
        print("non-repeating element is",i)
        break

# 2) frequency of an element  with dictionary
a = [2,6,6,2,3,4,3,2]
fre= {}
for i in range(len(a)):
    if a[i] in fre:
        fre[a[i]]+=1
    else:
        fre[a[i]] = 1
quarry = int(input("enter:"))
if quarry in fre:
    print(fre[quarry])
else:
    print(0)
l= [10,5,3,4,5,6]  # 4 first non repeating element
fre = {}
for i in l:
    if i in fre:
        fre[i]+=1
    else :
        fre[i] = 1 #
for i in l :      #
    if fre[i] > 1 : #
        print("non-repeating element is",i)
        break
    else:
        print(-1)
        break


# 5)  merge two dict
dict1 ={'ten':10,"twenty":20,"Thirty":30}
dict2 = {'Thirty':30,"Fourty":40,"Fifty":50}
dict1.update(dict2)
print(dict1)

# 6) check if value present in a dictionary
dict1 = {"a":100,"b":400,"c":300}
value = input("Enter the key:")
print("yes" ,dict1[value],"present")

# pallindrom  2 approch

a = str(input())
fre = {}
for i in range(len(a)):
    if a[i] in fre:
        fre[a[i]] += 1
    else:
        fre[a[i]] = 1
count = 0
for i in fre:
    if fre[i]%2 ==1:
        count+=1
if len(a)%2 == 0 and count ==0:
    print(1)
elif len(a)%2 !=0 and  count  ==1 :
    print(1)
else:
    print(0)
dict1 = {'a':100,"b":300,"c":400}
print('a')
person = {"name":"abc","age":25}
for i in person:
    print(i,person[i])
# clear
person = {"name":"abc","age":25}
print(dict[person.clear])
person = {"name":"abc","age":25}
print(tuple(person))
# to make dict with user help:
dic1 ={}
num = int(input("Enter the numbers to which long dictionary to be make"))
for i in range(num):
    key = input("Enter the keys:")
    value = input("Enter the values:")
    dic1[key] = value
print(dic1)
# 13 )
n = 5
d = {} # to make empty dictionary
for i in range(1,n+1):
    key = i   # i (number 1,2..)
    value =i*i  # i*i(squaring...)
    d[key] = value # key = value (mapp)
print(d)  # print(dict keys value ")
# 14) list to tuples
dict1 ={1:"a",2:"b",3:"c"}
print(dict1.items())
# 15)sort ed with help of keys sorted ()
dic = {2: 'Apple', 1: 'Mango', 3: 'Orange', 4: 'Banana'}
sorted_dic = dict(sorted(dic.items()))
for key,value in sorted_dic.items():
    print(key,value)

a = [2,3,5,4,9]  # 17
x = [i*i for i in a]
print(x)
a = [2,3,5,4,9]  # 18
x = [i for i in a if i%2 == 0]
print("Even numbers",x)
s = input("Enter the string :")   # 19
x = [i.upper() for i in s]
print(x)
# 20)
a = 4
print(type(a))
a = 4,
print(type(a))
a = (4)
print(type(a))
a = ()
print(type(a))
a = (4,)
print(type(a))
a = (4,5)
print(type(a))
# 1 6) common element
A = [1, 2, 2, 1]
B = [2, 3, 1, 2]
x = [i for i in A if i in B]
print(x)
n = 5
d = {x:x*x for x in range(n) }
print()
# 16 common element
A = [1,2,2,1]
B = [2,3,1,2]
fre = {}
for i in A :
    if i in fre :
        fre[i] += 1
    else :
        fre[i] = 1  # fre = {1:2,2:2}
C = []     # commom element are  present more than one time  in fre
for i in B :
    if i in fre and fre[i] > 0:  # common element greater than 0 hoga
        C.append(i)
print(sorted(C)) # [1,2,2] output

