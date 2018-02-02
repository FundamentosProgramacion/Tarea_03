#Jossian Abimelec García Quijano
#Encuentra el area de un trapecio

from math import sqrt

def calcularArea(basemenor, basemayor, altura):
    area=((basemenor+basemayor)/2)*altura
    return area


def calcularPerimetro(basemenor, basemayor, altura):
    perimetro = (sqrt(((basemayor-basemenor)/2)**2+altura**2))*2+basemenor+basemayor
    return perimetro

def main():
    basemayor = int(input("Teclea el valor de la base mayor: "))
    basemenor = int(input("Teclea el valor de la base menor: "))
    altura = int(input("Teclea el valor de la altura: "))
    area = calcularArea(basemenor, basemayor, altura)
    perimetro = calcularPerimetro(basemenor, basemayor, altura)
    print("Area: %.2f"%area)
    print("Perimetro: %.2f" % perimetro)

main()