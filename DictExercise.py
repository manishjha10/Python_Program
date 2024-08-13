Dict = {"human":25,"class":2} # Key: Values pair,ordered Dictionaries
# print(Dict["human"])
print(Dict.get("human1")) # with get() it not give error if key not present in dict.(gives None)

for keys in Dict.keys(): #  keys
    print(keys)
# for values in Dict.values():
#     print(values)
for i in Dict.values():
    print(i)
for x,y in Dict.items():
    print(x,y)
    print(Dict.items()) # tuple pair form
for keys in  Dict.keys(): # this syntax we can print the values of dict{name_dict[]} or dict_name[]
    print("Thee value corresponding to keys ",{Dict[keys]})
# items() print corresponding to key values iteration with f string
for keys,values in Dict.items():
    print(f"the corresponding key and values {keys} is {values}")
# f_string is used to replace values sa
name = " manish jha"   # 1
age = 21
letter= f"hello my name is {name} and i am {age} old"
print(letter)
country = "India"  # 2
city = "Agra"
print(f"HEllo Everyone i am  citizen of {country} and {city}.")
num = 98.233
print(format(num,".2f"))
print(f"multiplication of this is {2*10}") # any operation perform instring with the help of  f string
print(type(f''))  # f string so string type
d = {1:2,8:25}
print(d[1])
Data_Store = {"Roll1":28,"Roll2":85,"Roll":39}
# Data_Store.clear()   # name.clear()
print(Data_Store)
print()
Data_Store = {"Roll1":28,"Roll2":85,"Roll3":39}
Data_Store.popitem() # name.popitem () remove last entity
Data_Store.pop("Roll1") # full key value pair delete  name.pop()
print(Data_Store)
Data_Store = {"Roll1":28,"Roll2":85,"Roll3":39}
del Data_Store["Roll1"] # roll 1 delete del name[]n
print(Data_Store)
print("Manish jha")
