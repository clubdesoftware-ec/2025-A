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
        self.y += 1

dog = Perro()
dog2 = Perro()
print(dog.nombre)
dog.moverEnX()
print(dog.x)
print(dog2.x)


l = [32, 234, 123]
l.append(54)
print(l)