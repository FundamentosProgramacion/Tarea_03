# encoding: UTF-8
# Sebastian Morales Martin
# Calculo del pago de un trabajador

def calcularPagoNor(horas, sueldo): #calcula el pago por horas normal
    pago = horas * sueldo
    return pago

def calcularPagoEx(horas, sueldo): # calcula el pago por hora extra trabajada
    pago = (horas * sueldo)*1.75
    return pago

def main():
    hNormales = int(input("Teclea las horas normales trabajadas: "))
    hExtra = int(input("Teclea las horas extras trabajadas: "))
    pPorHora = int(input("Teclea el pago por hora: "))
    pagoNormal = calcularPagoNor(hNormales, pPorHora)
    pagoExtra = calcularPagoEx(hExtra, pPorHora)
    pagoTotal = pagoNormal + pagoExtra
    print("Pago normal: $%.2f\nPago extra: %.2f\n-----------------------\nPago total: $%.2f" % (pagoNormal, pagoExtra, pagoTotal))


main()
