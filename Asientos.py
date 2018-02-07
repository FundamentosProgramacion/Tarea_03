#Mirna Zertuche Calvillo A01373852
#Un programa que de acuerdo a la cantidad y tipos de asiento calcula el total a pagar de la compra


def calcularPago(A,B,C):
    TotalA= A*870
    TotalB = B*650
    TotalC = C*235
    totalPago = TotalA+TotalB+TotalC
    return( totalPago)

def main():
    A = int(input("Número de asientos clase A: "))
    B = int(input("Número de asientos clase B: "))
    C = int(input("Número de asientos clase C: "))
    totalPago= calcularPago(A,B,C)
    print("El costo total es: $%.2f" % totalPago)



main()
