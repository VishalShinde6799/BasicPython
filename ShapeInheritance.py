import math

class polygon:
    def number_of_sides(self):
        return 0

    def area(self):
        return 0

    def perimeter(self):
        return 0

class triangle(polygon):
    def number_of_sides(self):
        return 3

    def area(self, base, height):
        return (0.5*base*height)

    def perimeter(self,a,b,c):
        if a+b>c:
            return a+b+c
        else:
            return "invalid input"

if __name__ == "__main__":

    tri = triangle()
    print(f"area is:: {tri.area(100,150)}")
    print(f"perimeter is:: {tri.perimeter(100,200,100)}")
