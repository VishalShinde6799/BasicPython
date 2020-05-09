import Numlist as n 

def hello():
    return 'hiii'

def printlist(listobj):
    print(listobj.split())

def upd_string(string):
    string= string+" appended part"
    print(f"The string in function  is {string}")

def display(name, age, city):
    print(f"the city is {city}")
    print(f"the name is {name}")
    print(f"the age is {age}")

def disp(a, b=20):
    print(f"thre values are:: {a} and {b}")

print(hello())
printlist(n.str1)

str1 = "base part"
upd_string(str1)
print(f"the string outside function is:: {str1}")
display(age=25, city='nashik', name='tukya')
display('vicky', city='pune', age=20)
#keyword arguments can follow positionals, but not vice versa
display('vicky', 20, city='nashik') #is right
'''display('vicky', age=30, 'solapur') 
display(name='vicky', 20, city='nashik') # both throw error'''

disp('virat') #requires two arguments but only one is passed, second is taken from the definition

#variable length arguments::::
'''python provides a facility that allows us to pass comma separated arguments to a funtions. 
these arguments are treated as tuples'''

def disp2(*names):
    for name in names:
        print(name, end='\t')

disp2('aka','bika','rika','chika')