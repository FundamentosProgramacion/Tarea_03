#Carlos Ochoa
#Calcula el pago normal, extra y total de un trabajador debido a sus horas

#Calcula el pago normal
def pagoNormal(pagoN, pagoH):
    pagoN=pagoN*pagoH
    return (pagoN)

#Calcula el pago extra
def pagoExtra(pagoE, pagoH):
    pagoE=pagoE*pagoH
    return pagoE


def main():
    pagoN=int(input("Teclea las horas normales trabajadas: "))
    pagoE=int(input("Teclea las horas extras trabajadas: "))
    pagoH=int(input("Teclea el pago por hora: "))
    pagoHN=pagoNormal(pagoN, pagoH)
    pagoHE=pagoExtra(pagoE, pagoH)
    pagoT=pagoHN+pagoHE

    print("Pago normal: %.2f" %pagoHN)
    print("Pago extra: %.2f" %pagoHE)
    print("Pago total: %.2f" %pagoT)

main()
