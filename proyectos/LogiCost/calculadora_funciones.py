import Request as rq

class funciones_calculadora:
    def __init__(self, kilometrosxdia, gdcombustible, costo_neumatico, costo_preventivo, costo_correctivo):
        self.kilometroxdia = kilometrosxdia
        self.gdcombustible = gdcombustible
        self.precio_diesel = rq.get_fuel_price()
        self.rendimiento_neumaticos = 47500
        self.costo_neumatico = costo_neumatico
        self.costo_preventivo = costo_preventivo
        self.costo_correctivo = costo_correctivo

    def rendimiento_combustible(self):
        return self.kilometroxdia / self.gdcombustible * self.precio_diesel

    def costoxkilometro(self):
        return self.precio_diesel / self.rendimiento_combustible()

    def costo_combustible_año(self):
        return self.costoxkilometro() * self.kilometroxdia * 365

    def costo_total_neumaticos(self):
        return self.costo_neumatico * self.numero_neumaticos

    def costo_neumaticoxkm(self):
        return self.costo_total_neumaticos() / self.rendimiento_neumaticos

    def costo_neumatico_anual(self):
        return self.costo_neumaticoxkm() * self.kilometroxdia * 365

    def costo_variable_anual(self):
        return self.costo_combustible_año() + self.costo_neumatico_anual() + self.costo_preventivo + self.costo_correctivo

   