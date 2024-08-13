# n =[iterab for iterable in range() condition]
 # List Comprehension
n = [i for i in range(100) if i%2==0]
print(n)
n = [i*i for i in range(1,10,2) if (i*i)%2 ==1]
print(n)
n = [1,5,2,26]
b = [8,29,2,82]
m = [n[i]*b[i] for i in range(len(n))]  # multiplication ot two list
print(m)