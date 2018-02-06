# Autor: Diana Patricia Aguilar Martínez, A01745778
# Descripcion:  Este programa calcula el pago total de un trabajador
# A partir de aquí escribe tu programa


def rendimientoK(km, gasolinaL):
    gasKM= km/gasolinaL
    return gasKM


def rendimientoM(kilometros, gasoL):
    millas= kilometros * 1.6093
    galones= gasoL * 0.264
    gasGM= millas / galones
    return gasGM


def main():
    km=int(input("Teclee el numero de kilometros recorridos: "))
    gasolinaL=int(input("Teclee el numero de litros de gasolina gastados: "))
    rendimientoKM= rendimientoK(km, gasolinaL)
    rendimientoMG= rendimientoM(km, gasolinaL)
    print("                           ")

    print ("El rendimiento de su auto en km/L es de: %.2f"% rendimientoKM, "km/L")

    print ("El rendimiento de su auto en millas/ galon es de: %.2f" % rendimientoMG, "mi/gal"+ )

    print("                           ")
    distancia= int(input("¿Cuantos kilometros va a recorrer? "))
    litrosDistancia= (distancia *gasolinaL)/ km
    print("                           ")
    print("Para recorrer", distancia, "KM se necesitan: %.2f"%litrosDistancia, "litros" )
main()
