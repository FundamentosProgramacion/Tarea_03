# Autor: Fernando Sebastian Silva Miramontes
# Calcular el precio que se pagara en la compra de asientos que estan a diferentes precios.

def calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC):  # Se calcula el total a pagar dependiendo de la cantidad y tipo de boletos que se compren.
    total = (numeroBoletosA*870) + (numeroBoletosB*650) + (numeroBoletosC*235)
    return total


def main() :
    numeroBoletosA = int(input("Cuantos asientos A?\n"))
    numeroBoletosB = int(input("Cuantos asientos B?\n"))
    numeroBoletosC = int(input("Cuantos asientos C?\n"))
    total = calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC)
    print("Se va a pagar un total de: $%i" %  total)

main()
