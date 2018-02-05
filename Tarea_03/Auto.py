#Carlos Ochoa
#Calcular los kilometros sobre litro y las millas sobre galones que un auto puede recorrer

#Calcula los kilometros sobre litro
def KiloMetrosL(KMR, LGU):
    RenK=KMR/LGU
    return RenK

#Calcula las millas sobre galones
def MillasG(KMR, LGU):
    Millas = KMR * 0.621
    Galones = LGU * 0.264
    RenG = Millas / Galones
    return RenG



def main():
    KMR=int(input("Teclea el numero de kilometros recorridos: "))
    LGU=int(input("Teclea los litros de gasolina usados: "))
    KmL=KiloMetrosL(KMR, LGU)
    MiGal=MillasG(KMR, LGU)

    print ("%.2f" % KmL, "KM/Litros")
    print ("%.2f" % MiGal, "Millas/Galon")


main()

