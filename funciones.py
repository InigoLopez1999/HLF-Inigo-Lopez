from variables import *

def nuevo_tablero (Tamano):
    tablero = [[" " for i in range(Tamano)] for j in range(Tamano)]
    return tablero

def posicionar_barco_manual (tablero):
    global Numero_barcos
    global num_portaaviones
    global num_fragatas
    global num_acorazados
    global num_destructores
    colocacion = True
    Numero_barcos = num_fragatas + num_destructores + num_acorazados + num_portaaviones
    
    barco_a_colocar = input ("Qué barco desea colocar en el tablero?").lower()
    while barco_a_colocar not in ["fragata","destructor","acorazado","portaaviones"]:
        print("Entrada no válida. Vuelva a intentarlo")
        continue

    # Barco de 1 de eslora

    if barco_a_colocar == "fragata":

        if num_fragatas > 0:
            coord_x = int(input ("Dígame la coordenada X del barco a colocar:"))
            coord_y = int(input ("Dígame la coordenada Y del barco a colocar:"))
            tablero[coord_x][coord_y] = "B"
            num_fragatas = num_fragatas - 1
        
        elif num_fragatas == 0:
            print("Ya no quedan más fragatas")
            colocacion = False
            return Numero_barcos,colocacion

    # Barco de 2 de eslora

    elif barco_a_colocar == "destructor":

        if num_destructores > 0:
            coord_x = int(input ("Dígame la coordenada X del barco a colocar:"))
            coord_y = int(input ("Dígame la coordenada Y del barco a colocar:"))
            tablero[coord_x][coord_y] = "B"
            list_dest = [1]
            orientacion = input ("Cómo quiere colocar el barco, en horizontal o en vertical?").lower()
            if orientacion == "horizontal":
                este_oeste = input ("Hacia el este o hacia el oeste?")
                if este_oeste == "este":
                    for eslora in list_dest:
                        tablero[coord_x][coord_y + eslora] = "B"
                elif este_oeste == "oeste":
                    for eslora in list_dest:
                        tablero[coord_x][coord_y - eslora] = "B"
            elif orientacion == "vertical":
                norte_sur = input ("Hacia el norte o hacia el sur?")
                if norte_sur == "norte":
                    for eslora in list_dest:
                        tablero[coord_x - eslora][coord_y] = "B"
                elif norte_sur == "sur":
                    for eslora in list_dest:
                        tablero[coord_x + eslora][coord_y] = "B"
            num_destructores = num_destructores - 1

        elif num_destructores == 0:
            print("Ya no quedan más destructores")
            colocacion = False
            return Numero_barcos,colocacion
        
    # Barco de 3 de eslora

    elif barco_a_colocar == "acorazado":

        if num_acorazados > 0:
            coord_x = int(input ("Dígame la coordenada X del barco a colocar:"))
            coord_y = int(input ("Dígame la coordenada Y del barco a colocar:"))
            tablero[coord_x][coord_y] = "B"
            list_aco = [1,2]
            orientacion = input ("Cómo quiere colocar el barco, en horizontal o en vertical?").lower()
            if orientacion == "horizontal":
                este_oeste = input ("Hacia el este o hacia el oeste?")
                if este_oeste == "este":
                    for eslora in list_aco:
                        tablero[coord_x][coord_y + eslora] = "B"
                elif este_oeste == "oeste":
                    for eslora in list_aco:
                        tablero[coord_x][coord_y - eslora] = "B"
            elif orientacion == "vertical":
                norte_sur = input ("Hacia el norte o hacia el sur?")
                if norte_sur == "norte":
                    for eslora in list_aco:
                        tablero[coord_x - eslora][coord_y] = "B"
                elif norte_sur == "sur":
                    for eslora in list_aco:
                        tablero[coord_x + eslora][coord_y] = "B"
            num_acorazados = num_acorazados - 1
        
        elif num_acorazados == 0:
            print("Ya no quedan más acorazados")
            colocacion = False
            return Numero_barcos,colocacion
    
    # Barco de 4 de eslora

    elif barco_a_colocar == "portaaviones":

        if num_portaaviones > 0:
            coord_x = int(input ("Dígame la coordenada X del barco a colocar:"))
            coord_y = int(input ("Dígame la coordenada Y del barco a colocar:"))
            tablero[coord_x][coord_y] = "B"
            list_porta = [1,2,3]
            orientacion = input ("Cómo quiere colocar el barco, en horizontal o en vertical?").lower()
            if orientacion == "horizontal":
                este_oeste = input ("Hacia el este o hacia el oeste?")
                if este_oeste == "este":
                    for eslora in list_porta:
                        tablero[coord_x][coord_y + eslora] = "B"
                elif este_oeste == "oeste":
                    for eslora in list_porta:
                        tablero[coord_x][coord_y - eslora] = "B"
            elif orientacion == "vertical":
                norte_sur = input ("Hacia el norte o hacia el sur?")
                if norte_sur == "norte":
                    for eslora in list_porta:
                        tablero[coord_x - eslora][coord_y] = "B"
                elif norte_sur == "sur":
                    for eslora in list_porta:
                        tablero[coord_x + eslora][coord_y] = "B"
            num_portaaviones = num_portaaviones - 1
        
        elif num_portaaviones == 0:
            print("Ya no quedan más portaaviones")
            colocacion = False
            return Numero_barcos,colocacion

    Numero_barcos = num_fragatas + num_destructores + num_acorazados + num_portaaviones
    print (Numero_barcos,num_portaaviones,num_acorazados,num_destructores,num_fragatas,colocacion)
    return Numero_barcos,colocacion
    
def posicionar_barcos_fijos(tablero):
    tablero[3][3] = 'B'
    tablero[4][3] = 'B'
    tablero[5][3] = 'B'
    tablero[6][3] = 'B'

    tablero[1][0] = 'B'
    tablero[1][1] = 'B'
    tablero[1][2] = 'B'
    tablero[1][3] = 'B'
