# # print pattern
# n = int(input("Enter the no. of coloms:"))
# for i in range(1,n+1):# for rows #  for columns
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
# # ulta triangle
# n = int(input("Enter the no. of coloms:"))
# for i in range(n,0,-1):# for rows #  for columns
#     for j in range(0,i):
#         print("*",end=" ")
#     print()
    # half pyrimid
n = int(input("Enter the no. of coloms:"))
for i in range(1,n+1):# for rows
    for j in range(1,n-i): #  for columns
        print(end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
n = int(input("ENter the numebre:") )# half pyramid
for i in range(1, n + 1):
    for j in range(1, n - i+1):
        print(" ",end=" ")
    for j in range(0, i):
        print(" *", end=" ")
    print()
# patterns


