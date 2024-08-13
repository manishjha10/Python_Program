a= int(input("Enter the number: "))
if (a<=0):
    print("you are play:")
elif (a>0):
        if(a==5):
            print("you are win:")
        elif(a!=0):

             print("you are not win:")
        else:
                    print("you ")
else:
    print("you are not play:")
age = 20
if (age < 0):
    print("you are vote:")
elif (age > 0):
    if (age != 0):
        print("you are not vote:")
    elif (age == 0):
        print("you are oveslly vote:")
    else:
        print("yaaa vote:")
else:
    print("NO")

l = [1,2,3,4,5]
k = 3
if k <= len(l) :
    l[k-1] = l[k-1][::-1]
print(l)