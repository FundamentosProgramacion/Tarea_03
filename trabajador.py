#encoding: UTF-8
#Jean Paul Esquivel Lobato
#Calcular el pago semanal de un trabajador

#Función para realizar el pago rormal
def calcularPagoNormal(hNormales, pHora):
    return hNormales * pHora                                               #Realiza la operación y regresa el valor de calcularPagoNormal

#Función para realizar el pago rormal
def calcularPagoExtra( hExtras, pHora):
    extras = hExtras * pHora                                               #Calcula el valor de las horas extras sin el porcentaje
    e = extras * .75                                                       #Calcula el porcentaje de las horas extras
    totalPagoExtra = extras + e                                            #Suma el valor y el porcentaje
    return totalPagoExtra                                                  #Regresa el valor de calcularPagoEstra

#Función principal
def main():
    horasNormales = int(input("Teclea las horas normales trabajadas: "))   #Pide al usuario las horas normales
    horasExtras = int(input("Teclea las horas extras trabajadas: "))       #Pide al usuario las horas extras
    pagoHora = int(input("Teclea el pago por hora: "))                     #Pide al usuario el pago por hora
    pagoNormal = calcularPagoNormal (horasNormales, pagoHora)              #Llama a la función calcularPagoNormal
    pagoExtra = calcularPagoExtra(horasExtras, pagoHora)                   #Llama a la función calcularPagoExtra
    pagoTotal = pagoNormal + pagoExtra                                     #Calcula el pago total
    print("Pago normal: $%.2f" % (pagoNormal))                             #Imprime el pago normal
    print("Pago extra: $%.2f" % (pagoExtra))                               #Imprime el pago extra
    print("----------------------")
    print("Pago Total: $%.2f" % (pagoTotal))                               #Imprime el pago total

#Llama a la función main
main()
