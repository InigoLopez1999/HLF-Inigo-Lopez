import time
import os
import pprint
from variables import *
from funciones import *

tablero_nuevo = nuevo_tablero(Tamano_tablero)
pprint.pprint(tablero_nuevo)

while Numero_barcos != 0:
    posicionar_barco(tablero_nuevo)
    pprint.pprint(tablero_nuevo)
    if Numero_barcos == 0:
        print("Ya no quedan más barcos por colocar")
        break

