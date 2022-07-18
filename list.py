from typing import Set

anewlist=["zero","one" ,"two" ,"three" ,"four","five","six"]


secondlist=["apple","banana" ,"orange"]

thirdlist=["zero","one" ,"two" ,"three" ,"four","five","six"]
fourthlist=["zero","one" ,"two" ,"three" ,"four","five","six"]





new_list=[]

for x in anewlist:
    if "e" in x:
        new_list.append(x)

print(new_list)

new_list=[x for x in anewlist]
new_user
print(new_list)

new_list=[x if x!="three" else "orange" for x in anewlist]
print(new_list)
print(secondlist)
