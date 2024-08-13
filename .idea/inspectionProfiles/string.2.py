name = "manish,jha"
print(len(name))#len= 10
for character in name:
    print(character)
print(name[0:8])
print(len(name[:]))
print(len(name[:4]))# length ke lia (len function
print(len(name[4:5]))
print(name[0:-5])  # inedex stars from zero.
print(len(name[5:4]))  # 5>4 so first(5) is greater than 4=>0
print((name[-3:-1]))   #  len(10) -3 => 7,10-1 => 9, 7:9(maxsize- 1)(9-1=8) ,7:8(jh),
print(name[-10:0])  #  negative wale ma karta hai len ma sa minus .
print(len(name[-5:0]))#len -5 => (5:0)  5>0 => 0 (no print)
