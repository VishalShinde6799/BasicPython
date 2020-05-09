class vehicle:
    pass
    def __init__(self, color):
        self.color = color

class fourwheel(vehicle):
    def __init__(self, color, no_of_gears):
        super().__init__(color)
        self.no_of_gears = no_of_gears

class twowheeler(vehicle):
    def __init__(self, engine_cc):
        super().__init__("red")
        self.engine__cc = engine_cc
        self.color = "blue"

maruti = fourwheel("red", 4)
print(f"{maruti.color}  {maruti.no_of_gears}")
scoot = twowheeler(80)
print(f"{scoot.color} {scoot.engine__cc}")
