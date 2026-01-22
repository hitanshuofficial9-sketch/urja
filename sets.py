a={1,1,1,2,2,4}
print(a)

a={1,2,3}
a.add(4)
print(a)
a.remove(4)
print(a)

a={1,2,3,4}
a.discard(5)
print(a)

a={1,2,3}
print(max(a))

a={1,2,4,5}
b={3,7,4}
print(a|b)
print(a&b)
print(a-b)
print(a^b)

a={1,2,3,4,5}
for i in a:
    print(i)

a={1,2,3,4}
for i in a:
      print(4 in a)

l={1,2}
x={1,2,3,4}
l.issubset(x)
x.issubset(l)    
print(l.issubset(x))  
print(x.issubset(l))

a={1,2,3,5}
b={3,1,2}
print(a>b)