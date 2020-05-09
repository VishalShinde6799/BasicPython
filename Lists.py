List =[1,2,3,4,] #numeric list
print(List)

List1 = ["pune","nashik","mumbai"] #char list
print(List1)
List2 = [1,"Pune",2,"Nashik","Mumbai",4,3,12] #mixed list
print(List2)
list1 = [x+6 for x in [5,6,7,8]] #using for loop
print(list1)
str=list("python") # string into list
print(str)

#Accessing the list
print(List[0])
print(List[1],List[2],List[3])

#Changing the list member
List2[0]=101
List2[2]=105
List1[2]="Solapur"
print(List1)
print(List2)


# Using loops with List

for i in List2:
    print(i,end=',')
print()

for sample in List1:
    print(sample,end=' ')
print()
# Checking the member is present or not

if "pune" in List1:
    print("Pune Present")
else:
    print("Pune not Present")

# Finding the length of list

List3 = [1,"Pune",2,"Nashik","Mumbai",4,3,12]
print(len(List3))
print()

# Using Append()
List1 = ["pune","nashik","mumbai"]
List1.append("Solapur")
print(List1)
print()

# Adding element at a position

List1.insert(1,"Aurangabad")
print(List1)

# Removing the elements

List1.pop()
print(List1)
List1.pop(1)
print(List1)
print(List3)
List3.remove("Mumbai")
print(List3)

# Deleting a List

sample = [1,2,3,5,5]
print(sample)
del sample
print("______")
#print(sample)

list1= [1,2,3,4,5,6,7,8,9,0,11,12,13,14,15,16,17]

list2= list1[0:5]
print(list2)
print(list1[3:9])
print(list1[0:-1])
print(list1[1:])
print(list1[::-1])
print(list1[0:10:2])
print(list1[::-2])  #even index
print(list1[-2::-2]) ##odd index
list2=list1[::-2]  
print(list2)

#swapping first and last
temp=list1[-1]
list1[-1]=list1[0]
list1[0]=temp
print(list1)

#printing greatest
for i in list1:
    if(i>(i+1)):
        temp=i

print(temp)

#concatenating two lists
print(list1+list2)
    