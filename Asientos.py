#Autor: Jossian Abimelec García Quijano
#calcula el valor a pagar a partir de los asientos


def calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC):
    pago=numeroBoletosA*870+numeroBoletosB*650+numeroBoletosC*235
    return pago



def main():
    numeroBoletosA = int(input("Teclea el número de asientos clase A: "))
    numeroBoletosB = int(input("Teclea el número de asientos clase B: "))
    numeroBoletosC = int(input("Teclea el número de asientos clase C: "))
    pago=calcularPago(numeroBoletosA,numeroBoletosB,numeroBoletosC)
    print("el costo total es: $%.2f "%pago)

main()