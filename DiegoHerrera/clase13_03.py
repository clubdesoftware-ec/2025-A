#Variables
# Almacenamos valores durante la ejecución del programa

# Funciones
# Bloque de código que vamos a realizar para un objetivo

# Clases
# Coleccion de variables y funciones que nos permite agruparlas
# Para representar un concepto
# funciones -> metodos
# variables -> miembros

class Perro: 
    def __init__(self):
        self.nombre = "Mocca"
        self.edad = 2
        self.x = 10
        self.y = 20

    def moverEnx(self):
        self.x += 1
    
    def moverEnY(self):
        self.y += 1

dog = Perro()   # Se define un nuevo tipo de variable, y la definición se escribe arriba
dog2 = Perro()
print(dog.nombre)
dog.moverEnx()
print(dog.x)     # Print 11   
print(dog2.x)    # Print 11


# Es importante para hacer un código más organizado
# Reutilizar para inicia proyectos, se puede agregar funcionalidades sin tener que reescribir el código
# Define sus própios métodos, no afecta a lo demás.
# Usar interfaz que otros programadores van a usar.
# Solución para problema de organizar variables y funciones, para que otros usen el código de manera fácil y eficiente
# Permite mantener cierto estado