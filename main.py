import time
import os
import pprint
from variables import *
from funciones import *

colocacion = True

tablero_nuevo = nuevo_tablero(Tamano_tablero)
tablero_maquina = nuevo_tablero(Tamano_tablero)
tablero_disparo_usuario = nuevo_tablero(Tamano_tablero)
tablero_disparo_maquina = nuevo_tablero(Tamano_tablero)

print("Bienvenido al juego Hundir La Flota:")
print()
nombre_usuario = input("Introduzca su nombre si es tan amable:")
time.sleep(3)
print(f"Mucho gusto {nombre_usuario}. En este juego le proporcionaremos un tablero vacío de 10 x 10 donde podrá colocar un total de 10 barcos con las siguientes características:")
time.sleep(3)
print("-4 fragatas de 1 de eslora \n-3 destructores de 2 de eslora \n-2 acorazados de 3 de eslora \n-1 portaaviones de 4 de eslora")
print()
time.sleep(5)
print("Le daremos la posibilidad de poder colocar sus barcos de forma manual en el tablero o bien dejar que se coloquen aleatoriamente")
time.sleep(3)
print("Aquí está su tablero de juego vacío")
print()
pprint.pprint(tablero_nuevo)
time.sleep(5)
os.system("cls")

manual_o_aleatorio = input("Desea colocar los barcos manualmente o que estén posicionados de manera aleatoria?")
if manual_o_aleatorio == "manual":
    while Numero_barcos > 0:
        Numero_barcos,colocacion=posicionar_barco_manual(tablero_nuevo)
        if colocacion == True:
            pprint.pprint(tablero_nuevo)
        else:
            continue
        if Numero_barcos == 0:
            print("Ya no quedan más barcos por colocar")
            break

elif manual_o_aleatorio == "aleatorio":
    time.sleep(3)
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
    time.sleep(1)
    print()
    pprint.pprint(tablero_nuevo)
    time.sleep(3)
    os.system("cls")

time.sleep(2)
while num_portaaviones_maquina == 1:
    posicionar_poortaaviones_aleatorio(tablero_maquina,4)
    num_portaaviones_maquina = num_portaaviones_maquina - 1

while num_acorazados_maquina >= 1:
    posicionar_acorazados_aleatorio(tablero_maquina,3)
    num_acorazados_maquina = num_acorazados_maquina - 1

while num_destructores_maquina >= 1:
    posicionar_destructores_aleatorio(tablero_maquina,2)
    num_destructores_maquina = num_destructores_maquina - 1

while num_fragatas_maquina >= 1:
    posicionar_fragatas_aleatorio(tablero_maquina,1)
    num_fragatas_maquina = num_fragatas_maquina - 1

contador = 0
while hay_barcos(tablero_nuevo) and hay_barcos(tablero_maquina):
    print("Este es el tablero donde va a realizar sus disparos")
    print()
    pprint.pprint(tablero_disparo_usuario)
    print()
    time.sleep(2)
    while True:
        time.sleep(5)
        os.system("cls")
        x = int(input("Introduzca la fila, por favor: "))
        y = int(input("Introduza la columna, por favor: "))
        acierto =  disparo(tablero_maquina,tablero_disparo_usuario,x,y)
        contador = contador + 1
        if contador == 3:
            ganar_auto = input("Deseas ganar la partida?")
            if ganar_auto == "si":
                for linea in range(len(tablero_maquina)):
                    for letra in range(len(tablero_maquina[linea])):
                        if tablero_maquina[linea][letra] in ("A","P","D","F"):
                            tablero_maquina[linea][letra] = "X"
        time.sleep(2)
        if not hay_barcos(tablero_maquina):
            break
        if not acierto:
            print("Es el turno de tu oponente")
            time.sleep(1)
            os.system("cls")
            break
        time.sleep(3)
        os.system("cls")
   
    if not hay_barcos(tablero_maquina):
        pprint.pprint(tablero_maquina)
        time.sleep(3)
        print("Se acabó el juego. Ha batido a la máquina. Felicidades!")
        break

    while True:
        x = random.randint(0, Tamano_tablero - 1)
        y = random.randint(0, Tamano_tablero - 1)
        acierto =  disparo(tablero_nuevo,tablero_disparo_maquina,x,y)
        if not hay_barcos(tablero_nuevo):
            break
        if not acierto:
            print("Es el turno de tu oponente")
            time.sleep(1)
            os.system("cls")
            break
        time.sleep(3)
        os.system("cls")

    if not hay_barcos(tablero_nuevo):
        print("Se acabó el juego. La máquina ha ganado. Vuelva a intentarlo cuando guste.")
        break