# Autor: Carlos Martínez Rodríguez
# Descripción: Calcular el área de un trapecio dados la base mayor, la base menor y la altura de un trapecio

# Función para calcular el área del trapecio
def calcularArea(baseMayor, baseMenor, altura):
    totalArea = ((baseMayor + baseMenor) * altura) / 2
    return totalArea

# Función para calcular el perímetro del trapecio
def calcularPerimetro(baseMayor, baseMenor, altura):
    l = (baseMayor - baseMenor) / 2
    h = (altura**2 + l**2)**.5
    totalPerimetro = baseMayor + baseMenor + (h*2)
    return totalPerimetro


def main():
    # Entradas del usuario (medidas)
    baseMayor = int(input("Escribe la longitud de la base mayor: "))
    baseMenor = int(input("Escribe la longitud de la base menor: "))
    altura = int(input("Escribe la altura: "))
    # Calcular área y perímetro del trapecio
    area = calcularArea(baseMayor, baseMenor, altura)
    perimetro = calcularPerimetro(baseMayor, baseMenor, altura)
    # Imprimir resultados
    print("Área: %.2f" % area)
    print("Perímetro: %.2f" % perimetro)

main()