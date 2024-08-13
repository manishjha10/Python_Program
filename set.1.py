s = {1,2,3,2,5} # repeating values not print it print only one time
print(s)   # sets order not matter printr random order
info = {"Manish jha",20,"Subject","Btech_CS"} # multiples values store ,im_mutable not change the value
print(info)
print(len(s))  # repeating not count len
print(type(s))
s = {} # empty list, it gives dict
print(type(s))
s = set() # correct way to make empty list
print(type(s))
s1 = {1,2,3,4}
s2 = {5,4,6,7}
print(s1.union(s2)) # union of both sets and give answer
s1.update(s2) # all s2 values add in s1
print(s1)
m = {4,5,4,6}
n = {5,2,8,3}
d = m.intersection(n)
print(d)
city = {"goa","munbai","chenni"}
city1 ={"hyderabad","goa","chenni"}
city3 = city.intersection(city1)
city.intersection_update(city1)
print("both:",city)
print(city3) # intersection gives the common value which present in both the sets
city3 = city.symmetric_difference(city1)  # symmetric_difference print those values which not common in both the sets
print(city3)   # print not common values in both the sets
city3 = city.difference(city1) # difference it works similar a-b(a ma sa ba sub)
print(city3) # city -city1 rest re print
# isdisjoint returns true if both the sets have no common value
city = {"manish","jha","google"}
city1 ={"microsoft","ceo","apple"}
city3 = city.isdisjoint(city1) # in both there is no common value so return true
print(city3)
#  superset  means the set which present in given set
city = {"manish","jha","google"}
city1 ={"microsoft","ceo","google","apple"}
city3 = city.issuperset(city1)
city3 = city.issubset(city1) # city ka sare elements not presesnt in city1 sa retuen false
print(city3)
print(city3) # city1 ka all elements present in city so give true else give false
m = {"m","j"}
n = {"m","j","l"} # n all elements present in m
l=m.issuperset(n) # so give true
l= m.issubset(n)# checks all elements of first set is present in second set if present then true else false
print(l)  # m ka sare elements present hai n ma to true
print(l)
# we also add sets value
s1 = {"manish","jha","college"}
s1.add("name")  # two sets add with thw help of add
print(s1)   # 2 str pass karega value magega add ma
cities = {"delhi","agra","kanpur"}
place = {"tajmahl","lalkila","circuit house"}
cities.update(place) # update full str
print(cities) # store kar ka update nhi hoga ,update orginal str ma hoga use to print kar a na hoga

'''  Remove / Discard method is used to remove
Remove => if Element or str not present in given string so it raise an error 
but Discard => if Element or str not present in given string so it not give an error 
'''
cities = {"delhi","agra","kanpur"}
#cities.discard("agra")
cities.discard("goa") # goa  not present in cities but it not give error
print(cities)
# remove
cities = {"delhi1","agra1","kanpur1"}
cities.remove("agra1")
#cities.remove("goa") # goa  not present in citiesso it gives an error
print(cities)
# pop () random value select kar leta hai or return kardeta hai
cities = {"delhi2","agra2","kanpur2"}
s = cities.pop()
print(s)
# del help we delete entire set
name = {"mannat","place"}
del name  # del => delete kae ka entire set ko error raise kar deta hai name error
print(name)
# clear () best del method  to remove entire set
name = {"mannat","place"}
name.clear() # entire set is delete
print(name) # not print set is delete
# '''  sets methods
# union,update,intersection,interesction_update,issubset,issuperset,symmetric_difference,isdisjoint
# add,update(entire set),remove ,discard,del,clear,pop,
# '''
