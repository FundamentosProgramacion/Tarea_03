#Autor: Nataly Paulina Lopez Salazar
#Descripcion: Se va calcular area y perimetro del trapecio.

def calcularArea(baseM, basem, altura): #Calcula el area del trapecio
    a = ((baseM+basem)*altura)/2
    return a


def calcularPeri(baseM, basem, altura): #Calcula el perimetro del trapecio
    p = baseM + basem + (2*altura)
    return p


def main():
    baseM = int(input("Longitud de la base mayor: "))
    basem = int(input("longitud de la base menor: "))
    altura = int(input("Longitud de la altura: "))

    area = calcularArea(baseM,basem,altura)
    peri = calcularPeri(baseM,basem,altura)

    print("Area: %.2f"%area)
    print("Perimetro: %.2f"%peri)

main()