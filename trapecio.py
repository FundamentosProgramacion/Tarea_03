##Autor: David Medina  A01653311
##Calcular area de trapecio
import math

##Esta funcion calcula el area del trapecio
def calcularArea(bMa,bMe,h):
    area = ((bMa+bMe)/2*h)
    return area

##Esta funcion calcula el perimetro del trapecio
def calcularPerimetro(bMa,bMe,h):
    s = (bMa-bMe)/2
    perimetro = bMe + bMa + math.sqrt(h**2+s**2)*2
    return perimetro

##funcion principal
def main():
    baseMayor =  int(input("Ingresar base mayor: "))
    baseMenor =  int(input("Ingresar base menor: "))
    altura =  int(input("Ingresar altura: "))
    area = calcularArea(baseMayor, baseMenor, altura)
    perimetro = calcularPerimetro(baseMayor, baseMenor, altura)
    print ("Area: %.2f" % area)
    print ("Perimetro: %.2f" % perimetro)

main()