# Proyecto Hundir La Flota
### Realizado por Iñigo López Ayala

1. #### Archivo variables.py

    * La primera variable que definimos es el tamaño del tablero, siendo el número asignado el número de filas y columnas que poseerá el tablero 
        - En nuestro caso esta variable se ha asignado con el nombre de Tamano_tablero (10)
    * El siguiente conjunto de variables corresponde al número de barcos que hay en el tablero en función de su eslora, de manera que:
        - Si el barco tiene 1 de eslora (fragata), el número de fragatas es de 4
        - Si el barco tiene 2 de eslora (destructor), el número de destructor es de 3
        - Si el barco tiene 3 de eslora (acorazado), el número de acorazado es de 2
        - Si el barco tiene 4 de eslora (portaaviones), el número de portaaviones es de 1
    * Al final, se describe el número total de barco como la suma total de todas las variables de número de barcos

    * Este primer conjunto de variables que describe el número de barcos nos servirá para colocar los barcos en un tablero (en el del usuario)

    * Para el tablero de la máquina deberemos definir variable de número de barcos de distinto nombre ya que si las definimos con el mismo nombre, cuando colocamos los barcos en el primer tablero, no quedarán barcos por colocar en el segundo. Se explicará esto más adelante en el apartado de funciones.

2. #### Archivo funciones.py

    * ##### Función de creación del tablero

        * Esta función se define con un único argumento, siendo el tamaño del tablero (Tamano_tablero)
        * Se crea una variable llamada tablero como una lista de listas en función de la variable Tama

