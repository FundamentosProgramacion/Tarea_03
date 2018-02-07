#Autor : Karla Fabiola Ramirez Martinez
#Calcula pago de trabajador



def pagoN(x,pago):
    pagoNORMAL=float(x*pago)
    return pagoNORMAL


def pagoE(x,pago):
    extra=float(x*(1.75*pago))
    return extra

#RECUERDA PASARLO A FLOTANTE/Preguntar porque no te sale en flotante

def main():
    normal=float(input("Horas normales: "))
    extra=float(input("Horas extra: "))
    pago=float(input("Pago por hora: "))
    pnormal=pagoN(normal,pago)
    pextra=pagoE(extra,pago)
    total=float(pnormal+pextra)
    print("Pago normal: $%.2f"%pnormal)
    print("Pago extra: $%.2f"%pextra)
    print("--------------------------")
    print("Pago total: $%.2f"%total)




main()
