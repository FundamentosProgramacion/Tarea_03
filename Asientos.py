# encoding: UTF-8
# Sebastian Morales Martin
# Asientos, calcula el numero de boletos de las 3 clases posibles

def calcularPago(asientosA, asientosB, asientosC): #calcula el precio por clasificacion de asientos y los suma en total
    totA = asientosA * 870
    totB = asientosB * 650
    totC = asientosC * 235
    return totA + totB + totC

def main():
    boletosA = int(input('Número de boleros de clase A: '))
    boletosB = int(input('Número de boleros de clase B: '))
    boletosC = int(input('Número de boleros de clase C: '))
    total = calcularPago(boletosA, boletosB, boletosC)
    print('TOTAL: $%10.2f' % total)

main()