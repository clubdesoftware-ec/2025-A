## variables 
# Almacenamos valores durante la ejecución del programa 

## funciones 
# Bloque de codigo que vamos a realizar para un objetivos
# Variables locales, parametros, variables global

## clases
#coleción de variables y funciones qeu nos permiten agruparlas
# para representar un comsepto 
# funciones -> metodos 
# variables -> miembros
#_init__ -> constructor

class Perro:
    def __init__(self):
        self.nombre ="Mocca"
        self.edad = 2
        self.x = 10
        self.y = 20
        
    def moverEnX(self):
        self.x += 1
    
    def moverEnY(self):
        self.y += 1

dog = Perro()
print(dog.nombre)
dog.moverEnX() # moverEnX(dog)
print(dog.x)


l = [32, 324 , 123]
l.append(54)
print(l)

