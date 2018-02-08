#Ricardo Cornejo Lozano
#Calcula area y perimetro de un trapecio con los datos: Base Mayor, Base Menor y altura.

def calculaArea():
    a = ((baseMayor+baseMenor)/2)*altura
    return a
    
def calculaPerimetro():
    x = ((baseMayor-baseMenor)/2)
    pitagoras = ((x)**2) + (altura**2)
    x2 = (pitagoras)**(0.5)
    perimetro = ((x2*2)+baseMayor+baseMenor)
    return perimetro

def main():
    global baseMayor
    global baseMenor
    global altura
    baseMayor = int(input("Escribe la longitud de la base Mayor: "))
    baseMenor = int(input("Escribe la longitud de la base Menor: "))
    altura = int(input("Escribe la altura: "))
    total = calculaArea()
    total2 = calculaPerimetro()
    print("Area: %.2f " % (total), "\nPerimetro: %.2f" % (total2))

main()
    
