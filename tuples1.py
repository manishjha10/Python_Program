l = (1,2,3,4,3,3,"manish",5)  # tuple() im_mutable
m=(4,5,8)
print(l[0::-3])  # slicing (start,end(not included),step)
# only one (1) print hoga  loop nhi chalega {step (negative ) hai to one time he chalega} in slicing case
print(l[0:-1]) # reverse
print(l[0:-2]) # (1,2,3)
print(type(l))
print(l+m) # (+) concat tuple done
print(l[-1]) # only -1 index that is last index print

n = l.count(3)  # count() how many times repeat nuber
n = l.index(3) # it gives the first index that 3 is present
# n = l.index(311)#     error index not present

n = l.index(3,4,5) #        index(value,start,stop)
tup = [1,2,3,4,8,5,3,4]
n = tup.index(3,4,7)  # 3 value hai ,4 index  sa 3 search hoga or index 7 tak search hoga 3 jis index par 3 find hoga 4 index sa us ko hi print kar dega index
print(n)
print(len(tup))  # length 1 sa start , index 0 sa




