def series(n):
    a,b=0,1
    if n<0:
        print("enter positive number")
    elif n==1:
        return a
    else:
        for i in range(2,n):
            print a
            c=a+b
            a,b=b,c   