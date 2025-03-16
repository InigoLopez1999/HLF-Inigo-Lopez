# Proyecto Hundir La Flota
### Realizado por Iñigo López Ayala

1. #### Archivo variables.py

    * La primera variable que definimos es el tamaño del tablero, siendo el número asignado el número de filas y columnas que poseerá el tablero.
        - En nuestro caso esta variable se ha asignado con el nombre de Tamano_tablero (10).
    * El siguiente conjunto de variables corresponde al número de barcos que hay en el tablero en función de su eslora, de manera que:
        - Si el barco tiene 1 de eslora (fragata), el número de fragatas es de 4.
        - Si el barco tiene 2 de eslora (destructor), el número de destructor es de 3.
        - Si el barco tiene 3 de eslora (acorazado), el número de acorazado es de 2.
        - Si el barco tiene 4 de eslora (portaaviones), el número de portaaviones es de 1.
    * Al final, se describe el número total de barco como la suma total de todas las variables de número de barcos.

    * Este primer conjunto de variables que describe el número de barcos nos servirá para colocar los barcos en un tablero (en el del usuario).

    * Para el tablero de la máquina deberemos definir variable de número de barcos de distinto nombre ya que si las definimos con el mismo nombre, cuando colocamos los barcos en el primer tablero, no quedarán barcos por colocar en el segundo. Se explicará esto más adelante en el apartado de funciones.

2. #### Archivo funciones.py

    * ##### *Función de creación del tablero*

        * Esta función se define con un único argumento, siendo el tamaño del tablero (Tamano_tablero).
        * Se crea una variable llamada tablero como una lista de listas en función de la variable Tamano_tablero.
    
    * ##### *Función de colocación de barcos de manera manual*

        * Esta función nos permite colocar cada barco de manera manual en la ubicación que desee el usuario.
        * Esta función posee un único argumento de entrada, el tablero del usuario.
        * Lo primero que hacemos es globalizar las variables en el archivo variables.py para poder utilizarlas en cualquier instancia del archivo
        * Se crea una variable colocacion como un booleano inicializado a True. Cuando colocacion sea False será cuando no queden barcos de cierto tipo y se desee colocar otro, no habiendo ya barcos de ese tipo por colocar.
        * A través de un input se pregunta al usuario qué barco desea colocar en el tablero.
        * A continuación, mediante un bucle while, se asegura que la entrada sea robusta frente a input ajenos a los tipos de barcos.
        
        1. Si el usuario elige fragata:

            - En caso de que queden fragatas por colocar, se piden dos coordenadas x e y para poder poner la fragata donde quiera el usuario.
            - Se resta la cantidad de fragatas en 1.
            - Cuando llegue el número de fragatas a 0 y se desee colocar otra, saltará un mensaje que indique la ausencia de dicho barco y se devuelve
            colocacion = False. Las consecuencias de este False se explicarán en la sección de main.py.
        
        2. Si el usuario elige destructor:

            - Así como en el caso de las fragatas primero se comprueba que haya destructores disponibles para colocar .
            - Se coloca la primera porción del barco.
            - Se define una lista (lista_dest) que varía en longitud en función de la eslora del barco (en ste caso el destructor al tener 2 de eslora, la lista tendrá un elemento ya que se debe añadir la segunda porción del destructor).
            - A continuación, con una serie de condicionales, se da la opción de elegir la dirección (horizontal o vertical) y la dirección (este, oeste, sur y norte).
            - Se coloca la siguiente parte del barco a través de un bucle for que recorre lista_dest y se imprime una nueva parte del barco en función de su longitud de la lista.
            - Así como en las fragatas, una vez colocado el barco se resta uno del inventario y si ya no quedan destructores se le hace saber esto al ususario y se devuelve un False.

            

