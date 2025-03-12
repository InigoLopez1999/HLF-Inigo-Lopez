from variables import *

def nuevo_tablero (Tamano):
    tablero = [[" " for i in range(Tamano)] for j in range(Tamano)]
    return tablero

def posicionar_barco (tablero):
    barco_a_colocar = input ("Qué barco desea colocar en el tablero?").lower()
    coord_x = int(input ("Dígame la coordenada X del barco a colocar:"))
    coord_y = int(input ("Dígame la coordenada Y del barco a colocar:"))

    # Barco de 1 de eslora

    if barco_a_colocar == "fragata":
        tablero[coord_x][coord_y] = "B"
        num_fragatas = num_fragatas - 1

    # Barco de 2 de eslora

    elif barco_a_colocar == "destructor":
        tablero[coord_x][coord_y] = "B"
        list_eslora = [1]
        orientacion = input ("Cómo quiere colocar el barco, en horizontal o en vertical?").lower()
        if orientacion == "horizontal":
            este_oeste = input ("Hacia el este o hacia el oeste?")
            if este_oeste == "este":
                for eslora in list_eslora:
                    tablero[coord_x][coord_y + eslora] = "B"
            elif este_oeste == "oeste":
                for eslora in list_eslora:
                    tablero[coord_x][coord_y - eslora] = "B"
        elif orientacion == "vertical":
            norte_sur = input ("Hacia el norte o hacia el sur?")
            if norte_sur == "norte":
                for eslora in list_eslora:
                    tablero[coord_x - eslora][coord_y] = "B"
            elif norte_sur == "sur":
                for eslora in list_eslora:
                    tablero[coord_x + eslora][coord_y] = "B"
        num_destructores = num_destructores - 1
        
    # Barco de 3 de eslora

    elif barco_a_colocar == "acorazado":
        tablero[coord_x][coord_y] = "B"
        list_eslora = [1,2]
        orientacion = input ("Cómo quiere colocar el barco, en horizontal o en vertical?").lower()
        if orientacion == "horizontal":
            este_oeste = input ("Hacia el este o hacia el oeste?")
            if este_oeste == "este":
                for eslora in list_eslora:
                    tablero[coord_x][coord_y + eslora] = "B"
            elif este_oeste == "oeste":
                for eslora in list_eslora:
                    tablero[coord_x][coord_y - eslora] = "B"
        elif orientacion == "vertical":
            norte_sur = input ("Hacia el norte o hacia el sur?")
            if norte_sur == "norte":
                for eslora in list_eslora:
                    tablero[coord_x - eslora][coord_y] = "B"
            elif norte_sur == "sur":
                for eslora in list_eslora:
                    tablero[coord_x + eslora][coord_y] = "B"
        num_acorazados = num_acorazados - 1
    
    # Barco de 4 de eslora

    elif barco_a_colocar == "portaaviones":
        while num_portaaviones != 0:
            tablero[coord_x][coord_y] = "B"
            list_eslora = [1,2,3]
            orientacion = input ("Cómo quiere colocar el barco, en horizontal o en vertical?").lower()
            if orientacion == "horizontal":
                este_oeste = input ("Hacia el este o hacia el oeste?")
                if este_oeste == "este":
                    for eslora in list_eslora:
                        tablero[coord_x][coord_y + eslora] = "B"
                elif este_oeste == "oeste":
                    for eslora in list_eslora:
                        tablero[coord_x][coord_y - eslora] = "B"
            elif orientacion == "vertical":
                norte_sur = input ("Hacia el norte o hacia el sur?")
                if norte_sur == "norte":
                    for eslora in list_eslora:
                        tablero[coord_x - eslora][coord_y] = "B"
                elif norte_sur == "sur":
                    for eslora in list_eslora:
                        tablero[coord_x + eslora][coord_y] = "B"
            num_portaaviones = num_portaaviones - 1
            if num_portaaviones == 0:
                print ("No quedan más portaaviones por colocar")
                continue

    return tablero
