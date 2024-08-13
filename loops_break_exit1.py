for x in range(0,5,):# start with 0 and print end with 4(max-1)
    print(x)

print("range in 3 parameters:")
for x in range(0,12,2):# 0-11(max-1) tak chelga or 2 ka increment hoga(3 wala parameter increment ka lea hota hai)
    print(x)

print("for loops in string")
for x in "apple": # loops in string
        print(x, end =" ") # apple in one line print
print("for else in loop:")
for x in range(2,6):      # max-1 always:(6-1) tak chalega
    print(x)              # for with else use
else:
    print("all are print:")

print("else not print in these becoz break statement in spotted by loop:")
for x in range(5):
    if x==3:
        break    # 3 miljana ka bad break lag jaega aga nhi chalega
    print(x)
else:
    print(" ye print nhi hoga:")
print("Nested loop :")
fruits = ["apple","banana","mango"]
vegetable = ["lemon","ginger","lesun"]
for x in fruits:
  for y in vegetable :
     print(x,y)

print("pass_statement in loop:") # pass ko jab lagata hai tab loop ma kuch print nhi kara na hai or error  ka bacha na hai
for x in [0,5,1]: # pass kuch nhi karega loop ko as it is rahe na dega kuch print nhi karega
    pass     #  pass statement error nhi a na deta hai