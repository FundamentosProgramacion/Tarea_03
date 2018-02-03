# Autor: Andrés Reyes Rangel.
# Calcular área y diámetro de un trapecio isoceles.

import math

def calcularArea(baseMayor, baseMenor, altura):
    a = ((baseMayor + baseMenor) / 2) * altura
    return a

def calcularPerimetro(baseMayor, baseMenor, altura):
    c = (baseMayor-baseMenor)/2
    p = baseMenor + baseMayor + 2*( math.sqrt(altura**2 + c**2) )
    return p

def main():
    baseMayor = int(input("Escribe la longitud de la base mayor: "))
    baseMenor = int(input("Escribe la longitud de la base menor: "))
    altura = int(input("Escribe la altura: "))
    area = calcularArea(baseMayor, baseMenor, altura)
    perimetro = calcularPerimetro(baseMayor,baseMenor, altura)
    print("Área: %.2f" % area)
    print("Perimetro: %.2f" % perimetro)
main()