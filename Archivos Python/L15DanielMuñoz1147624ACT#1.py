def obtener_area_triangulo(base, altura):
    area = (base * altura) / 2
    return area
def obtener_area_cuadrado(lado):
    area = lado ** 2
    return area
def obtener_area_rectangulo(base, altura):
    area = base * altura
    return area
def obtener_area_circulo(radio):
    area = 3,1416 * radio ** 2
    return area
def menu():
    print("1. Calcular área de un triángulo")
    print("2. Calcular área de un cuadrado")
    print("3. Calcular área de un rectángulo")
    print("4. Calcular área de un círculo")
    opcion = int(input("Seleccione una opción (1-4): "))
    if opcion == 1:
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        area = obtener_area_triangulo(base, altura)
        print("El área del triángulo es:", area)
    elif opcion == 2:
        lado = float(input("Ingrese el lado del cuadrado: "))
        area = obtener_area_cuadrado(lado)
        print("El área del cuadrado es:", area)
    elif opcion == 3:
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        area = obtener_area_rectangulo(base, altura)
        print("El área del rectángulo es:", area)
    elif opcion == 4:
        radio = float(input("Ingrese el radio del círculo: "))
        area = obtener_area_circulo(radio)
        print("El área del círculo es:", area)
    else:
        print("Opción no válida")
    # Ejecutar el menú
menu()
