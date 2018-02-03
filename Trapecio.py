#Autor: Eduardo Roberto Müller Romero
#Programa que rcibe datos acerca de un trapecio (base mayor, base menor, altura) y calcule el área y el perímetro del mismo
'''
     __________________________
    /                          \
   /                            \
  /                              \
 /________________________________\
'''

def main():
	basemayor = int(input("Base Mayor: "))
	basemenor = int(input("Base Menor: "))
	altura = int(input("Altura: "))
	area, perimetro = calcularAreayPerimetro(basemayor, basemenor, altura) #La función regresa dos datos
	print("Área del Trapecio: %.2f" % area, "\nPerímetro del Trapecio: %.2f" % perimetro)

def calcularAreayPerimetro(basemayor, basemenor, altura): #La función calcula y regresa tanto área como perímetro
	area = ((basemayor + basemenor) / 2) * altura
	diferenciadeBases = (basemayor - basemenor) / 2
	lados = 2 * ((diferenciadeBases**2 + altura**2)**.5)
	perimetro = basemayor + basemenor + lados
	return area, perimetro

main()