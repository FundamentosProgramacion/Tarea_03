#Jossian Abimelec García Quijano
#Calcula el pago para un trabajador de horas y horas extras dadas las horas y el pago por horas


def calcularPago(horasnormales, pagohora):
    pago = horasnormales*pagohora
    return pago


def calcularPagoextra(horasextras, pagohora):
    pagoextra = (horasextras*pagohora)*1.75
    return pagoextra


def main():
    horasnormales = int(input("Teclea las horas normales trabajadas: "))
    horasextras = int(input("Teclea las horas extras trabajadas: "))
    pagohora = int(input("Teclea el pago por hora: "))
    pago = calcularPago(horasnormales, pagohora)
    pagoextra = calcularPagoextra(horasextras, pagohora)
    print("Pago normal: $%.2f"%pago)
    print("Pago extra: $%.2f" % pagoextra)
    print("Pago total: $%.2f"%(pago+pagoextra))
main()