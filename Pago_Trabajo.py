# Autor: Fernando Sebastian Silva Miramontes
# Se calcula el pago de las horas normales y extra por separado y juntos de una jornada de trabajo.

def gananciaNormal(pagoPorHora, horasNormales): # Calcula el pago por las horas normales trabajadas.
    return pagoPorHora*horasNormales


def gananciaExtra(pagoPorHora, horasExtras): # Calcula el pago por las horas extras trabajadas.
    montoExtra = pagoPorHora*1.75
    return montoExtra*horasExtras


def main() :
    horasNormales = int(input("Horas normales trabajadas: "))
    horasExtras = int(input("Horas extras trabajadas: "))
    pagoPorHora = int(input("Pago por hora: "))
    pagoNormal = gananciaNormal(pagoPorHora, horasNormales)
    pagoExtra = gananciaExtra(pagoPorHora, horasExtras)
    total = pagoExtra + pagoNormal
    print("Pago normal: %.2f" % pagoNormal)
    print("Pago extra: %.2f" % pagoExtra)
    print("Pago total: %.2f" % total)

main()