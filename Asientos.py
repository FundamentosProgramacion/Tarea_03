#Autor: Karla Fabiola Ramirez Martinez
#Total precio de boletos

def calcularPago(asientosA,asientosB,asientosC):
    a=asientosA*870
    b=asientosB*650
    c=asientosC* 235
    totalPago=a+b+c
    return totalPago


def main():
    numeroBoletosA=int(input("Dame el numero de asientos en A: "))
    numeroBoletosB = int(input("Dame el numero de asientos en B: "))
    numeroBoletosC = int(input("Dame el numero de asientos en C: "))
    total=calcularPago(numeroBoletosA,numeroBoletosB,numeroBoletosC)
    print("El costo total es: $%.2f"%total)



main()
