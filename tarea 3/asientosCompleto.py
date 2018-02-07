# Autor: Diana Patricia Aguilar Martínez, A01745778
# Descripcion:  Este programa calcula el total de tu compra por unos boletos
# A partir de aquí escribe tu programa

def totalA(asientosA):
    pagoA= asientosA * 870
    return pagoA


def totalB(asientosB):
    pagoB = asientosB * 650
    return pagoB


def totalC(asientosC):
    pagoC = asientosC * 235
    return pagoC



def main():
    boletosA= int(input("¿cuantos boletos vas a comprar de la clase A? "))
    boletosB= int(input("¿cuantos boletos vas a comprar de la clase B? "))
    boletosC= int(input("¿cuantos boletos vas a comprar de la clase C? "))

    totalPago= totalA(boletosA) + totalB(boletosB)+ totalC(boletosC)

    print ("Su total de pago es de: $%.2f"% totalPago)

main()