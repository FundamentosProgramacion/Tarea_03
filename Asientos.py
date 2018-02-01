# Autor: Fernando Sebastian Silva Miramontes
# Calcular asientos de un ensayo.

def calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC):
    total = (numeroBoletosA*870) + (numeroBoletosB*650) + (numeroBoletosC*235)
    return total


def main() :
    numeroBoletosA = int(input("Cuantos asientos A?\n"))
    numeroBoletosB = int(input("Cuantos asientos B?\n"))
    numeroBoletosC = int(input("Cuantos asientos C?\n"))
    total = calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC)
    print("Se va a pagar un total de: $",total)

main()
