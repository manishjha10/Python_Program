# n =[1,2,1,3,5,2,6,7]
# f = {}
# for i in range(len(n)):
#     if n[i] in f:
#         f[n[i]]+=1
#     else:
#         f[n[i]] =1
# for i in n:
#     if f[n[i]] == 1:
#         print(f[i])
#         break
# d =[1,2,1,2,3,5,6,7]
# fre= {}
# for i in range(len(d)):
#     if d[i] in fre:
#         fre[d[i]] +=1
#     else:
#         fre[d[i]] = 1
# # worksheet solution question 5
# l = [1,2,3,4,5,6,7,8]
# k = 3
# if k <= len(l):
#     l1 = l[:k]#  1 2 3
#     l2 =l[k::] #
#     l2.reverse()
#     print(l1+l2)
# # odd characters from string
# input_string = input("Enter a string: ")
# result = ""
#
# for i in range(len(input_string)):
#     if i % 2 == 0:
#         result += input_string[i]
#         print(i)
#     l = [1, 2, 3, 1, 2, 5]
#     count = 0
#     fre = {}
#     for i in range(len(l)):
#
#    if  l[i] in fre:
#     fre[l[i]] += 1
#     else:
#     fre[l[i]] = 1
#     print(fre)
#     for i in l:
# if fre[i] == 2:
#     print(i)
#     break
# else :
#     print(-1)
#     break
 #if fre[i] == 1:

    # print(i)
  #   break
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# dict1.update(dict2)
# print(dict1)
# dict1 = {'a': 100, 'b': 400, 'c': 300}
# b = 400
# if b in dict1.values():
#     print("yes")
# # dictionary comprhension
# n = 5
# x = {i:i*i for i in range(1,6) }
# print(x)
# # 14 )
# dict1 = {1: 'a', 2: 'b', 3: 'c'}
# x = [(key, value) for key, value in dict1.items()]
# print(x)
# # 15 )
# dict1 = {2:'apple',1:'mango',3:'orange',4:'banana'}
# s = sorted(dict1.keys())
# for i in s:
#     print(i,dict1[i])
# r = 5
# c = 5
# for i in range(1,r+1):
#     for j in range(c-i+1):
#         print(" ",end=" ")
#     for j in range(i):
#         print(" *",end=" ")
#     print()
# for i in range(1,r):
#     for j in range(i):
#         print(" ",end=" ")
#     for j in range(r-i):
#         print(" * ",end=" ")
#     print()
# n = 5
# c = 5
# for i in range(n,0,-1):
#     for j in range(c-i+1):
#         print("*",end=" ")
#     for j in range(2*i-2):
#         print(" ",end=" ")
#     for j in range(c-i+1):
#         print("*",end=" ")
#     print()
#
#
# r = 5
# c = 5
# for i in range(1,r+1):
#     a = 1
#     for j in range(c-i+1):
#         print(" ",end=" ")
#     for j in range(i):
#         print(a,end=" ")
#         a+=1
#     print()
dict1 ={1:'a',2:'b',3:'c',4:'d'}
dic =[(i,j) for i,j in dict1.items()]
print(dic)








