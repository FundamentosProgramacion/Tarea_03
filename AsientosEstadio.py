#encoding: UTF-8
#Jean Paul Esquivel Lobato
#Calcular el pago de la compra de boletos del estadio

#Función Secundaría
def calcularPago(asientoA, asientoB, asientoC):                                          #Realiza la operación para regresar el valor a la función principal
    aA = asientoA * 870                                                                  #Calcula la cantidad por los asientos A
    aB = asientoB * 650                                                                  #Calcula la cantidad por los asientos B
    aC = asientoC * 235                                                                  #Calcula la cantidad por los asientos C
    total = aA + aB + aC                                                                 #Calcula la cantidad a pagar por todos los asientos
    return total                                                                         #Regresa el valor de calcularPago

#Función Principal
def main():
    numeroBoletosA = int(input("Número de boletos A: "))                                 #Pide al usuarui el número de boletos A
    numeroBolestosB = int(input("Número de boletos B: "))                                #Pide al usuarui el número de boletos B
    numerosBoletosC = int(input("Número de boletos C: "))                                #Pide al usuarui el número de boletos C
    costoTotal = calcularPago(numeroBoletosA, numeroBolestosB, numerosBoletosC)          #Llama a la funcion calcularPago para recibir el resultado
    print ("El costo total es: $%.2f " % costoTotal)                                     #Imprime el resultado del costo total

#Llama a la función principal
main()