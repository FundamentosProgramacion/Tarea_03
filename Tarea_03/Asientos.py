#Carlos Ochoa
#Calcula el total a pagar por unos asientos determinando el tipo de asiento


#Calcula el pago total de los asientos

def calcularPago(asientosA, asientosB, asientosC):
    pagoA=asientosA*870
    pagoB=asientosB*650
    pagoC=asientosC*235
    totalPago=pagoA+pagoB+pagoC

    return totalPago


def main():
    numBA=int(input("cuantos boletos a se vendieron: "))
    numBB=int(input("cuantos boletos b se vendieron: "))
    numBC=int(input("cuantos boletos c se vendieron: "))
    pagoT=calcularPago(numBA, numBC, numBC )

    print ("total a pagar: %.2f" % pagoT)

main()