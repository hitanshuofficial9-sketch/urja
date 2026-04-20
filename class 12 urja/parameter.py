def details(name="urja",age=17):
    print(name,age)

details()    

#variable length parameters
def add(*nums):
    print(sum(nums))

add(1,4,6)


