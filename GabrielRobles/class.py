## variables
# Almanezamos valores durante la ejecucion del programa 

## funciones
# Bloque de codigo que vamos a realizar para un objetivo
# Variables locales, parametros, varibles global

## clases
# coleccion de variables y funciones que nos permite agruparlas 
# para representar un concepto
# funciones -> metodos
# variables -> miembros
# __init__ -> constructor

class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.x = 10
        self.y = 20

    def moverEnX(self):
        self.x += 1

    def moverEnY(self):
        self.y += 1

dog1 = Perro("Mocca", 2)
dog2 = Perro("Fido", 7)
print(dog1.nombre)
dog1.moverEnX() # -> moverEnX(dog)
print(dog1.x)  # print 11
print(dog2.x) # print 10

l = [32, 234, 123]
l.append(54)
print(l)