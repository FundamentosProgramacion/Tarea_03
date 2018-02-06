#Autor: Jorge Mora Cárdenas
# Calcular el Área y Perímetro de un trapecio
import math

def calcularArea (baseMayor, baseMenor,altura):
    #Calcula el Area del trapecio
    Area = ((baseMayor + baseMenor) /2) * altura
    return Area

def calcularPerimetro (baseMayor, baseMenor, altura):
    #Calcula la logitud de los lados oblicuos y despues calcula el perimetro
    diferenciaBases = (baseMayor - baseMenor)/2
    pitagoras = math.sqrt((diferenciaBases)**2 + (altura)**2)
    perimetro = baseMayor + baseMenor + (pitagoras * 2)
    return perimetro


def main ():
    baseMayor = int(input("Escriba la longitud de la base mayor: "))
    baseMenor = int(input("Escriba la longitud de la base menor: "))
    altura = int(input("Escriba la altura del trapecio: "))
    area = calcularArea (baseMayor, baseMenor, altura)
    perimetro = calcularPerimetro (baseMayor, baseMenor, altura)
    print("Area: %.2f"% area)
    print("Perimetro: %.2f"% perimetro)


main()
