def febo(n):
    if n<=0:
        return 1
    return febo (n-1) + febo (n-2)

t=febo(3)
print(t)


def fb(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fb(n-1)+fb(n-2)
    
g=fb(5)
print(g)
