#Mirna Zertuche Calvillo A01373852
#Un programa que calcula el pago semanal de un trabajador dado el pago por hora, el numero de horas y en su caso horas extras

def pagoHorasN(horas,pagoHora):
    pH= horas* pagoHora
    return pH

def  pagoHorasE(horasE,pagoHora):
    pagoHoraE= pagoHora+ pagoHora*.75
    pHE = horasE*pagoHoraE
    return pHE

def main():
    horas = float(input("Teclea las horas normales trabajadas: "))
    horasE = float(input("Teclea las horasextras trabajadas: "))
    pagoHora = float(input("Teclea el pago por hora: "))
    pagoHN = pagoHorasN(horas,pagoHora)
    pagoHE = pagoHorasE(horasE,pagoHora)
    pagoTotal= pagoHN+pagoHE
    print("Pago normal: $%.2f" % pagoHN)
    print("Pago extra: $%.2f" % pagoHE)
    print("------------------------")
    print("Pago total: %.2f" % pagoTotal)

main()