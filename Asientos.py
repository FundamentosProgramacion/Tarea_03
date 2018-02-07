#Autor: Nataly Paulina Lopez Salazar
#Descripcion: Se va calcular el costo total de tres tipos de asientos.

def calcularTotal(asientosA, asientosB, asientosC): #Calcula el numero de asientos por su costo para al final dar el costo total de asinetos
    boletosA = asientosA*870
    boletosB = asientosB*650
    boletosC = asientosC*235

    pago = boletosA + boletosB + boletosC

    return pago

def main():
    asientosA = int(input("Numero de asientos del tipo A: "))
    asientosB = int(input("Numero de asientos del tipo B: "))
    asientosC = int(input("Numero de asientos del tipo C: "))
    total = calcularTotal(asientosA, asientosB, asientosC)
    print("El costo total es: $%.2f"%total)
main()