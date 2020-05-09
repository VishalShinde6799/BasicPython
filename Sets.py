set1 = {1,2,3,4,5,6,7,1,2}
print(len(set1))

Week= {'Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','Monday'}

print(Week)  #prints the whole set
print(type(Week))  #prints type of container (set)
for i in Week: #prints elements of set one by one
    print(i)

list1 = [1,2,3,4,5,6,7,8,9,1,1,2,3,4]
set1 = set(list1)
print(set1)

set1.add(11) #add one element
print(set1)
set1.update([12,13,14,15])  #add multiple elements
print(set1)
set1.discard(11) #delete one member. if not member, do nothing
print(set1)

set3 = set1.copy() #create shallow copy of a set
'''
if you do set3 = set1 instead of set3 = set1.copy(), the operations you perform on set3 
will be reflected on set1. for example; if you do set3 = set1 and
set3.clear(), set1 will also get cleared
'''
set3.remove(9) #remove one member. if not, raise error
print(set1)
print(set3)
set3.clear() #empties the set

print(set3)
print(set1)

