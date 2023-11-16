import math

class Vector:

    def __init__(self, x, y): #constuctor
        self.x = x 
        self.y = y
    
    def muestra(self):
        print(f"x: {self.x}, y: {self.y}")

    def magnitude(self):
        return round(math.sqrt(self.x **2 + self.y**2),2)
    
vector_1 = Vector(4,5)
vector_1.muestra()
magnitud = vector_1.magnitude()
print(magnitud)

