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
        
        3. Si el usuario elige acorazado:

            - El código es exactamente igual que para colocar el destructor, a excepción de la lista a recorrer con el for. Al ser un barco de 3 de eslora, una vez colocada la primera parte del barco, la lista será de dos elementos pues son los que hay que añadir para completar el acorazado.

        4. Si el usuario elige portaaviones:

            - Exactamente idéntico al código anterior a excepción de la lista a iterar que es [1,2,3], que equivalen al número de partes a añadir para formar el portaaviones.
        
    * #### *Función de colocación de barcos aleatoria*

        Esta función se ha repetido un total de 4 veces en el archivo de funciones, una para cada tipo de barco.

        - Cada función de colocación de barcos aleatoria posee dos argumentos: el tablero donde se desea colocar el barco y la longitud (o eslora) del barco a colocar.

        - Se inicializa con un while True que se romperá en caso de que el barco no quepa en el tablero o se superponga con otro barco.

        - En primer lugar se declaran tres variables, donde gracias a la función random.randint se generan dos números aleatorios correspondientes a la fila y columna donde se vaya a colocar la primera parte del barco. La tercera variable consiste en un random.choice, donde el programa escogerá una letra de cuatro disponibles, representando cada una de los 4 puntos cardinales.

        - En cada una de las 4 orientaciones:

        1. Con un bucle for se recorre un range con la longitud (eslora) introducida como argumento. Esto nos servirá para poder colocar el número óptimo de partes de barco en función de su longitud.

        2. Antes de colocar el barco se hacen dos comprobaciones: que el barco no se salga del tablero al acabar las iteraciones del for y que no se pueda colocar una parte de un barco sobre otra. En cualquiera de los dos casos se oredena al programa con un break que salga del bucle while True y se repetirá el bucle hasta que se coloquen todos los barcos de esa clase.

        3. En caso de que el for no se rompa con un break se ejecuta el else correspondiente, el cual imprime la totalidad del barco en el tablero a travles de otro bucle for (parte por parte)

        - Esta comprobación de las 4 orientaciones se hace en las 4 funciones para cada tipo de barco (lo único que cambia entre cada función de colocación aleatoria es la letra representativa de cada barco)
    
    * #### *Función de disparo*

        Esta función recibe como argumentos el tablero sobre el que va a realizar el disparo y el tablero del usuario que dispara donde indicará las localizaciones de todos los disparos que realice con el fin de saber dónde ha disparado el jugador. Los otros dos argumentos son las corrdenadas X e Y donde el jugador desee realizar el disparo. Tanto el usuario como la máquina utlizarán esta función.

        - Lo primero que comprueba la función es si se ha acertado el disparo. Si ha sido el caso el programa devuelve True (lo que significa que se repetirá la función hasta que el jugador falle). En ambos tableros se imprimirá una X para indicar el acierto.

        - Si el jugador da en el agua o mete una coordenada utilizada previamente, el programa indica el correspondiente fallo del jugador y devuelve False (es el turno del oponente). Si el acierto da en el agua se marca con una O en los dos tableros.
    
    - #### *Función para comprobar si sigue habiendo barcos en el tablero de algún jugador*

        Con dos bucles for se comprueba que en cada celda haya cualquiera de las cuatro letras que representan. Si se devuelve True el juego sigue y se pasa al siguiente bucle. En caso contrario, se devuelve False y, por ende, el juego termina.
    
3. ### Main.py

Al principio del programa se importan las librerías time, os y pprint para estilizar la presentación del juego. Además se importan todas las funciones y variables de los otros archivos con from import *.
 
Lo primero que se hace es crear los cuatro tableros (uno para posicionar los barcos de cada jugador y uno para realizar disparos para cada jugador)

A continuación se crea una interfaz de bienvenida al usuario, donde debe introducir su nombre y se inicializa el juego. Todo ello con lapsus de tiempo y limpiezas de terminal para una mejor apreciación de los elementos en pantalla.

Se crea un input que pregunta al usuario cómo desea colocar los barcos, manualmente o aleatoriamente.

* Si elige de forma manual y mientras el número de barcos sea mayor que 0, se irán colocando uno a uno los barcos como se ha indicado en la función descrita previamente. En caso de que el barco se coloque, se imprimirá el tablero y, cuando se acaben los barcos, el programa volverá al comienzo del while, donde preguntará por el barco a colocar hasta que se elija otro tipo de barco. Cuando tras haber colocado todos loa barcos el contador baje a 0 se podrá salir del bucle while inicial y empezar a disparar.

* Si elige de forma aleatoria, se crearán 4 bucles while para las 4 funciones de colocación que existen para cada barco. En cada una de ellas se irán colocando los barcos cuya eslora en indicada al llamar a la función. Se saldrá de cada uno de los bucles while cuando se acaben los barcos en cada familia.

* Este proceso de colocación aleatoria se emula para el ordenador, con lo que ya podemos pasar a hacer los disparos.

* A la hora de hacer los disparos se  debe comprobar que queden barcos en alguno de los dos. Esto se hace con un bucle while que, gracias a la función que nos permite recorrer todas las celdas del tablero descrita previamente.

* Si quedan barcos los disparos se irán realizando por turnos, empezando en primer lugar el jugador.

* Dentro de un while True se pregunta al usuario por las coordenadas donde desea realizar su disparo. Si el usuario acierta acierto devolverá True y el bucle se repetirá hasta que falle, en cuyo caso acierto será False y entonces se romperá el bucle mediante un break.

* Durante el turno de la máquina se replica este procedimiento, solo que la máquina escoge las coordenadas de disparo de manera aleatoria mediante un random.randint.

* Cada vez que un jugador falle, se romperá el bucle while True y se regresará al bucle que comprueba que queden barcos en alguno de los dos tableros, de manera que los disparos serán continuados hasta que alguien se quede sin barcos. Si se da el caso, el programa declarará el ganador y mediante un break romperá el while y se acabará el juego.

* Nota: para agilizar el juego durante el día de la demo se ha incluido un input que pregunta al usuario si desea ver el tablero de la máquina para así poder acertar todos los disparos ya acabar antes la partida.

            

