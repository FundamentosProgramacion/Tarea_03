# Autor: Diana Patricia Aguilar Martínez, A01745778
# Descripcion:  Este programa calcula el perimetor y area de un trapecio
# A partir de aquí escribe tu programa

import math
def calcularArea(mayor, menor, high):
    valorArea= ((mayor + menor) * high) /2
    return valorArea


def pitagoras(high, bMayor, bMenor):
    lado= (( (bMayor - bMenor)/2)**2 + ((high)**2) )**0.5
    return lado


def calcularPerimetro(mayor, menor, ladoC):
    p= ((ladoC*2)+ menor + mayor)
    return p

def main():
    baseMayor=int(input("inserte el valor de la base mayor: "))
    baseMenor= int(input("inserte el valor de base menor: "))
    altura= int(input("inserte el valor de la altura: "))
    area= calcularArea(baseMayor, baseMenor, altura)
    c= pitagoras(altura, baseMayor, baseMenor)
    perimetro= calcularPerimetro(baseMayor, baseMenor, c)

    print ("el area del trapecio es: %.2f"% area)
    print("el perimetro del trapecio es: %.2f" % perimetro)
main()