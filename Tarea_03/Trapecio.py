#Carlos Ochoa
#Calcula el area y el perimetro de un trapecio isoceles

#Calcula el area
def Atrapecio(lonBMen, lonBMay, h):
    area=((lonBMay+lonBMen)/2)*h
    return area

#Calcula el perimetro
def Ptrapecio(lonBMen, lonBMay, h):
    perimetro=lonBMay+lonBMen+(2*h)
    return perimetro

def main():
    baseMen=int(input("Escribe la base menor: "))
    baseMay=int(input("Escribe la base mayor: "))
    altura=int(input("Escribe la altura: "))
    area=Atrapecio(baseMen, baseMay, altura)
    perimetro=Ptrapecio(baseMen, baseMay, altura)

    print ("El area es: %.2f" % area)
    print ("El perimetro es: %.2f" % perimetro)

main()
