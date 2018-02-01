# Autor: Fernando Sebastian Silva Miramontes
# Se calcula el pago de un trabajo

def gananciaNormal(pagoPorHora, horasNormales):
    return pagoPorHora*horasNormales


def gananciaExtra(pagoPorHora, horasExtras):
    ganacia = pagoPorHora*1.75
    return ganacia*horasExtras


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