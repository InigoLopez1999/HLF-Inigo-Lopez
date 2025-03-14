import time
import os
import pprint
from variables import *
from funciones import *

colocacion = True

tablero_nuevo = nuevo_tablero(Tamano_tablero)
tablero_maquina = nuevo_tablero(Tamano_tablero)
tablero_disparo_usuario = nuevo_tablero(Tamano_tablero)
tablero_disparo_usuario = nuevo_tablero(Tamano_tablero)

print("Bienvenido al juego Hundir La Flota:")
print()
print("Aquí está su tablero de juego vacío")
print()
pprint.pprint(tablero_nuevo)
print()
print("Aquí está el tablero de la máquina")
print()
pprint.pprint(tablero_maquina)

manual_o_aleatorio = input("Desea colocar los barcos manualmente o que estén posicionados de manera aleatoria?")
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
        #pprint.pprint(tablero_nuevo)
        num_portaaviones = num_portaaviones - 1

    while num_acorazados >= 0:
        posicionar_acorazados_aleatorio(tablero_nuevo,3)
        #pprint.pprint(tablero_nuevo)
        num_acorazados = num_acorazados - 1
    
    while num_destructores >= 0:
        posicionar_destructores_aleatorio(tablero_nuevo,2)
        #pprint.pprint(tablero_nuevo)
        num_destructores = num_destructores - 1
    
    while num_fragatas >= 0:
        posicionar_fragatas_aleatorio(tablero_nuevo,1)
        #pprint.pprint(tablero_nuevo)
        num_fragatas = num_fragatas - 1
    print()
    print("Le presento su tablero con los barcos colocados")
    print()
    pprint.pprint(tablero_nuevo)

while num_portaaviones_maquina == 1:
    posicionar_poortaaviones_aleatorio(tablero_maquina,4)
    num_portaaviones_maquina = num_portaaviones_maquina - 1

while num_acorazados_maquina >= 0:
    posicionar_acorazados_aleatorio(tablero_maquina,3)
    num_acorazados_maquina = num_acorazados_maquina - 1

while num_destructores_maquina >= 0:
    posicionar_destructores_aleatorio(tablero_maquina,2)
    num_destructores_maquina = num_destructores_maquina - 1

while num_fragatas_maquina >= 0:
    posicionar_fragatas_aleatorio(tablero_maquina,1)
    num_fragatas_maquina = num_fragatas_maquina - 1
print()
print("Le presento el tablero de la máquina con los barcos colocados")
print()
pprint.pprint(tablero_maquina)
print()

while True:
    print("Este es el tablero donde va a realizar sus disparos")
    print()
    pprint.pprint(tablero_disparo_usuario)
    print()
    x = int(input("Introduzca la fila, por favor: "))
    y = int(input("Introduza la columna, por favor: "))
    acierto =  disparo(tablero_maquina,tablero_disparo_usuario,x,y)
    if not acierto:
        pprint.pprint(tablero_disparo_usuario)
        break
    