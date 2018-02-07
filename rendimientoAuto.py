#Mirna Zertuche Calvillo A01373852
#Un programa que calcula el rendimiento de kilometros por litro de gasolina, lo transforma a millas por galon y calcula cuantos litros se necesitan para ciertos kilometros

def KmporLitro(Km,Lt):
    Kxl=Km/Lt
    return Kxl

def MiporGalon(Km,Lt):
    KaM= Km/1.6093
    LaG= Lt*0.264
    MxG= KaM/LaG
    return MxG

def LitrosRecorrer(kl,Kmr):
    LxR= Kmr/kl
    return LxR

def main():
    Km = int(input("Teclea el número de km recorridos: "))
    Lt = int(input("Teclea el número de litros de asolina usados: "))
    kl= KmporLitro(Km,Lt)
    mg= MiporGalon(Km,Lt)
    print("Si reorres",Km,"Kms con",Lt,"litros de gasolina, el rendimiento es:")
    print("%.2f" %kl,"km/l")
    print("%.2f" %mg,"mi/gal")
    Kmr = int(input("¿cuántos kilómetros vas a recorrer? "))
    Ltn = "%.2f" %LitrosRecorrer(kl,Kmr)
    print("Para recorrer",Kmr,"km necesitas",Ltn,"litros de gasolina")

main()