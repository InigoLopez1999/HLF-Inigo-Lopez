from variables import *

def nuevo_tablero (Tamano):
    tablero = [[" " for i in range(Tamano)] for j in range(Tamano)]
    return tablero

def posicionar_barco ():
    barco_a_colocar = input ("Qué barco desea colocar en el tablero?")
    