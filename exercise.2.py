n = int(input("Enter the numbre:"))  # prime number
count=0
for i in range(1,n+1):
    if n % i == 0:
        count+=1  # prime no only if its factor is either 1 and its own number.
if count == 2:
    print('prime number:')
else:
    print("not prime number:")


#  print the  nth element of fabonacci series .
num = int(input("Enter the number:"))
a = 1
b = 0
s = 0
for i in range(1,num+1):
    s = a+b
    a = b
    b = s
    s1 = s + (a+b)
    print("The",i, "element in Fabonacci  series is",s)
print("Nth sum of  fabonacci series is ", s1-1)



# armstrong number:
n = int(input('Enter the number:'))
su_m = 0
count = len(str(n))
copy = n
while n>0:
    digit = n % 10
    su_m = su_m+(digit ** count)
    n = n//10
if su_m == copy:
    print("Armstrong Number:")
else:
    print("Not Armstrong")



# If any of the elements in the list passed as an argument is true,
# then Python any() function returns a TRUE value. To demonstrate the result of the any() function in various situations,
# we shall consider numerous lists with different entries.
# all values are True


list1 = [1,2,3,4]
print(any(list1))

# all values are False
list2 = [0, False]
print(any(list2))

# True since 2, 4 are True
list3 = [0, 2, 4]
print(any(list3))

# False since the list is empty
list4 = []










