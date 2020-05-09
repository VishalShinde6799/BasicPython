
def fact(num):
    fact = 1
    if num == 0:
        return 1
    
    elif num>0:
        for i in range(num):
            fact = fact*(i+1)
        return fact

    else:
        return 'can\'t caculate'


print(fact(-1))