## Autor: David Medina A01653311
## Calcular precio de asientos de estadio.

##Esta funcion calcula el total a pagar de los asientos
def calcularPago(asientosA, asientosB, asientosC):
    precioAsientosA = asientosA * 870
    precioAsientosB = asientosB * 650
    precioAsientosC = asientosC * 235
    totalPago = precioAsientosA + precioAsientosB + precioAsientosC
    return totalPago

##funcion principal
def main():
    numeroBoletosA = int(input("Ingrese numero de asientos seccion A: "))
    numeroBoletosB = int(input("Ingrese numero de asientos seccion B: "))
    numeroBoletosC = int(input("Ingrese numero de asientos seccion C: "))
    precioFinal = calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC)

    print ("El costo total es de: $ %.2f"% precioFinal)

main()


