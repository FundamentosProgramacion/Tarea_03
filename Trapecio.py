#Autor: Guillermo Adrian Urbina Aguiñiga
# Programa para calcular el area y perimetro de un trapecio

import math

def Area(BaseM,Basem,Altura):
    AreaT = ((BaseM + Basem) / 2) * Altura
    return AreaT
# Función para calcular el area total

def Perimetro(BaseM,Basem,Altura):
    PerimetroT = (BaseM + Basem + (2*(math.sqrt((((BaseM - Basem)**2) + Altura**2)))))
    return PerimetroT
#Función para sacar el perimetro total

def main():
    BaseM = int(input("Escribe la longitud de la base mayor: "))
    Basem = int(input("Escribe la longitud de la base menor: "))
    Altura = int(input("Escribe la longitud de la altura: "))
    AreaFinal = Area(BaseM,Basem,Altura)
    PerimetroFinal = Perimetro(BaseM,Basem,Altura)
    print("Perimetro es: ", AreaFinal)
    print("Area es: ", PerimetroFinal)

main()









