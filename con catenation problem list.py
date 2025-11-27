l=[1,3,5,9]
n=len(l)
print(l*2)

l=[1,3,7,8]
n=len(l)
r=[]
for i in range(0,3):
    for j in range(0,len(l)):
        r.append(l[j])
print(r)        
