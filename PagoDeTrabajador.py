#Autor: Nataly Paulina Lopez Salazar
#Descripcion: Se va calcular el pago semanal de un trabajador por horas, incluyendo horas extras.

def calcularNormal(horasN, pago): #Calcula el valor de las horas trabajadas normalmente por su costo por hora
    normal = horasN*pago
    return normal


def calcularExtras(horasE, pago): #Calcula el valor de las horas extras trabajadas por el 75% mas del costo normal
    extras = pago*1.75*horasE
    return extras


def main():
    horasN = int(input("Numero de horas trabajadas: "))
    horasE = int(input("Numero de horas extras trabajadas: "))
    pago = int(input("Pago por hora: "))

    pagoNormal = calcularNormal(horasN,pago)
    pagoExtra = calcularExtras(horasE,pago)
    pagoTotal = pagoNormal + pagoExtra

    print("\nPago Normal: $%.2f"%pagoNormal)
    print("Pago Extras: $%.2f"%pagoExtra)
    print("Pago Total: $%.2f"%pagoTotal)

main()