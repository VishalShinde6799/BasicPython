import random
import math
import numpy as np

#tuple
tup1= ("vishal",'findruss', 'abhishek','vinod')
print(tup1)

#unpacking a tuple
vish, vaish, abhi, vinn = tup1
print(vaish)

#index of an element in a tuple::
print(f" the index of element 'findruss' using directly the element:: {tup1.index('findruss')}")
print(f"Index of element 'vishal' using the unpacked abb:: {tup1.index(vish)}")

tup2 =  (10,20,30,("one","two","three"))
print(tup2[3])

#ASSIGNMENTS ON TUPLES::

tup3= ('aka','bika','chika','pika','rika','eena','meena','dika')

print(tup3[::-1]) #reverse
print(tup3[0:-1]) #excluding last
print(tup3[1:])  #excluding first
print(len(tup3)) #return the size of the tuple
print(tup3[0::2]) #give alternate elements

#existance of an element in a tuple::
if "meena" in tup3:
    print("yeahhhh boiii")

#if you use sorted function with anything, it returns a list!!
tup4 =sorted(tup3)
tup5=tuple(tup4)
print(tup5)

print(max(tup5)) #return the greatest element from tuple

#sorting a list of tuples::
Testlist= [('a','b','c'),('1','2','3'),('man','woman')]
print(sorted(Testlist))

list1=[1,2,3,4,5]
list2=['suresh', 'ramesh','ganesh','yogesh']

#zip function gives key-value pairs from two iterables
tup6= tuple(zip(list1, list2))
print(tup6)
print(f"\nthe list of the tuple is: {list(tup6)}")

#one more zipping example
tup7= tuple(zip(tup5, tup6))
print(tup7)
print(np.array(tup7))

