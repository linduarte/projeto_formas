# main.py
import math


class Trapezio:
    def __init__(self, base_maior: float, base_menor: float, altura: float):
        self.base_maior = base_maior
        self.base_menor = base_menor
        self.altura = altura

    def calcular_area(self) -> float:
        """Calcula a área do trapézio: ((B + b) * h) / 2"""
        return ((self.base_maior + self.base_menor) * self.altura) / 2

    def calcular_perimetro_isosceles(self) -> float:
        """
        Calcula o perímetro assumindo um trapézio isósceles (lados oblíquos iguais).
        Usa Pitágoras para encontrar o comprimento do lado oblíquo.
        """
        # Projeção da base para formar o triângulo retângulo
        projecao_base = (self.base_maior - self.base_menor) / 2

        # Hipotenusa (lado oblíquo) = sqrt(altura^2 + projecao_base^2)
        lado_obliquo = math.sqrt(self.altura**2 + projecao_base**2)

        return self.base_maior + self.base_menor + (2 * lado_obliquo)


# Bloco de teste rápido na bancada
if __name__ == "__main__":
    # Exemplo: Trapézio com Base Maior = 10, Base Menor = 6, Altura = 4
    trap = Trapezio(base_maior=10, base_menor=6, altura=4)
    print("--- Teste da Classe Trapezio ---")
    print(f"Área: {trap.calcular_area()} m²")
    print(f"Perímetro (Isósceles): {trap.calcular_perimetro_isosceles():.2f} m")
