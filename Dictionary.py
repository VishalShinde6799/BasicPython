dict1 ={
"love" : 'hate',
"loyalty" : "backstabbing",
"importance" : "ignorance",
"priority" : 'ditch',
"knowledge" : 'dumbness',
'oaths' : 'treachery'

}
if __name__ == "__main__":

    print(dict1["love"])

    list1=[1,2,3,4,5,6,7,8,9]
    list2=['o','i','u','y','t','r','e','w','q']

    #creating a dictionary using zip function::
    dict2= dict(zip(list1,list2))
    dict2[10] ='v'
    print(dict2)

    #creating a dictionary. way2::
    dict3 = dict(virat=89, vishal=123)
    print(dict3)

    #printing keys::
    for i in dict2:
        print(i, end=" ")

    #printing  values::
    for i in dict2:
        print(dict2[i], end=" ")

    #printing values::
    for i in dict2.values():
        print(i ,end=" ")

    #printing key value pairs::
    for i,j in dict2.items():
        print(f"{i} -> {j}")

    x= dict2[1] #get the value at the key
    y= dict2.get(10) #pass key and get value
    print(y)
    print(x)

    #deleting an element from a dictionary::
    dict2.pop(10)
    print(dict2)

    #sort it by key::
    for key in sorted(dict2):
        print(f"{key} -> {dict2[key]}")


    #sort using values::
    #for i in sorted(dict2.get(i)):
    #   print(dict2[i])