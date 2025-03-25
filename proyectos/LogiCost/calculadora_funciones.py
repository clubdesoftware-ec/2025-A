class funciones_calculadora:
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2

    def suma(self):
        return self.valor1 + self.valor2

    def resta(self):
        return self.valor1 - self.valor2

    def multiplicacion(self):
        return self.valor1 * self.valor2

    def division(self):
        return self.valor1 / self.valor2

    def potencia(self):
        return self.valor1 ** self.valor2

    def raiz_cuadrada(self):
        return self.valor1 ** 0.5

    def raiz_cubica(self):
        return self.valor1 ** (1/3)

    def raiz_n(self):
        return self.valor1 ** (1/self.valor2)

    def porcentaje(self):
        return (self.valor1 * self.valor2) / 100

    def factorial(self):
        if self.valor1 == 0:
            return 1
        else:
            return self.valor1 * funciones_calculadora.factorial(self, self.valor1 - 1)

    def fibonacci(self):
        if self.valor1 == 0:
            return 0
        elif self.valor1 == 1:
            return 1
        else:
            return funciones_calculadora.fibonacci(self, self.valor1 - 1) + funciones_calculadora.fibonacci(self, self.valor1 - 2)

    def mcd(self):
        a = self.valor1
        b = self.valor2
        while b != 0:
            a, b = b, a % b
        return a

    def mcm(self):
        a = self.valor1
        b = self.valor2
        return (a * b) / funciones_calculadora.mcd(self)

    def suma_lista(self, lista):
        suma = 0
        for i in lista:
            suma += i
        return suma

    def promedio_lista(self, lista):
        suma = funciones_calculadora.suma_lista(self, lista)
        return suma / len(lista)

    def mediana_lista(self, lista):
        lista.sort()
        n = len(lista)
        if n % 2 == 0:
            return (lista[n//2 - 1] + lista[n//2]) / 2
        else:
            return lista[n//2]

