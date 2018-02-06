#Autor: Jorge Mora Cárdenas
# calcula el total a pagar por la compra de los boletos.

def calcularPago (asientosA, asientosB,asientosC):
    # Calcula el costo de cada asiento comprado y devuelve el total a pagar
    claseA = 870 * asientosA
    claseB = 650 * asientosB
    claseC = 235 * asientosC
    totalPago = claseA + claseB + claseC
    return totalPago


def main ():
    numeroDeBoletosA =int(input("Boletos a comprar en clase A: "))
    numeroDeBoletosB =int(input("Boletos  a comprar en clase B: "))
    numeroDeBoletosC =int(input("Boletos a comprar en clase C: "))
    totalPago = calcularPago(numeroDeBoletosA, numeroDeBoletosB, numeroDeBoletosC)
    print("El costo total a pagar es de: $%.2f "% totalPago)




main()
