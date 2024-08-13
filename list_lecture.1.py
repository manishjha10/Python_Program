# manupilating list adding elements
# 1) Append() -> Add element at end of list
l = [1,2,'manish','jha',3.5,[4,25]]
l.append(10)
print(l)
l.append([100,200]) # l.append(100,200) -> without [] multiple aruments in l.append gives error.
print(l)
# 2) insert() use to insert some value ,addition of value in that index and that index is swift ==> l.insert(index,value)
l = [1,2,'manish','jha',3.5,[4,25]]
l.insert(2,'hello')
print(l)
# 3) extend() ==> use to add mutiple values in list in one time in same list
l = [1,2,'manish','jha',3.5,[4,25]]
l.extend([100,20.45,60])
print(l)
# 4 )remove() ==> use to remove the only  first element l.remove(accept value or argument)
l = [1,2,1,'manish','jha',3.5,1,[4,25],1]
l.remove(1)
print(l)
# 5 ) pop() => index ,remove by default last element from list , l.pop(last element from list)
l = [1,2,'manish','jha',3.5,[4,25]]
l.pop() # remove by default laas telement  that is [4,25]
print(l)
l.pop(2)  # remove manish from list
print(l)

