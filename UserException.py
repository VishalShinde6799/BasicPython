class myerror(Exception):
    pass

try:
    raise myerror("this is the condition of global haphazard")

except myerror as error:
    print(f"situation: {error}")
else:
    print("This is demo")

    '''create an employee class with id, name, desig, sal getdetails(), printdetails().
    using user defined exceptions, handle inputs.
    designation should not be empty, salary should be in between 10000 and 70000
    '''