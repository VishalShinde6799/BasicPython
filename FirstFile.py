from builtins import print

var = 11
print(f"variable is {var}")
a=95
a-=-15
a+=15  #shorthand operation
print(f"normal division {a/var} returns a float" )
print(f"floor division {a//var} returns an integer")

'''let it rain over me'''

b = 10
print(b/2)
print(b/3)
print(b//3)
b*=2  #shorthand operation
b/=2    #shorthand operation
b//=2   #shorthand operation
b-=2    #shorthand operation
print(b)

p,q,r = 30,40,50
print(f"respective values of p, q, r are {p, q, r}")

#using the type function::

s=p/3
bool = True
name='vishal'
print(f"the type of p is {type(p)} \n the type of name is {type(name)} \n the type of s is {type(s)} \n the type of bool is: {type(bool)}")