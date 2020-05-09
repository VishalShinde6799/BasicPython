import Dictionary as dc
def getdata(listobj):
    var2= listobj.key()
    var = listobj.get()
    return var2, var

def printdata(key , value):
    print(f"the keys and values are::{key}: {value}")

for i, j in dc.dict1.items():
    printdata(i,j)
    print(getdata(dc.dict1))

    