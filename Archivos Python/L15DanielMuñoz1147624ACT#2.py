#Variables globales que se pueden acceder desde el programa principal y en las funciones
x = 0 
y = 0

#declaración de función, se utiliza la palabra "def" nombre de la función y entre () van los parametros o las entradas de la misma
def MoverPosicion(cantX, cantY):
    global x, y 
    x += cantX
    y += cantY

#Ciclo while para desplegar el menú de opciones
opcion = 'a'
while(opcion != 'e'):
    print("Menú")
    print("a. Sube","b. Baja","c. Izquierda","d. Derecha", "e. Salir", sep = "\t\n")
    opcion = input("ingrese su opción: ")

    match opcion:
        case 'a': #opción sube
            MoverPosicion(0,1) #para cada opción se manda a llamar la función creada anteriormente
        case 'b': #opción baja
            MoverPosicion(0,-1)
        case 'c':
            MoverPosicion(-1,0)
        case 'd':
            MoverPosicion(1,0)

    print(f"La poscición actual es: [{x}][{y}]")