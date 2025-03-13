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

    while num_portaaviones == 1:
        posicionar_poortaaviones_aleatorio(tablero_nuevo,4)
        pprint.pprint(tablero_nuevo)
        num_portaaviones = num_portaaviones - 1

    while num_acorazados >= 0:
        posicionar_acorazados_aleatorio(tablero_nuevo,3)
        pprint.pprint(tablero_nuevo)
        num_acorazados = num_acorazados - 1
    
    while num_destructores >= 0:
        posicionar_destructores_aleatorio(tablero_nuevo,2)
        pprint.pprint(tablero_nuevo)
        num_destructores = num_destructores - 1
    
    while num_fragatas >= 0:
        posicionar_fragatas_aleatorio(tablero_nuevo,1)
        pprint.pprint(tablero_nuevo)
        num_fragatas = num_fragatas - 1
