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

class funciones_calculadora2:
    def __init__(self, gastos_mantenimiento_preventivo_anual, gastos_mantenimiento_correctivo_anual
                , gasto_anual_mano_obra, gastos_legalizacion_anual, depreciacion_anual, gastos_administrativos_anuales, costo_inversion
                , costo_neumatico_anual, costo_combustible_año):
        self.gastos_mantenimiento_preventivo_anual = gastos_mantenimiento_preventivo_anual
        self.gastos_mantenimiento_correctivo_anual = gastos_mantenimiento_correctivo_anual
        self.gasto_anual_mano_obra = gasto_anual_mano_obra
        self.gastos_legalizacion_anual = gastos_legalizacion_anual
        self.depreciacion_anual = depreciacion_anual
        self.gastos_administrativos_anuales = gastos_administrativos_anuales
        self.costo_inversion = costo_inversion
        self.costo_neumatico_anual = costo_neumatico_anual
        self.costo_combustible_año = costo_combustible_año

    def costo_fijo_total(self):
        return self.gasto_anual_mano_obra + self.gastos_legalizacion_anual + self.depreciacion_anual + self.gastos_administrativos_anuales + self.costo_inversion\
        + self.gastos_mantenimiento_preventivo_anual + self.gastos_mantenimiento_correctivo_anual + self.costo_neumatico_anual + self.costo_combustible_año\
   