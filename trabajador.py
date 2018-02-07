##Autor: David Medina A01653311
##Calcular pago de un trabajador

##Esta funcion calcula el pago de horas normales
def calcularPagoNormal(hN,pG):
    normal = hN * pG
    return normal

##Esta funcion calcula el pago de horas extra
def calcularPagoExtra(hE,pG):
    extra = hE*pG*1.75
    return extra

##Funcion principal
def main():
    hNormales = int(input("Ingresar horas normales trabajadas: "))
    hExtras = int(input("Ingresar horas extras trabajadas: "))
    pagoHora = int(input("Ingresar pago por hora del trabajador: "))
    pagoN = calcularPagoNormal(hNormales,pagoHora)
    pagoE = calcularPagoExtra(hExtras, pagoHora)
    pagoTotal = pagoN + pagoE
    print ("Pago normal: $ %.2f" % pagoN)
    print ("Pago extra: $ %.2f" % pagoE)
    print ("Pago total : $ %.2f" % pagoTotal)

main()
