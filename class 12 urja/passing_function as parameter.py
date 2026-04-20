def greet(name):
    return(f"hello{name}")
def clove(func,value):
    return func(value)

t=clove(greet,"urja")
print(t)


#typehinting
from typing import List
def add(numbers:List[int]):
    return sum(numbers)

t=sum(4)
print(t)