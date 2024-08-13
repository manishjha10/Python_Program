# def f(n):  # fabonacci with recursion
#     if n <= 1:
#         return 1
#     return f(n - 1) + f(n - 2)  # function call itself
#
#
# n = 5  # indexing start from 0
# ans = f(n)
# print(ans)
# for i in range(1, n + 1):  # series
#     print(f(i), end=" ")
#

def multiply( num1 , num2):
    ans = int(num1)
    ans1 = int(num2)
    sum = ans * ans1
    return sum

num1 = input()
num2 = input()
# ans = int(n)
# ans1 = int(n1)
ans = multiply(num1 ,num2)
final = str(ans)
print(final)
