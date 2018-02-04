#Autor: Jossian Abimelec García Quijano
#calcula el valor a pagar a partir de la clase de los asientos que quiere comprar

def calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC):
    pago=numeroBoletosA*870+numeroBoletosB*650+numeroBoletosC*235
    return pago



def main():
    numeroBoletosA = int(input("Número de boletos de clase A: "))
    numeroBoletosB = int(input("Número de boletos de clase B: "))
    numeroBoletosC = int(input("Número de boletos de clase C: "))
    pago=calcularPago(numeroBoletosA,numeroBoletosB,numeroBoletosC)
    print("el costo total es: $%.2f "%pago)

main()