class point:

    def __init__(self, x=0, y=0):
        super().__init__()
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"{self.x}, {self.y}"

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return point(x, y)

    def __mul__(self, other):
        y = self.y * other.y
        x = self.x * other.x
        return point(x,y)

    def __sub__():
        pass
    def __div__():
        pass
    
p1 = point(2,3)
p2 = point(4,3)
p3 = p1+p2
print(p3)
p3 = p1*p2
print(p3)