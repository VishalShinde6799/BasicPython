class shape(metaclass = ABCmeta):
    def __init__(self):
        super().__init__()
        print("i'm an init0")

        @abstractmethod
        def draw_shape(self):
            pass
        
        @abstractmethod
        def set_color(self):
            pass
class circle(shape):
    def draw_shape(self):
        print("draw circle")

circle1 = circle()
circle1.draw_shape()