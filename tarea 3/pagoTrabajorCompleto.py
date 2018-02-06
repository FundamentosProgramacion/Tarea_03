# Autor: Diana Patricia Aguilar Martínez, A01745778
# Descripcion:  Este programa calcula el pago total de un trabajador
# A partir de aquí escribe tu programa


def pagoHorasN(normal, pagoH):
    horasN= normal*pagoH
    return horasN


def pagoHorasE(extra, pagoH):
    horasE= extra*(pagoH +(pagoH*0.75))
    return horasE

def main():
    pagoNormal= int(input("Teclee las horas normales trabajadas:  "))
    pagoExtra=int(input("teclee las horas extras trabajadas: "))
    pago= int(input("teclee el pago por hora: "))
    pagoHN= pagoHorasN(pagoNormal, pago )
    pagoHE= pagoHorasE(pagoExtra, pago )
    pagoTotal= pagoHN + pagoHE

    print ("                           ")
    print ("Pago normal: $%.2f"% pagoHN)
    print("Pago extra: $%.2f" % pagoHE)
    print ("---------------------------")
    print ("Pago total es de: $%.2f"% pagoTotal)

main()
