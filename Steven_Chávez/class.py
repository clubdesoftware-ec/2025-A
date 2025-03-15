#variables
# Almacenamos valores durantes la ejecución del porgrama

# funciones
# Blouqe de código que vamos a realizar para un objetivo
# strings
# Variables locales, parametros, varaible global


# Clases
# colección de variables y funciones que nos permite agruparlas
# para representar un concepto
# funciones -> metodos
# variables -> miembros
#__init__ -> contructor , permite construir la clase


class perro:
    def __init__(self):
        self.nombre = "Mocca"
        self.edad = 2
        self.x = 10
        self.y = 20

    def moverEnX(self):
        self.x += 1

    def moverEnY(self):
        self.y += 1


dog = perro()
print(dog.nombre)
dog.moverEnX()
print(dog.x)

