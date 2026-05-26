# main.py
import math
from dataclasses import dataclass


@dataclass
class Circle:
    radius: float


@dataclass
class Rectangle:
    width: float
    height: float


@dataclass
class IsoscelesTriangle:
    base: float
    side: float  # Os dois lados iguais


@dataclass
class PythagoreanTriangle:
    cathetus_a: float
    cathetus_b: float


def area(shape) -> float:
    match shape:
        case Circle(radius=r):
            return 3.14159 * r * r

        case Rectangle(width=w, height=h):
            return w * h

        case IsoscelesTriangle(base=b, side=s):
            # Altura h = sqrt(side^2 - (base/2)^2)
            height = math.sqrt(s**2 - (b / 2) ** 2)
            return (b * height) / 2

        case PythagoreanTriangle(cathetus_a=a, cathetus_b=b):
            # Área de um triângulo retângulo é (base * altura) / 2 usando os catetos
            return (a * b) / 2

        case _:
            raise ValueError("Forma geométrica desconhecida")


def get_hypotenuse(triangle: PythagoreanTriangle) -> float:
    """Calcula a hipotenusa de um triângulo retângulo usando o Teorema de Pitágoras."""
    return math.hypot(triangle.cathetus_a, triangle.cathetus_b)


# Exemplo de uso para testar:
if __name__ == "__main__":
    circulo = Circle(5.0)
    retangulo = Rectangle(4.0, 5.0)

    # Triângulo Isósceles: base = 6.0, lados iguais = 5.0 (Altura será 4.0)
    tri_isosceles = IsoscelesTriangle(base=6.0, side=5.0)

    # Triângulo Retângulo clássico (3, 4, 5)
    tri_pitagoras = PythagoreanTriangle(cathetus_a=3.0, cathetus_b=4.0)

    print(f"Área do círculo: {area(circulo):.2f}")
    print(f"Área do retângulo: {area(retangulo):.2f}")
    print(f"Área do triângulo isósceles: {area(tri_isosceles):.2f}")
    print(f"Área do triângulo de Pitágoras: {area(tri_pitagoras):.2f}")
    print(f"Hipotenusa do triângulo de Pitágoras: {get_hypotenuse(tri_pitagoras):.2f}")

# Fim do módulo de formas geométricas

# Validação final de assinatura nativa
