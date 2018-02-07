#Autor: Guillermo Adrian Urbina Aguiñiga
#Programa para calcular el salario total de un trabajador

def PagoNormal(HorasNormales, PagoHora):
    PagoNT = HorasNormales * PagoHora
    return PagoNT
#Función para calcular el pago de horas normales

def PagoExtra(HorasExtras, PagoHora):
    PagoET = HorasExtras * (PagoHora + (PagoHora * 0.75))
    return PagoET
#Función para calcular el pago de horas extras

def main():
    HorasNormales = int(input("Horas normales trabajadas: "))
    HorasExtras = int(input("Horas extra trabajadas: "))
    PagoHora = int(input("Pago por horas: "))
    PNT = PagoNormal(HorasNormales, PagoHora)
    PET = PagoExtra(HorasExtras, PagoHora)
    print("El pago normal es: ", PNT)
    print("El pago extra es: ", PET)
    print("El pago total es: ", PNT + PET)
#Función para resolver el problema

main()