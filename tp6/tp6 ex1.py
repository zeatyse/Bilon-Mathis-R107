L1= [0]*3
print(L1)
print(type(L1))
print(id(L1))
L1[1]=2
print(L1)
print(id(L1))
for elem in L1:
    print(elem, id(elem))

s = "machine"
print(id(s))

for ch in s:
    print(ch, type(ch), id(ch))