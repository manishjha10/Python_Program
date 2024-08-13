# 1) logic)1
words = ["meet","red"]
x = "e"
for i in range(len(words)):
    if x in words[i]:
        print(i)
# 2 logic)2   #list comprehension
words = ["meet","red"]
ans = [i for i in range(len(words)) if x in words[i]]
print(ans)
# 2) num
# num1 = input("enter num1") # string inputs
# num2 = input("enter the num2")
# num3 = int(num1)
# num4 = int(num2)
# ans = num3 * num4
# print(ans)
#3) last words count in string
# s = str(input("Enter string as a input"))
# n = len(s) # carry forward technic reverse start
# count =0
# for i in range(n-1,-1,-1):
#     if s[i] == " ":
#         break
#     else:
#         count += 1
# print(count)
# 4) unique elements foe xor logic
l = [2,2,1]
ans = 0
for i in l:
    ans = ans ^ i
print("unique element",ans)
# 5) reverse fron index given
l =[1,2,3,4,5,6,7,8]
k = 3
l1 =l[:k]
l2 =l[k::-1]# 4 3 2 1
ans = l1 +l2
print(ans)


l =[1,2,3,4,5,6,7,8]
k = 3
l1 =l[:k] # 123 as it is
l2 =l[k::] # 4 5 6 7 8
l2.reverse()
ans = l1 +l2
print(ans)





