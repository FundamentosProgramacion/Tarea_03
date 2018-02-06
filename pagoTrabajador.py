#Autor: Jorge Mora Cardenas
# Calcular el pago de un trabajador

def calcularPagoNormal (horasNormales,costoHora):
    #Calcula el pago por horas normales trabajadas
    pagoNormal = horasNormales * costoHora
    return pagoNormal

def calcularPagoExtra (HorasExtra, costoHora):
    #Calcula el 75% por hora extra y el pago por el totl de horas extras trabajadas.
    porcentaje = costoHora * 0.75
    costoExtra = costoHora + porcentaje
    pagoExtra = HorasExtra * costoExtra
    return pagoExtra

def main ():
    horasNormales = int(input("teclea las horas normales trabajadas: "))
    horasExtras = int(input("teclea las horas extras trabajadas: "))
    costoHora = int(input("Teclea el pago por hora: "))
    pagoNormal = calcularPagoNormal (horasNormales,costoHora)
    pagoExtra = calcularPagoExtra (horasExtras,costoHora)
    pagoTotal = pagoNormal + pagoExtra
    print("Pago Normal: $%.2f"% pagoNormal)
    print("Pago por horas Extras: $%.2f"% pagoExtra)
    print("-------------------------------")
    print("pago total: $%.2f"% pagoTotal)

main()
