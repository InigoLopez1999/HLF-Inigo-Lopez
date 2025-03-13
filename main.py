import time
import os
import pprint
from variables import *
from funciones import *

colocacion = True

tablero_nuevo = nuevo_tablero(Tamano_tablero)
pprint.pprint(tablero_nuevo)

manual_o_aleatorio = input("Deseas colocar los barcos manualmente o que estén posicionados de manera aleatoria?")
if manual_o_aleatorio == "manual":
    while Numero_barcos > 0:
        Numero_barcos,colocacion=posicionar_barco_manual(tablero_nuevo)
        print(Numero_barcos)
        if colocacion == True:
            pprint.pprint(tablero_nuevo)
        else:
            continue

        if Numero_barcos == 0:
            print("Ya no quedan más barcos por colocar")
            break

elif manual_o_aleatorio == "aleatorio":
    posicionar_barcos_aleatorio(tablero_nuevo,3)
    pprint.pprint(tablero_nuevo)
 