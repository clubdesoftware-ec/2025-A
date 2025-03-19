##Variable -> almacenan valores durante la ejecución del programa

##Funciones -> bloque de código que vamos a realizar para un objetivo
#strings - variables locales, parámetros, v. global

#Clases -> colección de variables y funciones que nos permite agruparlas
# funciones -> método
# variables -> miembros 

'''def fn(x,y, z):
    w = 5
    v = 3
    print(l)
    print("HI desde fn")

l = 10
fn("gato","perro", "loro")'''

class Perro:
    def __init__(self):
        self.nombre = "Mocca"
        self.edad = 2
        self.x = 10
        self.y = 20
        
    def moverEnX(self):
         self.x += 1

    def moverEnY(self):
        self.x += 1


dog = Perro()
print(dog.nombre)
dog.moverEnX()
print(dog.x)


'''def moverEnY(self):
    print(dog.nombre)
'''

