# encoding: UTF-8
# Sebastian Morales Martin
# Asientos, calcula el numero de boletos de las 3 clases posibles

def calcularPago(asientosA, asientosB, asientosC):
    totA = asientosA * 870
    totB = asientosB * 650
    totC = asientosC * 235
    return totA + totB + totC

def main():
    boletosA = int(input('Número de boleros clase A: '))
    boletosB = int(input('Número de boleros clase B: '))
    boletosC = int(input('Número de boleros clase C: '))
    total = calcularPago(boletosA, boletosB, boletosC)
    print('TOTAL: $%10.2f' % total)

main()