add = lambda a,b: a+b
print(add(3,2))

l = [lambda x:x**2, lambda x:x**3, lambda x:x**4]

for i in l[0:2]:
    print(i(2))

