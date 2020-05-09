

def add(a, b):
   return a+b
def sub(a,b):
    return a-b

def div(a,b):
    if b==0:
        print("can't divide by zero")
    else:
        return a/b

def mul(a,b):
    return a*b



def indirect(i, a, b):
    switcher = {
        0: add(a, b),
        1: sub(a, b),
        2: mul(a, b),
        3: div(a, b)
    }

    fun = switcher.get(i, lambda: "invalid")
    print(fun)


if __name__ == '__main__':
    ch = 1
    while(ch==1):
            a = int(input("enter an integer: "))
            b = int(input("enter another one: "))
            c= int(input("enter a choice \n 0:add \n 1:sub \n 2: mul \n 3:div: "))
            indirect(c,a,b)
            ch = int(input("do you want to continue..?"))

    '''if c==0:
        add(a,b)
    elif c==1 :
        sub(a,b)
    elif c==2 :
        mul(a,b)
    elif c==3 :
        div(a,b)
    else :
        print("wrong choice")
'''
   
           