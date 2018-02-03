#Jossian Abimelec García Quijano
#Calcula el pago para un trabajador dadas las horas


def calcularPago(horasnormales, pagohora):
    pago = horasnormales*pagohora
    return pago


def calcularPagoextra(horasextras, pagohora):
    pagoextra = (horasextras*pagohora)*1.75
    return pagoextra


def main():
    horasnormales = int(input("Teclea en número de horas normales trabajadas: "))
    horasextras = int(input("Teclea en número de horas extras trabajadas: "))
    pagohora = int(input("Teclea el pago por hora: "))
    pago = calcularPago(horasnormales, pagohora)
    pagoextra = calcularPagoextra(horasextras, pagohora)
    print("Pago normal: $%.2f"%pago)
    print("Pago extra: $%.2f" % pagoextra)
    print("Pago total: $%.2f"%(pago+pagoextra))
main()