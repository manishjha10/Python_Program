# 1) square
def area_of_sqaure(s):
    area = s * s
    print(area)
area_of_sqaure(4)

# 2 )area_of_circle

def area_of_circle(r):
    area = 3.14**r
    print(area)
area_of_circle(4)

# 3)area_of_sqaure

def area_of_sqaure(a,b):
    ans = a**b
    print(ans)
area_of_sqaure(2,3)
#4) cube numbers
def cube(num):
    ans = num *num *num
    print(ans)
cube(5)
#5)  sum of numbers of x to y
def sum_of_array(x,y):
    for i in range(x,y+1):
        print(i*i)
sum_of_array(3,16)
# 6)
def su_m():
    a = 5
    b = 10
    ans = a+b
    print(a+b)
su_m()
#7
def pythagorus(a,b):# para
    square_a = a*a
    square_b = b*b
    return (square_a+square_b)# calling
ans  = pythagorus(3,4)# argu
print(ans)# str print
# 8
def s_um(a,b):
    add = a+b
    print(add)
def sub(a, b):
    minus = a - b
    print(minus)
def mul(a,b):
    fact = a*b
    print(fact)
def div(a,b):
    division = a/b
    print(division)
s_um(10,5)
sub(10,5)
mul(10,5)
div(10,5)

# 9)

def volume_of_sphere(r):
    area = (4/3)*(3.14**r)
    print(area)
volume_of_sphere(5)

# 10
def ar_ellipse(a,b):
    pi = 3.14
    area = pi*a*b
    print(area)
ar_ellipse(5,6)
#  11 )sum of array
def su_m_array(sum):
    sum = 0
    x = 5
    for i in range(1,x+1):
        sum = sum + i
        print(sum)
su_m_array(5)



# Square root of a number 12)
def perfect_square_root(A):
    sqrt = A ** 0.5
    if sqrt.is_integer():
        return int(sqrt)
    else:
        return -1

# Example usage
A = 50
result = perfect_square_root(A)
print("Square root of", A, "is", result)


# print  all the values of sub array
def value_of_arr():
    arr = [1,2,3,4]
    return print(arr)
value_of_arr()

#1) Sub_Array.

arr = [1,2,3,4]
n = len(arr)
def print_subarray(arr,start,end):
    for i in range(start,end+1):
        print(arr[i])
print_subarray(arr,0,n-1)



#2) print all all the sub arrays

def print_subarray(arr,start,end):
    for i in range(start,end+1):
        for i in range(i):
            print(i)
print_subarray(arr,0,n-1)



#3)
# arr = [1,2,3,4]
# n = len(arr)
# def print_subarray(arr,start,end):
#     for i in range(start,end+1):
#         print(arr[i])
# def print_all_subarray(arr):
#     for i in range(n):
#         for j in range(i,n):
#             print_subarray(arr,i,j)
#     print()
# print_all_subarray(arr)



# 1) find the sum of all the elements in the given array
# 2) print sum of every single sub array.
#1 )
def subarray_elements():
    sum  = 0
    for i in range(n):
        sum = sum + arr[i]
    print(sum)
subarray_elements()

# 2) print each suba_rray elements in
arr  = [1,2,3,4]
n = len(arr)
def subarray(arr,start,end):
    sum = 0
    for i in range(start,end+1):
        sum = sum +arr[i]
    print(sum)
        # print(arr[i])  # print
def all_elements_of_subarray(arr):
    for i in range(n):
        for j in range(i,n):
             subarray(arr,i,j)
all_elements_of_subarray(arr)





