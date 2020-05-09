class circle:
    tag = 'heyy'
    pi = 3.1415987
    def __init__(self):
        super().__init__()
        self.radius = 3

    def area(self):
        return (self.radius**2)*(circle.pi)   #to access the class variable, do not refer by object. instead, refer by class name

class student:
    count = 0
    def __init__(self):
        super().__init__()
        print("a non para. constructor")

    def display(self, name):
        print(f"the name is {name}")

    @classmethod
    def asdf(cls):
        cls.count+=2
        print(cls.count)
        
    @staticmethod
    def totals():
        student.count+=1
        print(student.count)

class student1:

    '''this is the student1 class'''
    def __init__(self, id, name, age):
        super().__init__()
        self.id = id
        self.name = name
        self.age = age

    def display(self):
        print(f"id: {self.id}, Name: {self.name}, age: {self.age}")
        print("hii")
        print("ID: %d\nNAME: %s \nAGE: %d" %(self.id, self.name,self.age))
    
class employee:
    '''create a class employee with name, id, designation and salary. 
    create para. constructor, at leaset 3 functions: display(), salary(). 
    create 3 objects and demonstrate use of 
    getattr() and setattr() for the objects'''
    count=0
    def __init__(self, id, name, desi, sal):
        super().__init__()
        self.id = id
        self.name = name
        self.desi = desi
        self.sal = sal
        employee.count+=1

    def CalSal(self):
        print(f"the annual salary is:: {self.sal*12}")

    def emp_display(self):
        print(f"The salary is:: {self.sal} \nThe name is:: {self.name} \nThe designation is:: {self.desi} \nThe id is:: {self.id}")

if __name__ == "__main__":
    my_circle = circle() #creates object using the constructor
    print(my_circle.tag) #accesses the class variable tag
    print(my_circle.radius) #prints radius of the 
    print(2*3.142* my_circle.radius) 

    c2 = circle()
    c2.radius = 5  #radius from the constructor gets overrode
    print(c2.area())
    c2.pi = 10
    print(c2.area()) #calls the area method of the class

    st = student()  #creates object and calls constructor
    st.display("vishal")
    st.totals()

    st1 = student1(10, "vishi", 20)
    st1.display()
    print(f"the name is::{getattr(st1, 'name')}")
    ##print(setattr(st1, "name",  "vishal"))
    print("after setting name vishal::\n")
    print("debug1\n")
    st1.display()
    print("debug2\n")

    print("afer setting name findruss::\n")
    st1.__setattr__("name", "findruss")
    st1.display()

    print(st1.__getattribute__("name"))

    print(st1.__dict__) #gives variables in a dictionary
    print(st1.__doc__) #gives class documentation if any
    
    emp1 = employee(1, 'vishi', 'CEO', 20000)
    emp2 = employee(2, 'findruss', 'Manager', 40000)
    emp3 = employee(3, 'Abhi', '', 0)

    emp1.CalSal()
    emp1.emp_display()

    print(getattr(emp2, 'sal'))
    emp2.emp_display()

    emp3.emp_display()
    setattr(emp3, "sal", 40000)
    setattr(emp3, 'desi', 'worker')
    emp3.emp_display()

    print(employee.count)
    '''write a program to count the number of objects of a class'''

