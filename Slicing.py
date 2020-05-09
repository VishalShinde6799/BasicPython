import time

time1=time.time()
string= "hahahahahahahahahahahhahaha"
string1= "nanananaanananananananananananana"
print(string, string1)
for i in range(len(string)):
    print(string[i]+string1[i], end="",)

print()

substr= string[0:7]
print("the string is %s \n"%string)
print('a' in string)
print(f"the test case in string is {string[:6]}")
print(f"substring of string is {substr}")

substr1= string1[0:15:2]
print(f"substring of string1 alternate characters is {substr1}")
print(f"the reverse of string1 is: {string1[::-1]}")
print(f"the special character from string is: {string[len(string)%15]}")

'''A string can be completely changed. A certain index cannot be changed
string[len(string)%15]= "b"
print(f"the special character from string is: {string[len(string)%15]}")'''

ex= "vishal"
print(ex.title())
print(ex.upper())
ex1= ex.upper()
print(ex1)
print(ex1.lower())

print(ex1.casefold())  #casefold
print(ex.capitalize()) 

print(string1.center((len(string1)+8), '*')) 
#adds equal no of specified characters to the left and right. 
# if second argument is not given, takes space!!!

count = string1.count('na', 0, 10 )
print(count)
#counts number of 'na's in string1 from 0th index to 10th!!
print(string1.count('n'))
print(string1.count('a', 4, -5)) #from index 4 to index -5(excluded)
print(string)
print(string.count('a', 5)) #from index 5 to the last(included)

print(string1.find('ana'))

shiv= 'shiv jayanti, shiv jayanti festival, shiv jayanti- jay bhavani'

print(shiv.count('shiv'))
print(shiv.count('jay'))
print(shiv.find('ant'))
print(f"{shiv[8]}{shiv[9]}{shiv[10]}")

print(shiv.split('v', 2)) 
print(shiv.split())
#creates an array of elements from the occurences of given argument
#if not given, takes space
# the second argument gives number splits, starting from 

extring=string1.replace('n', 'b')
print(extring)

print(shiv.replace('shiv', 'shivaji'))
print(shiv.replace('shiv', 'shivaji', 2))

digistring = '123456780'
print(digistring.isdigit())

sample= "this is a sample string for assignments"
lista= sample.split()

lista.remove("a")
print(lista)
for i in lista:
    print(i, end=" ")

print(f"\nreverse of sample is:: {sample[::-1]}")

time2=time.time()
print(time2-time1)

