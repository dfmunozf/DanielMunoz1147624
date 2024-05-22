# Definimos el tablero de ajedrez utilizando la estructura proporcionada
Tablero = [[["v"], ["v"], ["v"], ["v"], ["v"], ["v"], ["v"], ["v"]],
           [["v"], ["v"], ["v"], ["v"], ["v"], ["v"], ["v"], ["v"]],
           [["v"], ["v"], ["v"], ["v"], ["v"], ["v"], ["v"], ["v"]],
           [["v"], ["v"], ["v"], ["v"], ["v"], ["v"], ["v"], ["v"]],
           [["v"], ["v"], ["v"], ["v"], ["v"], ["v"], ["v"], ["v"]],
           [["v"], ["v"], ["v"], ["v"], ["v"], ["v"], ["v"], ["v"]],
           [["v"], ["v"], ["v"], ["v"], ["v"], ["v"], ["v"], ["v"]],
           [["v"], ["v"], ["v"], ["v"], ["v"], ["v"], ["v"], ["v"]]]

# Función para convertir la notación de ajedrez a índices de la matriz
def notacion_a_indices(coordenada):
    columna = ord(coordenada[0].lower()) - ord('a')
    fila = 8 - int(coordenada[1])
    return fila, columna

# Función para verificar si la posición es válida y no está ocupada
def es_posicion_valida(fila, columna):
    return 0 <= fila < 8 and 0 <= columna < 8 and Tablero[fila][columna][0] == "v"

# Función para agregar una pieza al tablero
def agregar_pieza(tipo, color, coordenada):
    fila, columna = notacion_a_indices(coordenada)
    if es_posicion_valida(fila, columna):
        Tablero[fila][columna] = [tipo, color]
        return True
    else:
        return False

# Función para mostrar todos los posibles movimientos de la torre
def movimientos_torre(filaTorre, colTorre, colorTorre):
    movimientos = []

    # Movimientos hacia la derecha
    colDerechaInicial = colTorre + 1
    if colDerechaInicial < 8:
        for x in range(colDerechaInicial, 8):
            if Tablero[filaTorre][x][0] == "v":
                movimientos.append((filaTorre, x, "vacía"))
            else:
                if Tablero[filaTorre][x][1] != colorTorre:
                    movimientos.append((filaTorre, x, f"{Tablero[filaTorre][x][0]} {Tablero[filaTorre][x][1]}"))
                else:
                    movimientos.append((filaTorre, x, "misma color"))
                break

    # Movimientos hacia la izquierda
    colIzquierdaInicial = colTorre - 1
    if colIzquierdaInicial >= 0:
        for x in range(colIzquierdaInicial, -1, -1):
            if Tablero[filaTorre][x][0] == "v":
                movimientos.append((filaTorre, x, "vacía"))
            else:
                if Tablero[filaTorre][x][1] != colorTorre:
                    movimientos.append((filaTorre, x, f"{Tablero[filaTorre][x][0]} {Tablero[filaTorre][x][1]}"))
                else:
                    movimientos.append((filaTorre, x, "misma color"))
                break

    # Movimientos hacia arriba
    filSuperiorInicial = filaTorre - 1
    if filSuperiorInicial >= 0:
        for x in range(filSuperiorInicial, -1, -1):
            if Tablero[x][colTorre][0] == "v":
                movimientos.append((x, colTorre, "vacía"))
            else:
                if Tablero[x][colTorre][1] != colorTorre:
                    movimientos.append((x, colTorre, f"{Tablero[x][colTorre][0]} {Tablero[x][colTorre][1]}"))
                else:
                    movimientos.append((x, colTorre, "misma color"))
                break

    # Movimientos hacia abajo
    filInferiorInicial = filaTorre + 1
    if filInferiorInicial < 8:
        for x in range(filInferiorInicial, 8):
            if Tablero[x][colTorre][0] == "v":
                movimientos.append((x, colTorre, "vacía"))
            else:
                if Tablero[x][colTorre][1] != colorTorre:
                    movimientos.append((x, colTorre, f"{Tablero[x][colTorre][0]} {Tablero[x][colTorre][1]}"))
                else:
                    movimientos.append((x, colTorre, "misma color"))
                break

    return movimientos

# Lista de piezas de ajedrez
piezas_validas = ["rey", "reina", "torre", "alfil", "caballo", "peón"]

# Solicitar el número de piezas a agregar
n = int(input("Ingrese la cantidad de piezas a agregar: "))

# Agregar las piezas
for _ in range(n):
    while True:
        tipo = input(f"Ingrese el tipo de pieza ({', '.join(piezas_validas)}): ").lower()
        if tipo in piezas_validas:
            break
        else:
            print("Tipo de pieza inválido. Intente nuevamente.")
    
    while True:
        color = input("Ingrese el color (blanco o negro): ").lower()
        if color in ["blanco", "negro"]:
            break
        else:
            print("Color inválido. Intente nuevamente.")
    
    while True:
        coordenada = input("Ingrese la posición (Ejemplo: a1, b2, c3, d4, e5, f6, g7, h8): ").lower()
        if len(coordenada) == 2 and coordenada[0] in "abcdefgh" and coordenada[1] in "12345678":
            if agregar_pieza(tipo, color, coordenada):
                break
            else:
                print("Posición inválida o ya ocupada. Intente nuevamente.")
        else:
            print("Posición inválida. Intente nuevamente.")

# Ingresar la pieza de la torre a evaluar
tipoTorre = "torre"
while True:
    colorTorre = input("Ingrese el color de la torre a evaluar (blanco o negro): ").lower()
    if colorTorre in ["blanco", "negro"]:
        break
    else:
        print("Color inválido. Intente nuevamente.")
        
while True:
    coordenadaTorre = input("Ingrese la posición (Ejemplo: a1, b2, c3, d4, e5, f6, g7, h8): ").lower()
    if len(coordenadaTorre) == 2 and coordenadaTorre[0] in "abcdefgh" and coordenadaTorre[1] in "12345678":
        filaTorre, colTorre = notacion_a_indices(coordenadaTorre)
        if es_posicion_valida(filaTorre, colTorre):
            Tablero[filaTorre][colTorre] = [tipoTorre, colorTorre]
            break
        else:
            print("Posición inválida para la torre o ya ocupada. Intente nuevamente.")
    else:
        print("Posición inválida. Intente nuevamente.")

# Mostrar todos los posibles movimientos válidos
movimientos = movimientos_torre(filaTorre, colTorre, colorTorre)
for movimiento in movimientos:
    fila, col, estado = movimiento
    print(f"{chr(col + ord('a'))}{8 - fila} {estado}")

# Imprimir matriz
for filaTablero in Tablero:
    print(filaTablero)
