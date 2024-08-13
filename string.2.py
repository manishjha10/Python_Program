# name = " Manish,jha"
# print(len(name)) # len= 10
# for character in name:
#     print(character)
# print(name[0:8])    # string slicing
# print(len(name[:]))
# print(len(name[:4]))# length ke lia (len function
# print(len(name[4:5]))
# print(name[0:-5])  # inedex stars from zero.
# print(len(name[5:4]))  # 5>4 so first(5) is greater than 4=>0
# print((name[-3:-1]))   #  len(10) -3 => 7,10-1 => 9, 7:9(maxsize- 1)(9-1=8) ,7:8(jh),
# print(name[-10:0])  #  negative wale ma karta hai len ma sa minus .
# print(len(name[-5:0]))#len -5 => (5:0)  5>0 => 0 (no print)
s = "manish"
print(s[::-1])
l = list(s)
l.reverse()
print(l)
# in string we cannot use reverse () to reverse the string
# reverse string to loop ,slicing , convert into list(mutable)
# im_mutable tuple,string,sets,dictionay => reverse function not use to reverse
# s = "manish jha"  #
# l = list(s)
# r = l[::-1]
# p = " ".join(r)
# print(p)
# s = "manish jha"  # jha manish   2
# word = s.split() # string to lst
# word.reverse()  # reverse list
# res = " ".join(word)# list string convert join.
# print(res)
# s = "manish  "
# l = s[::-1]
# print(l)
# input string
t = int(input("Eneter the num:"))
for i in range(0,t):
    count = 0
    vow = 0
    inp = input().lower()
    for i in inp:
          if i == 'a' or i == 'e' or i == 'o' or i =='i' or i == 'u':
               vow+=1
          else :
               count+= 1
    print(count)
    print(vow)
#  1) given an array of integer a every element in repeated twice exect 1 find that uniqe number
l  = [1,2,10,20,5,3,10,20,3,1,2]  # 1  Unique Number
u =[]
for i in l:
    if l.count(i) == 1:
        u = i
print(u)
l  = [1,2,10,20,5,3,10,20,3,1,2]  # 2
u =[]
for i in l:
    if l.count(i) == 1:
        u.append(i)  # list form
print(i)
