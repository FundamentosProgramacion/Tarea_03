#Autor: Ricardo Cornejo Lozano
#calcula precio total de boletos conforme el tipo de asientos

def calcularPago(a,b,c):
   total = (a*870) + (b*650) + (c*235)
   return total

def main():
  a = int(input("Teclea numero de asientos clase A: "))
  b = int(input("Teclea numero de asientos clase B: "))
  c = int(input("Teclea numero de asientos clase C: "))
  total =calcularPago(a,b,c)
  print ("El costo total es: $%.2f" % total)

main()
