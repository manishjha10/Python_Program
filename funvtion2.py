# maxium of three numbers

# a = int(input("enter a"))
# b= int(input("enter b"))
# c = int(input("enter c"))
# find_m = lambda a,b,c : (a if a>b>c else b if b>c else c)
# result = find_m(a,b,c)
# print(result)
#
# # add two elements in list
# l = [1,2,3,4]
# m = [5,6,7,8]
# ans = list(map(lambda x,y :x+y ,l,m))
# print(ans)
# # square
# n = int(input("enter the number:"))
# ans = lambda n:n*n
# print(ans(n))

# cube of numbers
# n = 8
# ans = lambda n : n**3
# print(ans(n))
#
# # square of number of list :
# l = [1,2,3,4]
# ans = list(map(lambda x:(x**2),l))
# print(ans)
#
# # maxium of two numbers
# a = 10
# b = 25
# ans = lambda a,b : a if a>b else b
# print(ans(a,b))
# # even odd filter out in a number
# n = int(input("no"))
# ans = lambda n : "even" if n%2 == 0 else "odd"
# print(ans(n))
#
# # filter out even odd in a list
# l = [1,2,3,4,5]  # using map fuctions .
# print(list(map(lambda x :  x%2==0,l)))  # boolean return
#
# # filter function
# def fun(a):
#     if a % 2 == 0:
#         return True
#     else :
#         return  False
# a = [1,2,3,4,5]
# ans = list(filter(fun,a))
# print(ans)
# # using lambda function function filter out
# #1)
# n =[1,2,3,4]
# x = [i for i in n if i%2 == 0]
# print(x)
# # #2)
# l =[1,2,3,4]
# ans = list(filter(lambda x: x%2 == 0,l))
# print(ans)
# num = int(input("enter the number"))
# def fact(num):
#     if num== 0 or num == 1:
#         return 1
#     return fact(num-1) * num
# ans = fact(num)
# print(ans)
n = [65,25,99,20,10,8,9,7,5]
ans = lambda x :'even' if n %2 == 0 else "odd"
print(ans(n))
# 18 ) number greater than 60
n = [65,25,99,20]
ans =  list(filter(lambda x :  x > 60,n))
print(ans)
