#encoding: UTF-8
#Jean Paul Esquivel Lobato
#Calcular el área y perímetro de un trapecio

#Llama de la libreria math la función para resolver raices
from math import sqrt

#Función para realizar el área
def calcularArea(bMayor, bMenor, h):
    area = ((bMayor + bMenor) * h )/2                                 #Calcula la operación para sacar el área
    return area                                                       #Regresa el valor de área

#Función para realizar el perímetro
def calcularPerimetro (bM, bm, h):
    x = (bM - bm)/2                                                    #Calcula la base del triangulo
    l = sqrt(x**2 + h**2)                                              #Calcula la hipotenusa del triangulo
    perimetro = bM + bm + (2*l)                                        #Realiza la operación para sacar el perímetro
    return perimetro                                                   #Regresa el valor del perímetro

#Función principal
def main():
    baseMayor = int(input("Escribe la longitud de la base mayor: "))   #Pide al usuario la base mayor
    baseMenor = int(input("Escribe la longitud de la base menor: "))   #Pide al usuario la base menor
    altura = int(input("Escribe la altura: "))                         #Pide al usuario la altura
    area = calcularArea (baseMayor, baseMenor, altura)                 #llama a la funcion calcularArea
    perimetro = calcularPerimetro (baseMayor, baseMenor, altura)       #llama a la funcion calcularArea
    print("Área: %.2f " % area)                                        #Imprime el resultado de Área
    print("Perímetro: %.2f " % perimetro)                              #Imprime el resultado de Perímetro

#Llama a la función principal
main()