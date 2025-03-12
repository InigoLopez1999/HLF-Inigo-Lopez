from variables import *

def nuevo_tablero (Tamano):
    tablero = [[" " for i in range(Tamano)] for j in range(Tamano)]
    return tablero

def posicionar_barco (tablero):
    global Numero_barcos
    global num_portaaviones
    global num_fragatas
    global num_acorazados
    global num_destructores
    barco_a_colocar = input ("Qué barco desea colocar en el tablero?").lower()
    while barco_a_colocar not in ["fragata","destructor","acorazado","portaaviones"]:
        print("Entrada no válida. Vuelva a intentarlo")
        barco_a_colocar = input ("Qué barco desea colocar en el tablero?").lower()

    # Barco de 1 de eslora

    if barco_a_colocar == "fragata":
        if barco_a_colocar == "fragata" and num_fragatas == 0:
            print("Ya no quedan más fragatas")
            barco_a_colocar = input ("Qué barco desea colocar en el tablero?").lower()
        while num_fragatas > 0:
            coord_x = int(input ("Dígame la coordenada X del barco a colocar:"))
            coord_y = int(input ("Dígame la coordenada Y del barco a colocar:"))
            tablero[coord_x][coord_y] = "B"
            num_fragatas = num_fragatas - 1

    # Barco de 2 de eslora

    elif barco_a_colocar == "destructor":
        if barco_a_colocar == "destructor" and num_destructores == 0:
            print("Ya no quedan más destructores")
            barco_a_colocar = input ("Qué barco desea colocar en el tablero?").lower()
        while num_destructores > 0:
            coord_x = int(input ("Dígame la coordenada X del barco a colocar:"))
            coord_y = int(input ("Dígame la coordenada Y del barco a colocar:"))
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
        if barco_a_colocar == "acorazado" and num_acorazados == 0:
            print("Ya no quedan más acorazados")
            barco_a_colocar = input ("Qué barco desea colocar en el tablero?").lower()
        while num_acorazados > 0:
            coord_x = int(input ("Dígame la coordenada X del barco a colocar:"))
            coord_y = int(input ("Dígame la coordenada Y del barco a colocar:"))
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
        if barco_a_colocar == "portaaviones" and num_portaaviones == 0:
            print("Ya no quedan más portaaviones")
            barco_a_colocar = input ("Qué barco desea colocar en el tablero?").lower()
        while num_portaaviones > 0:
            coord_x = int(input ("Dígame la coordenada X del barco a colocar:"))
            coord_y = int(input ("Dígame la coordenada Y del barco a colocar:"))
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
    
    Numero_barcos = num_fragatas + num_destructores + num_acorazados + num_portaaviones
    print (Numero_barcos,num_portaaviones,num_acorazados,num_destructores,num_fragatas)
    
    return tablero
