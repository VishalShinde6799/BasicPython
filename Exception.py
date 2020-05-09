def divexc():
    try:
        a = int(input("enter a number"))
        b = int(input("enter a number"))
        c = a/b
        print(c)
    except Exception:
        print("can't divide by zero")
        pass
    else:
        print(a/b)

def fileexc():
    try:
        name = input("enter the file name")
        fileptr = open(name, 'r')
    except IOError:
        print("file not found")
    else:
        readvar = fileptr.read()
        print(readvar)
    finally:
        print("error")

def writeexc():
    try:
        name = input("enter the file name")
        fileptr = open(name, 'a')
    except IOError:
        print("file not found")
    else:
        fileptr.write("bello")
    finally:
        fileptr.close()
        print("closed")

def airthexc():
    try:
        a = int(input("enter first "))
        b = int(input("enter b "))

        if b is 0:
            raise ArithmeticError
        else:
            print(f"a/b: {a/b}")
    except ArithmeticError:
        print("this is not happening dude")


'''divexc()
fileexc()
writeexc()'''
airthexc()

