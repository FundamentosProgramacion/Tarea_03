# encoding: UTF-8
#Autor: Genaro Ortiz Durán
#Descripción:Crear programa que calcule el área y perímetro de un trapecio.

from math import sqrt

#Calcula el área a través de la división de la suma de las dos y resultado multiplicandolo por la altura.
def calcularArea(lM, lm, h):
    area=((lM+lm)/2)*h
    return area

#Calcula el perímetro a través de la división entre dos de la resta del lado mayor menos el lado menor. Aplicando el teorema de Pitágoras se saca la raíz cuadrada del resultado anterior al cuadrado más la altura al cuadrado. Al resultado de la raíz se multiplica por dos y  se le suma los lados del trapecio.
def calcularPerimetro(lM, lm, h):
    resultante=(lM-lm)/2
    lados=sqrt((h**2)+(resultante**2))
    perimetro=lados*2+lm+lM
    return perimetro



def main():
    lM=float(input("Escribe la longitud del lado mayor:"))
    lm = float ( input ( "Escribe la longitud del lado menor:" ) )
    h=float(input("Escribe la altura:"))

    print("El área del trapecio es:",format(calcularArea(lM,lm,h),".2f"))
    print("El perímetro es:",format(calcularPerimetro(lM,lm,h),".2f"))



main()