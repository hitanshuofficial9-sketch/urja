def howmany(id,val):
    count=0
    for i in id:
        if i==val:
            count=count+1
    print(count)

id=[10,20,50,10,30]
val=10
howmany(id,val)


#global scope
def display():
    global x
    x=10
    print(x)

display()


#passing list,tupple,dicitionary and a function in a parameter
def func_list(list):
    print(list)

l=[1,2,3,4,5]
func_list(l)