# Autor: Andrés Reyes Rangel.
# Calcular el pago de un trabajador.

def calcularPagoNormal(hNormales, pago):
    normal = hNormales*pago
    return normal

def calcularPagoExtra(hExtras, pago):
    a = (pago*0.75)+pago
    extra = hExtras * a
    return extra

def main():
    hNormales = int(input("Teclea las horas normales trabajadas: "))
    hExtras = int(input("Teclea las horas extras trabajadas: "))
    pago = int(input("Teclea el pago por hora: "))
    pagoNormal = calcularPagoNormal(hNormales, pago)
    pagoExtra = calcularPagoExtra(hExtras, pago)
    total = pagoNormal+pagoExtra
    print("Pago normal: $%.2f" % pagoNormal)
    print("Pago extra: $%.2f" % pagoExtra)
    print("Pago total: $%.2f" % total)
main()