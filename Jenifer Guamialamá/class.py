## variables
# Almacenamos valores durante la ejecucion del programa

## funciones
# bloqueo de codigo que vamos a realizar para un objetivo
# variables locales, parametros, variables global

##clases
# coleccion de variables y funciones que nos permite agruparlas
# para represetar un concepto
# funciones -> metodos
# variables -> miembros
#__init__-> constructor

class perro:
    def __init__(self):
        self.nombre = "Mocca"
        self.edad = 2
        self.x = 10
        self.y = 20

    def moverEnX(self):
        self.x += 1
    
    def moverEnY(self):
        self.y +=1

dog = perro()
print(dog.nombre)
dog.moverEnX()
print(dog.x)
