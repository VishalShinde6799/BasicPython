filevar = open('aka.txt' ,'r')
readvar = filevar.read()
charval = filevar.tell()+1

print(f"the number of characters in a file are :: {charval}")

for i in readvar:
    if i.isdigit():
        print(i)

for i in readvar:
    if not i.isdigit():
        print(i)

filevar = open('bika.txt', 'w')
filevar.write(readvar)
filevar.close()



