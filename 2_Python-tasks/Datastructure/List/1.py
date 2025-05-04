# Lists
x = list(range(1,20,3))
print(x)
x.append(21)
print(x)
x.pop()
print("Removing the last element", x)
print("Third element is", x[2])
x.remove(4)
print("Removing 4 from list", x)

print()
# Tuples
t = (1,2,3)
print("tuple",t)
print("second element is",t[1])
s1 = set((1,2,3))
s2 = set((3,4,5))
print("set 1 is",s1)
print("set 2 is",s2)
print("Union is ",s1.union(s2))
print("Intersection is ",s1.intersection(s2))
print("Difference s1-s2 is ",s1.difference(s2))
print("Adding element 4 to set 1")
s1.add(4)
print(s1)
print()

# Dictionary
d = {'a':1, 'b':2, 'c':3}
print("Dictionary is",d)
d['d'] = 4
print("Added d:4 to dictionary",d)
d['a'] = 42
print("Replaced a:1 with a:42",d)
print("Keys are", d.keys(),"Values are",d.values())
d.update({'e':6, 'f':7})
print("Updated dictionary",d)
print("Second key is", list(d.keys())[1], "Second value is",list(d.values())[1])
