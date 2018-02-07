# encoding: UTF-8
# Sebastian Morales Martin
# Medida de el trapecio
import math as mat

def calcularArea(bMayor, bMenor, altura): #calcula el area del trapecio
    area = ((bMayor + bMenor)/2)*altura
    return area

def calcularDiametro(bMayor, bMenor, altura): # calcula el diametro del trapecio
    a = bMayor - bMenor
    hip = mat.sqrt((a*a)+(altura*altura))
    diametro = bMayor + bMenor + (hip*2)
    return diametro







def main():
    bMayor = int(input("Escribe la longitud de la base mayor: "))
    bMenor = int(input("Escribe la longitud de la base menor: "))
    altura = int(input("Escribe la altura: "))
    area = calcularArea(bMayor, bMenor, altura)
    diametro = calcularDiametro(bMayor, bMenor, altura)
    print("Área: %10.2f\nPerímetro: %10.2f" % (area, diametro))


main()
