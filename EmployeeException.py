class vishal(Exception):
    def __init__(self,msg):
        print(msg)

class Employee:

    def __init__(self, id, name, sal, desig):
        super().__init__()
        self.id = id
        self.desig = desig
        self.name = name
        self.sal = sal
    
    def getdetails(self):
        try:
            sal = int(input("enter a salary\n"))
            if sal<10000 and sal<50000:
                raise vishal("salary cannot be less than 10k and greater than 50k")
            name = input("enter employee name\n")
            if name == "":
                raise vishal("name cannot be empty")
            desig = input("enter the designation:\n")
            if desig == "":
                raise vishal("designation cannot be empty")
            id = int(input("enter the ID:\n"))
            if id<0:
                raise vishal("id cannot be negative")
        
        except vishal as e1:
            print(f"{e1}")

        else: print("data collected")

e1 = Employee(1, 'name0',20000 , '')
e1.getdetails()
        
        