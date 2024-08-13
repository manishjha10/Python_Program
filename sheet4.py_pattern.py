# rows = int(input("Enter the number:"))  # 1)  square
# for i in range(rows):
#     for j in range(rows):
#         print("*",end=" ")
#     print()
# rows = int(input("Enter the number:"))  # 2) sidha triangle
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
# rows = int(input("Enter the number:"))  # 3)  ulta triangle
# for i in range(rows):  # rows start from last- so (rows))
#     for j in range(rows-i):
#         print("*",end=" ")
#     print()
# r = int(input("Enter rows:"))        #12)
# for i in range(1,r+1):
#     a = 1
#     for j in range(1,i+1):
#         print(a,end=' ')
#         a=a+1
#     print()
# r = int(input("Enter rows:"))    # 14)
# a=1
# for i in range(1, r + 1):
#     for j in range(1, i + 1):
#         print(a, end=' ')
#         a = a + 1
#     print()
# r = int(input("Enter rows:"))     # 13)
# for i in range(r):
#     a = 1
#     for j in range(r-i):
#         print(a,end=' ')
#         a=a+1
#     print()
#
# for i in range(1):   # 4)
#     print(1)
# for i in range(1):
#     print(1, "*")
# for i in range(1):
#     print(1, "*", 3)
# for i in range(1):
#     print(1, "*", 3, "*")
# for i in range(1):
#     print(1, "*", 3, "*", 5)
# r = int(input("Enter the rows:"))         # 5)
# for i in range(r):
#     for j in range(r):
#         if j==0 or j==r-1:
#            print("*",end=" ")
#         else :
#             print("_",end = " ")
#     print()
# rows = int(input("Enter the number:"))      # 7)
# for i in range(rows):
#     for j in range(rows-i):
#         print("_",end=" ")
#     for k in range(i+1):
#         print("*",end=" ")
#     print()
# rows = int(input("Enter the number:"))     # 8)
# for i in range(rows):
#     for j in range(i+1):
#         print("_",end=" ")
#     for k in range(rows-i):
#         print("*",end=" ")
#     print()
# n = int(input("ENnter no."))          # 6)
# for i in range(n):
#     print("*",end=" ")
#     for i in range(n-i):
#         print("_",end =" ")
#     for i in range(1):
#         print("*",end=" ")
#     print()
# r=int(input("no"))            # 15)
# for i in range(1,r+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
# for i in range(1,r+1):
#     for j in range(1,r-i+1):
#         print("*",end=" ")
#     print()
#                                   # 9)
# for i in range(1, 6):
#     for j in range(1, 11):
#         if j <= 6 - i or j >= 5 + i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#                                   # 10)
# for i in range(0,5): # for print 5 rows in star
#     for j in range(0,9):  #  no colums in star
#         if j<=i or j>=9-i-1: # j<=i => i =0,1,2,3,4 ,j>=9-i-1 => spaces bad star
#             print("*",end=" ")
#         else :
#             print(" ",end=" ")
#     print()
# # pattern like square in middle part is space
# for i in range(0,5):
#     for j in range(0,10):
#         if j<=5-i-1 or j>=5+i:
#             print("*",end=" ")
#         elif  j<=i or j>=10-i-1:
#              print("*",end=" ")
#         else :
#             print(" ",end=" ")
#     print()
#  1-1)
# N = int(input("enter the rows:"))
# for i in range(N):
#     for j in range(N-i):
#         print("*",end=" ")
#     print()
# # 11 )
# for i in range(1, 6):
#     for j in range(1, 11):
#         if j <= 6 - i or j >= 5 + i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# for i in range(0,5): # for print 5 rows in star
#     for j in range(0,9):  # no colums in star
#         if j<=i or j>=9-i-1: # j<=i => i =0,1,2,3,4 ,j>=9-i-1 => spaces bad star
#             print("*",end=" ")
#         else :
#             print(" ",end= " ")
#     print()
# # 4)
# N = int(input("Enter the no."))
# for i in range(1,N+1):
#     for j in range(1,i+1):
#         if (j%2==0):
#             print("*",end=" ")
#         else :
#             print(j,end=" ")
#     print()
n = int(input("Enter the number:"))
for i in range(1, n+1):
    print("*", end=" ")
    for j in range(n+1-i):
        print("_", end=" ")
    print("*", end=" ")
    print()
n = int(input("ENnter no."))        # 9 ) user input
for i in range(1, n+1):
    for j in range(n-i+1):
        print("*", end=" ")
    for j in range(2*i-2):
        print(" ", end=" ")
    for j in range(n-i+1):
        print("*", end=" ")
    print()
r = int(input("Enter the rows:"))   # 10)
c = int(input("Enter the columns:"))
for i in range(r,0,-1): # 5=>Start
    for j in range(c+1-i):  # 1 star print
        print("*",end=" ")
    for j in range(2*i-2): # 8 spaces (10-2)
        print(" ",end=" ")
    for j in range(c+1-i):
        print("*",end=" ")
    print()
r = int(input("Enter the rows:"))   #9
c = int(input("Enter the columns:"))
for i in range(1,r+1):
    for j in range(c+1-i):
        print("*",end=" ")
    for j in range(2*i-2):
        print(" ",end=" ")
    for j in range(c+1-i):
        print("*",end=" ")
    print()
