list1 = [1,2,3,4,5,6,7,8,9,10,13,24,34,45,56] 

import Numlist as N
from time import time

list2 = N.str1.split("\n")
list3 = [1,2,4,5,6,7,8,9,10]

time1 = time()

def binary_search(listobj, key):
    mid = int((len(listobj))/2)
    
    if key>mid:
         return binary_search(listobj[mid:], key)
    elif key==mid:
        return mid

    elif key<mid:
        return binary_search(listobj[0:mid], key)

    else:
        return -1
    

print(binary_search(list3, 942))
time2 = time()
print(time2-time1)
