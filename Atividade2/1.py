# 1 - Calculando circulo

import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):

        area = math.pi * (self.raio ** 2)
        return area


raio_do_circulo = 5.0  # Posso substituir pelo valor do raio que eu desejar
circulo = Circulo(raio_do_circulo)
area_do_circulo = circulo.calcular_area()
print(f"A área do círculo com raio {raio_do_circulo} é {area_do_circulo:.2f}")