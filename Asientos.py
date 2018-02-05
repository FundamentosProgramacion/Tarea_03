# encoding: UTF-8
#Autor: Genaro Ortiz Durán
#Descripción: Crear un algoritmo que calcule el total a pagar con la cantidad de asientos de cada tipo.
A=870
B=650
C=235
# Calcula la cantidad multiplicando la cantidad del asiento pedido por su respectivo precio.
def calcularPago(boletosA, boletosB, boletosC):
    total=(A*boletosA)+(B*boletosB)+(C*boletosC)
    return total



def main():
    boletosA=int(input("¿Cuántos boletos de clase A quieres?:"))
    boletosB=int( input ( "¿Cuántos boletos de clase B quieres?:"))
    boletosC=int( input ( "¿Cuántos boletos de clase C quieres?:"))
    print("El costo toal es", "$",format(calcularPago(boletosA,boletosB,boletosC),".2f"))




main()