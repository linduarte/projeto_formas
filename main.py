# main.py
from dataclasses import dataclass

@dataclass
class Circle:
    radius: float

@dataclass
class Rectangle:
    width: float
    height: float

def area(shape):
    match shape:
        case Circle(radius=r):
            return 3.14159 * r * r
        case Rectangle(width=w, height=h):
            return w * h

# Exemplo de uso para testar:
if __name__ == "__main__":
    circulo = Circle(5.0)
    retangulo = Rectangle(4.0, 5.0)

    print(f"Área do círculo: {area(circulo)}")
    print(f"Área do retângulo: {area(retangulo)}")
    
