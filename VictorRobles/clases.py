## Clases
# Colección de variables y funciones que nos permiten agruparlas 
# para representar un concepto 
# funciones = métodos
# variables = miembros
# __init__ = constructor

class Perro:
    def __init__(self):
        self.nombre = "Chimuelo"
        self.edad = 3
        self.x = 15
        self.y = 30
    
    def moverEnX(self):
        self.x += 1
    
    def MoverEnY(self):
        self.y = += 1

dog = Perro()
print(dog.nombre)
dog.moverEnX()
print(dog.x)
