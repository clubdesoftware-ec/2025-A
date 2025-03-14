## una funcion solo accede a una variables locales,parametros, variables global

##clases
#Coleccion de variables y funciones que nos permite agruparllas
#para representar un concepto
#funciones -> métodos
#variables - miembros 
# __init__ -> constructor, nos permite hacer eso
def fn(x,y,z):
    w=5
    v=3
    print("hi desde fn")

fn("gato", "perro","loro")

class Perro:
    def __init__(self):
        self.nombre="Mocca"
        self.edad = 2
        self.x =10
        self.y = 20
    def moverEnX(self):
        self.x +=1
    def moverEnY(self):
        self.y +=1

dog =Perro()
print(dog.nombre)
dog.moverEnX()
print(dog.x)
