class parent:
    parent_name = ""
    child_name = ""

    def __init__(self):
        print("the parent object created")

    def display(self):
        print(self.parent_name)

class son(parent):
    def __init__(self):
        super().__init__()
        print("the son class created")

    def display_child(self):
        print(self.child_name)

    def display_parent(self):
        print(self.parent_name)

class daughter(parent):
    def __init__(self):
        super().__init__()
        print("the daughter class created")

    def display_child(self):
        print(self.child_name)

    def display_parent(self):
        print(self.parent_name)

class father():
    fathername =""

    def __init__(self):
        super().__init__()
        print("the father cons")
    def show_father(self):
        print("the father is ::", self.fathername)

class mother():
    mothername = ""

    def __init__(self):
        super().__init__()
        print("the mother cons")

    def show_mother(self):
        print("the mother name is:: ", self.mothername)

class child(father, mother):

    def __init__(self):
        super().__init__()
        print("the child cons")

    def show_parents(self):
        print(f"the father is:: {self.fathername} \nThe mother is:: {self.mothername}")


if __name__ == "__main__":
    d1 = daughter()
    s1 = son()
    s1.parent_name = "vishi"
    s1.child_name = "dfvb"

    d1.parent_name = "abhi"
    d1.child_name = "findruss"

    d1.display_child()
    d1.display_parent()
    print()
    s1.display_child()
    s1.display_parent()

    c1 = child()
    c1.fathername = "vishi"
    c1.mothername = "YTA"
    c1.show_father()
    print()
    c1.show_mother()
    print()
    c1.show_parents()
    