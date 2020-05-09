import calculate as clt


ch=1
while ch==1:
    var1 = int(input("enter the first variable"))
    var2 = int(input("enter the second variable"))
    print(clt.add(var1, var2))
    print(clt.sub(var1, var2))
    print(clt.div(var1, var2))
    print(clt.mul(var1, var2))
    ch= int(input("do you want to continue...?"))