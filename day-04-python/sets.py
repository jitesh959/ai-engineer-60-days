s = {"hi","hello","hi",52,6,52,True,False,None}
s2 = {"jay","jack",256,145,256}
print(type(s))
print(s)

print(s.union(s2))
s.update(s2)
print(s)