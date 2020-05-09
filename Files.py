
'''
files can be opened using various modes like read, write and append
open("fILENAME", 'r')
open("filename", 'w')
open("filename", "a")
'''

filevar = open('Factorials.py', 'w')

print(filevar)  #prints the status of the file opening


filevar.write("hhii\t")
filevar.close()
filevar=open("Factorials.py", 'r')
read1 = filevar.read()
print(read1)

filevar = open("aka.txt", 'a')
#filevar.write(f" this is the aka file.")
filevar.close()

filevar = open('aka.txt', 'r')
read1 = filevar.read()

print(read1)

read2= read1.replace("aka", 'bika')

filevar = open("aka.txt", 'w')
filevar.write(f"this was aka file but it has been turned to bika file::\n {read2}")
filevar.close()

filevar = open('aka.txt', 'r')
filevar.seek(0)
print(f"the file pointer is at position:: {filevar.tell()}")
filevar.seek(30)

print(f"the file pointer after seeking is:: {filevar.tell()}")
read1 = filevar.read()
print(read1)
print(f"the file pointer after reading is:: {filevar.tell()}")