import random
from abc import ABC, abstractmethod

# Interfaz
class Coloreado(ABC):
    @abstractmethod
    def comoColorear(self) -> str:
        pass

class Figura(ABC):
    def __init__(self, color="rojo"):
        self.color = color

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def __str__(self):
        return f"Color: {self.color}"

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

class Cuadrado(Figura, Coloreado):
    def __init__(self, lado, color="azul"):
        super().__init__(color)
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado

    def comoColorear(self):
        return "Colorear los cuatro lados"

    def __str__(self):
        return f"Cuadrado - {super().__str__()}, Lado: {self.lado}"

class Circulo(Figura):
    def __init__(self, radio, color="verde"):
        super().__init__(color)
        self.radio = radio

    def area(self):
        return 3.1416 * self.radio ** 2

    def perimetro(self):
        return 2 * 3.1416 * self.radio

    def __str__(self):
        return f"Circulo - {super().__str__()}, Radio: {self.radio}"

# Programa
def main():
    figuras = []

    for _ in range(5):
        tipo = random.choice(["cuadrado", "circulo"])
        if tipo == "cuadrado":
            lado = random.randint(1, 10)
            figura = Cuadrado(lado)
        else:
            radio = random.randint(1, 10)
            figura = Circulo(radio)
        figuras.append(figura)

    for figura in figuras:
        print("-" * 40)
        print(figura)
        print(f"Área: {figura.area():.2f}")
        print(f"Perímetro: {figura.perimetro():.2f}")
        if isinstance(figura, Coloreado):
            print(f"Coloreado: {figura.comoColorear()}")

if __name__ == "__main__":
    main()