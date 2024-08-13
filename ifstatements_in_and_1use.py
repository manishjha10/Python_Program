n = int(input())
if(n%2!=0):
    print("Weird")
elif n%2==0 and 2<=n<=5: # and is used in if statements to check the both the (two conditions) in same time
    print("Not Weird")
elif n%2==0 and 6<=n<=20:
    print("Weird")
elif n%2==0 and n>20:
    print("Not Weird")