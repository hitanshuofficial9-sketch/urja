import random
# print(random.randint(5,20))
# print(random.random())
# print(random.uniform(5,20))
# print(random.randrange(5,20,2))

# a=["apple","aryabhatt","bhaskar","rohini"]
# print(random.choice(a))
# print(random.choices(a,k=2))
# print(random.sample(a,2))

n=int(input("Enter the number:: "))
otp="1234567890"
k=" ".join(random.choices(otp,k=4))
if k==str(n):
    print("sucessful")
else:
    print ("fail")

    


