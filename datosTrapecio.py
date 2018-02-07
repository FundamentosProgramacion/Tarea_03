#Mirna Zertuche Calvillo A01373852
#Un programa que calcula el área y el perímetro de un trapecio isóseles a partir de su base mayor, base menor y altura.

def areaTotal(B,b,h):
    area= (B+b)/2*h
    return area

def perimetroTotal(B,b,h):
    a=(B-b)/2
    c= (a**2+h**2)**0.5
    p= B+b+c*2
    return p

def main():
    B = float(input("Escribe la longitud de la base mayor: "))
    b = float(input("Escribe la longitud de la base menor: "))
    h = float(input("Escribe la altura: "))
    area= areaTotal(B,b,h)
    perimetro = perimetroTotal(B,b,h)
    print("Área: %.2f" % area)
    print("Perímetro: %.2f" % perimetro)

main()