# multiplication table for using for_loop
count = 1
for x in count:
    print("5 X",x+1,"=",5*(x+1))
    count+=1
    if(x>10): # if, else ,elif, for, while, match (:) mandatory hai two bindi.
      break

num = int(input('Enter the num:'))
num =0    # for user input:
print("Table is:")
while(num<=10):
    print("6 X",num+0,"=",6*(num+0))
    num = num +1

a = int(input("Enter the number(a):"))
b = int(input("Enter the number(b):"))
m =1   # power  find  program:
i=1
while(i<=b):
    i=i+1
    m = m*a
    if(i>b):
      print(a,"raised to the power",b,"is:",m)
num = int(input("Enter the number:")) # factorial program :
i=1
pd=1
while(i<=num):
    pd = pd *i # in python not this type like pd*=i,i+=1
    i = i+1
    if(i>num):
     print("Factorial sum is :", pd)

