#Autor: Karla Fabiola Ramirez Martinez
#Calcula el area de un trapecio


#Primero importamos la libreria Math
import math
#Se define la funcion de area
def funcionarea(bm,bM,h):
    area= ((bm+bM)/2)*h
    return area
#Se define la funcion de diametro
def funciondiametro(bm,bM,h):
    diferencia=(bm-bM)/2
    c=math.sqrt(((diferencia**2)+(h**2)))
    diametro=2*c+bm+bM
    return diametro
#Funcion principal
def main():
    bmayor=int(input("Dime la base mayor: "))
    bmenor=int(input("Dime la base menor: "))
    altura=int(input("Dime la altura: "))
    area=funcionarea(bmayor,bmenor,altura)
    diametro=funciondiametro(bmayor,bmenor,altura)
    print("Tiene un area de: %.2f"%area)
    print("Tiene un diametro de: %.2f"%diametro)



main()