#Autor: Guillermo Adrian Urbina Aguiñiga
#Calcula el redimiento de un auto en Km y Millas


def KmporL(Km, L):
    KmL = Km / L
    return KmL
#Función para calcular la eficiencia en Km por Litro

def MiporGal(Km, L):
    MiGal = ((Km / 1.6093) / (L * 0.264))
    return MiGal
#Función para calcular la eficiencia en Millas por Galón

def main():
    Km = int(input("Introduce el número de km recorridos: "))
    L = int(input("Introduce el número de litros de gasolina usados: "))
    print("Si recorres ", Km , " con ", L , " litros de gasolina, el rendimiento es: ")
    print(KmporL(Km, L), " Km/l")
    print(MiporGal(Km, L), "Mi/gal")
    Recorrer = int(input("¿Cuantos kilómetros vas a recorrer?: "))
    Litros = Recorrer / (KmporL(Km, L))
    print("Para recorrer ", Recorrer, " necesitas ", Litros, " Litros de gasolina" )

main()