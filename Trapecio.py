# Autor: Fernando Sebastian Silva Miramontes
# Datos de un trapecio

import math

def calcularArea(baseMayor, baseMenor, altura):
    area = ((baseMenor + baseMayor)/2)*altura
    return area


def calcularPerimetro(baseMayor, baseMenor, altura):
    baseTriangulo = (baseMayor - baseMenor)/2
    hipotenusa = math.sqrt(baseTriangulo**2 + altura**2)
    return baseMayor + baseMenor + hipotenusa*2


def main() :
    baseMayor = int(input("Longitud de la base mayor: "))
    baseMenor = int(input("Longitud de la base menor: "))
    altura = int(input("Longitud de la altura: "))
    area = calcularArea(baseMayor, baseMenor, altura)
    perimetro = calcularPerimetro(baseMayor, baseMenor, altura)
    print("Area: %.2f" % area)
    print("Perimetro: %.2f" % perimetro)
main()