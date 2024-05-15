import turtle

# Constante
ANCHOVENTANA = 1280
ALTOVENTANA = 720
INICIALTEXTO = (-400, 300)
INICIALNARRATIVA = (-420, -280)
ANCHO = 800
ALTO = 400

# Datos del niño
nombreniño = str(input("Por favor, ingresa el nombre del niño: "))
edadniño = int(input("Por favor, ingresa la edad del niño: "))
colorfavorito = str(input("Por favor, ingresa el color favorito del niño (entre rojo, azul, verde, morado o naranja): "))


if colorfavorito == "rojo":
    def escena1(tortuga, width, height, color):
        # Dibujar el marco 1
        tortuga.penup()
        tortuga.setpos(-450, 335)  
        tortuga.pendown()
        tortuga.color("black")
        for _ in range(2):
            tortuga.forward(900)  
            tortuga.right(90)
            tortuga.forward(500)  
            tortuga.right(90)

        # Dibujar el marco 2
        tortuga.penup()
        tortuga.setpos(-450, 280)  
        tortuga.pendown()
        tortuga.color("black")
        for _ in range(2):
            tortuga.forward(900)  
            tortuga.right(90)
            tortuga.forward(600)  
            tortuga.right(90)


        ventana = turtle.Screen()
        ventana.bgcolor("sky blue")
        tortuga.speed(40)
        tortuga.penup()
         # Dibujo del perro café
        tortuga.goto(-200, -100)
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del perro
        tortuga.end_fill()
        tortuga.penup()
          # Ojos y nariz del perro café
        tortuga.goto(-215, -50)
        tortuga.dot(10, "black")
        tortuga.goto(-185, -50)
        tortuga.dot(10, "black")
        tortuga.goto(-200, -70)
        tortuga.dot(5, "black")

        # Orejas del perro café
        tortuga.goto(-225, -30)
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(-175, -30)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del perro amarillo
        tortuga.goto(0, -100)
        tortuga.pendown()
        tortuga.color("yellow")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del perro
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del perro amarillo
        tortuga.goto(-15, -50)
        tortuga.dot(10, "black")
        tortuga.goto(15, -50)
        tortuga.dot(10, "black")
        tortuga.goto(0, -70)
        tortuga.dot(5, "black")
          # Orejas del perro amarillo
        tortuga.goto(-25, -30)
        tortuga.pendown()
        tortuga.color("yellow")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(25, -30)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del gato rojo
        tortuga.goto(200, -100)
        tortuga.pendown()
        tortuga.color("red")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del gato
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del gato rojo
        tortuga.goto(185, -50)
        tortuga.dot(10, "black")
        tortuga.goto(215, -50)
        tortuga.dot(10, "black")
        tortuga.goto(200, -70)
        tortuga.dot(5, "black")

        # Orejas del gato rojo
        tortuga.goto(225, -30)
        tortuga.pendown()
        tortuga.color("red")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(175, -30)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del primer árbol
        tortuga.goto(-300, 0)
        tortuga.color("brown")
        tortuga.pendown()
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(20)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(-290, 20)  # Posición ajustada para el follaje
        tortuga.pendown()
        tortuga.color("green")
        tortuga.begin_fill()
        tortuga.circle(40)
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del segundo árbol
        tortuga.goto(250, 0)
        tortuga.color("brown")
        tortuga.pendown()
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(20)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(260, 20)  # Posición ajustada para el follaje
        tortuga.pendown()
        tortuga.color("green")
        tortuga.begin_fill()
        tortuga.circle(40)
        tortuga.end_fill()
        tortuga.penup()
# Dibujo de unos arbustos
        for x in [-150, -120, -90, -60, 150, 180, 210, 240]:
            tortuga.goto(x, -130)
            tortuga.color("dark green")
            tortuga.pendown()
            tortuga.begin_fill()
            tortuga.circle(20)
            tortuga.end_fill()
            tortuga.penup()

        # Dibujo del sol amarillo
        tortuga.goto(-350, 160)
        tortuga.color("yellow")
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(50)
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo de las nubes
        for x, y in [(0, 205), (200, 185), (-200,190)]:
            tortuga.goto(x, y)
            tortuga.color("white")
            tortuga.pendown()
            tortuga.begin_fill()
            tortuga.circle(30)
            tortuga.end_fill()
            tortuga.penup()
            tortuga.goto(x + 45, y)
            tortuga.pendown()
            tortuga.begin_fill()
            tortuga.circle(30)
            tortuga.end_fill()
            tortuga.penup()
            
             # Finalizar y mostrar ventana
        tortuga.hideturtle()
        tortuga.stamp()
        tortuga.penup()

    def escena2(tortuga, width, height, color):

        # Dibujar el marco 1
        tortuga.penup()
        tortuga.setpos(-450, 335)  
        tortuga.pendown()
        tortuga.color("black")
        for _ in range(2):
            tortuga.forward(900)  
            tortuga.right(90)
            tortuga.forward(500)  
            tortuga.right(90)

        # Dibujar el marco 2
        tortuga.penup()
        tortuga.setpos(-450, 280)  
        tortuga.pendown()
        tortuga.color("black")
        for _ in range(2):
            tortuga.forward(900)  
            tortuga.right(90)
            tortuga.forward(600)  
            tortuga.right(90)


            ventana = turtle.Screen()
            ventana.bgcolor("sky blue")
            tortuga.speed(40)
        tortuga.penup()
            

        # Dibujo de la primera casa
        # Cuerpo de la casa
        tortuga.goto(-350, -100)
        tortuga.pendown()
        tortuga.fillcolor("orange")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(100)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        # Techo de la casa
        tortuga.goto(-350, 0)
        tortuga.pendown()
        tortuga.fillcolor("green")
        tortuga.begin_fill()
        for _ in range(3):
            tortuga.forward(100)
            tortuga.left(120)
        tortuga.end_fill()
        tortuga.penup()

        # Ventanas
        tortuga.goto(-340, -40)  # Ajuste de coordenada x de la ventana izquierda
        tortuga.pendown()
        tortuga.fillcolor("sky blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(30)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        tortuga.goto(-290, -40)  # Ajuste de coordenada x de la ventana derecha
        tortuga.pendown()
        tortuga.fillcolor("sky blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(30)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        # Puerta
        tortuga.goto(-310, -60)  # Ajuste de coordenada x de la puerta
        tortuga.pendown()
        tortuga.fillcolor("brown")
        tortuga.begin_fill()
        for _ in range(2):
            tortuga.forward(20)
            tortuga.right(90)
            tortuga.forward(40)
            tortuga.right(90)
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo de la cuarta casa
        # Cuerpo de la casa
        tortuga.goto(-175, 0)
        tortuga.pendown()
        tortuga.fillcolor("orange")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(100)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        # Techo de la casa
        tortuga.goto(-175, 100)
        tortuga.pendown()
        tortuga.fillcolor("green")
        tortuga.begin_fill()
        for _ in range(3):
            tortuga.forward(100)
            tortuga.left(120)
        tortuga.end_fill()
        tortuga.penup()

        # Ventanas
        tortuga.goto(-165, 60)  # Ajuste de coordenada x de la ventana izquierda
        tortuga.pendown()
        tortuga.fillcolor("sky blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(30)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        tortuga.goto(-115, 60)  # Ajuste de coordenada x de la ventana derecha
        tortuga.pendown()
        tortuga.fillcolor("sky blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(30)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        # Puerta
        tortuga.goto(-135, 40)  # Ajuste de coordenada x de la puerta
        tortuga.pendown()
        tortuga.fillcolor("brown")
        tortuga.begin_fill()
        for _ in range(2):
            tortuga.forward(20)
            tortuga.right(90)
            tortuga.forward(40)
            tortuga.right(90)
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo de la segunda casa
        # Cuerpo de la casa
        tortuga.goto(300, -100)
        tortuga.pendown()
        tortuga.fillcolor("orange")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(100)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        # Techo de la casa
        tortuga.goto(300, 0)
        tortuga.pendown()
        tortuga.fillcolor("green")
        tortuga.begin_fill()
        for _ in range(3):
            tortuga.forward(100)
            tortuga.left(120)
        tortuga.end_fill()
        tortuga.penup()

        # Ventanas
        tortuga.goto(310, -40)  # Ajuste de coordenada x de la ventana izquierda
        tortuga.pendown()
        tortuga.fillcolor("sky blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(30)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        tortuga.goto(360, -40)  # Ajuste de coordenada x de la ventana derecha
        tortuga.pendown()
        tortuga.fillcolor("sky blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(30)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        # Puerta
        tortuga.goto(340, -60)  # Ajuste de coordenada x de la puerta
        tortuga.pendown()
        tortuga.fillcolor("brown")
        tortuga.begin_fill()
        for _ in range(2):
            tortuga.forward(20)
            tortuga.right(90)
            tortuga.forward(40)
            tortuga.right(90)
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo de la tercera casa
        # Cuerpo de la casa
        tortuga.goto(150, 0)
        tortuga.pendown()
        tortuga.fillcolor("orange")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(100)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        # Techo de la casa
        tortuga.goto(150, 100)
        tortuga.pendown()
        tortuga.fillcolor("green")
        tortuga.begin_fill()
        for _ in range(3):
            tortuga.forward(100)
            tortuga.left(120)
        tortuga.end_fill()
        tortuga.penup()

        # Ventanas
        tortuga.goto(160, 60)  # Ajuste de coordenada x de la ventana izquierda
        tortuga.pendown()
        tortuga.fillcolor("sky blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(30)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        tortuga.goto(210, 60)  # Ajuste de coordenada x de la ventana derecha
        tortuga.pendown()
        tortuga.fillcolor("sky blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(30)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        # Puerta
        tortuga.goto(190, 40)  # Ajuste de coordenada x de la puerta
        tortuga.pendown()
        tortuga.fillcolor("brown")
        tortuga.begin_fill()
        for _ in range(2):
            tortuga.forward(20)
            tortuga.right(90)
            tortuga.forward(40)
            tortuga.right(90)
        tortuga.end_fill()
        tortuga.penup()

         # Dibujo del perro café
        tortuga.goto(-200, -100)
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del perro
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del perro café
        tortuga.goto(-215, -50)
        tortuga.dot(10, "black")
        tortuga.goto(-185, -50)
        tortuga.dot(10, "black")
        tortuga.goto(-200, -70)
        tortuga.dot(5, "black")

        # Orejas del perro café
        tortuga.goto(-225, -30)
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(-175, -30)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del perro amarillo
        tortuga.goto(0, -100)
        tortuga.pendown()
        tortuga.color("yellow")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del perro
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del perro amarillo
        tortuga.goto(-15, -50)
        tortuga.dot(10, "black")
        tortuga.goto(15, -50)
        tortuga.dot(10, "black")
        tortuga.goto(0, -70)
        tortuga.dot(5, "black")

        # Orejas del perro amarillo
        tortuga.goto(-25, -30)
        tortuga.pendown()
        tortuga.color("yellow")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(25, -30)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del gato rojo
        tortuga.goto(200, -100)
        tortuga.pendown()
        tortuga.color("red")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del gato
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del gato rojo
        tortuga.goto(185, -50)
        tortuga.dot(10, "black")
        tortuga.goto(215, -50)
        tortuga.dot(10, "black")
        tortuga.goto(200, -70)
        tortuga.dot(5, "black")

        # Orejas del gato rojo
        tortuga.goto(225, -30)
        tortuga.pendown()
        tortuga.color("red")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(175, -30)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo de las nubes
        for x, y in [(0, 205), (200, 185), (-200,190)]:
            tortuga.goto(x, y)
            tortuga.color("white")
            tortuga.pendown()
            tortuga.begin_fill()
            tortuga.circle(30)
            tortuga.end_fill()
            tortuga.penup()
            tortuga.goto(x + 45, y)
            tortuga.pendown()
            tortuga.begin_fill()
            tortuga.circle(30)
            tortuga.end_fill()
            tortuga.penup()

        # Dibujo del sol amarillo
        tortuga.goto(-350, 160)
        tortuga.color("yellow")
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(50)
        tortuga.end_fill()
        tortuga.penup()
        

        # Finalizar y mostrar ventana
        tortuga.hideturtle()
        tortuga.stamp()
        tortuga.penup()
    
    def escena3(tortuga, width, height, color):

        # Dibujar el marco 1
        tortuga.penup()
        tortuga.setpos(-450, 335)  
        tortuga.pendown()
        tortuga.color("black")
        for _ in range(2):
            tortuga.forward(900)  
            tortuga.right(90)
            tortuga.forward(500)  
            tortuga.right(90)

        # Dibujar el marco 2
        tortuga.penup()
        tortuga.setpos(-450, 280) 
        tortuga.pendown()
        tortuga.color("black")
        for _ in range(2):
            tortuga.forward(900)  
            tortuga.right(90)
            tortuga.forward(600)  
            tortuga.right(90)

            ventana = turtle.Screen()
            ventana.bgcolor("skyblue")  # Fondo blanco para mejor contraste
            tortuga.speed(30)
        tortuga.penup()

        # Dibuja un charco en forma ovalada más grande
        tortuga.penup()
        tortuga.goto(0, -100)  # Ajusta la posición inicial del charco hacia abajo para más espacio
        tortuga.pendown()
        tortuga.color("blue")
        tortuga.begin_fill()
        tortuga.left(45)  # Inclina la elipse para el charco
        for _ in range(2):  # Dibuja una elipse más grande
            tortuga.circle(150, 90)  # Aumenta el radio largo de la elipse
            tortuga.circle(150//2, 90)  # Aumenta el radio corto de la elipse
        tortuga.end_fill()
        tortuga.penup()

        # Dibuja las piedras
        # Primera piedra
        tortuga.penup()
        tortuga.goto(-90, 10)  # Ajusta la posición para que coincida con el charco más grande
        tortuga.pendown()
        tortuga.color("gray")
        tortuga.begin_fill()
        tortuga.circle(20)  # Tamaño de la primera piedra
        tortuga.end_fill()
        tortuga.penup()

        # Segunda piedra
        tortuga.penup()
        tortuga.goto(-40, -20)  # Ajusta la posición para que coincida con el charco más grande
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(15)  # Tamaño de la segunda piedra
        tortuga.end_fill()
        tortuga.penup()

        # Tercera piedra
        tortuga.penup()
        tortuga.goto(10, -5)  # Ajusta la posición para que coincida con el charco más grande
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(15)  # Tamaño de la tercera piedra
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del perro café
        tortuga.goto(-200, -100)
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del perro
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del perro café
        tortuga.goto(-240, -50)
        tortuga.dot(10, "black")
        tortuga.goto(-210, -50)
        tortuga.dot(10, "black")
        tortuga.goto(-225, -70)
        tortuga.dot(5, "black")

        # Orejas del perro café
        tortuga.goto(-245, -40)
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(-200, -40)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del perro amarillo
        tortuga.goto(-300, 0)
        tortuga.pendown()
        tortuga.color("yellow")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del perro
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del perro amarillo
        tortuga.goto(-340, 45)
        tortuga.dot(10, "black")
        tortuga.goto(-310, 45)
        tortuga.dot(10, "black")
        tortuga.goto(-325, 30)
        tortuga.dot(5, "black")

        # Orejas del perro amarillo
        tortuga.goto(-355, 50)
        tortuga.pendown()
        tortuga.color("yellow")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(-285, 50)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del gato rojo
        tortuga.goto(-150, 0)
        tortuga.pendown()
        tortuga.color("red")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del gato
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del gato rojo
        tortuga.goto(-190, 45)
        tortuga.dot(10, "black")
        tortuga.goto(-160, 45)
        tortuga.dot(10, "black")
        tortuga.goto(-175, 30)
        tortuga.dot(5, "black")

        # Orejas del gato rojo
        tortuga.goto(-205, 50)
        tortuga.pendown()
        tortuga.color("red")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(-135, 50)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo de las nubes
        for x, y in [(0, 205), (200, 185), (-200,190)]:
            tortuga.goto(x, y)
            tortuga.color("white")
            tortuga.pendown()
            tortuga.begin_fill()
            tortuga.circle(30)
            tortuga.end_fill()
            tortuga.penup()
            tortuga.goto(x + 45, y)
            tortuga.pendown()
            tortuga.begin_fill()
            tortuga.circle(30)
            tortuga.end_fill()
            tortuga.penup()

        # Dibujo del sol amarillo
        tortuga.goto(-350, 160)
        tortuga.color("yellow")
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(50)
        tortuga.end_fill()
        tortuga.penup()

        tortuga.hideturtle()
        tortuga.stamp()
        tortuga.penup()

    def escena4(tortuga, width, height, color):

        # Dibujar el marco 1
        tortuga.penup()
        tortuga.setpos(-450, 335)  
        tortuga.pendown()
        tortuga.color("black")
        for _ in range(2):
            tortuga.forward(900)  
            tortuga.right(90)
            tortuga.forward(500)  
            tortuga.right(90)

        # Dibujar el marco 2
        tortuga.penup()
        tortuga.setpos(-450, 280)  
        tortuga.pendown()
        tortuga.color("black")
        for _ in range(2):
            tortuga.forward(900)  
            tortuga.right(90)
            tortuga.forward(600)  
            tortuga.right(90)
            ventana = turtle.Screen()
            ventana.bgcolor("gray")
            tortuga.speed(40)
        tortuga.penup()

        # Dibujo de la primera casa
        # Cuerpo de la casa
        tortuga.goto(-350, -100)
        tortuga.pendown()
        tortuga.fillcolor("pink")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(100)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        # Techo de la casa
        tortuga.goto(-350, 0)
        tortuga.pendown()
        tortuga.fillcolor("purple")
        tortuga.begin_fill()
        for _ in range(3):
            tortuga.forward(100)
            tortuga.left(120)
        tortuga.end_fill()
        tortuga.penup()

        # Ventanas
        tortuga.goto(-340, -40)  # Ajuste de coordenada x de la ventana izquierda
        tortuga.pendown()
        tortuga.fillcolor("sky blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(30)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        tortuga.goto(-290, -40)  # Ajuste de coordenada x de la ventana derecha
        tortuga.pendown()
        tortuga.fillcolor("sky blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(30)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        # Puerta
        tortuga.goto(-310, -60)  # Ajuste de coordenada x de la puerta
        tortuga.pendown()
        tortuga.fillcolor("brown")
        tortuga.begin_fill()
        for _ in range(2):
            tortuga.forward(20)
            tortuga.right(90)
            tortuga.forward(40)
            tortuga.right(90)
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo de las nubes
        for x, y in [(0, 205), (200, 185), (-200, 190)]:
            for offset in [0, 45]:  # Dibuja dos partes de cada nube
                tortuga.goto(x + offset, y)
                tortuga.color("white")
                tortuga.pendown()
                tortuga.begin_fill()
                tortuga.circle(30)
                tortuga.end_fill()
                tortuga.penup()

        # Agregar lluvia
        tortuga.color("blue")
        for x, y in [(0, 205), (200, 185), (-200, 190)]:
            for offset in [0, 45]:  # Agrega lluvia debajo de cada parte de la nube
                for i in range(-10, 10, 5):  # Varias gotas de lluvia por nube
                    tortuga.goto(x + offset + i, y - 30)  # Posición inicial de la lluvia
                    tortuga.pendown()
                    tortuga.right(90)  # Asegura que la tortuga apunte hacia abajo
                    tortuga.forward(20)  # Longitud de la lluvia
                    tortuga.penup()
                    tortuga.left(90)  # Reestablece la orientación de la tortuga


        # Dibujo del perro café
        tortuga.goto(-200, -100)
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del perro
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del perro café
        tortuga.goto(-215, -50)
        tortuga.dot(10, "black")
        tortuga.goto(-185, -50)
        tortuga.dot(10, "black")
        tortuga.goto(-200, -70)
        tortuga.dot(10, "black")
        tortuga.goto(-200, -90)
        tortuga.dot(12, "black")

        # Orejas del perro café
        tortuga.goto(-225, -30)
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(-175, -30)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del perro amarillo
        tortuga.goto(0, -100)
        tortuga.pendown()
        tortuga.color("yellow")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del perro
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del perro amarillo
        tortuga.goto(-15, -50)
        tortuga.dot(10, "black")
        tortuga.goto(15, -50)
        tortuga.dot(10, "black")
        tortuga.goto(0, -70)
        tortuga.dot(5, "black")

        # Orejas del perro amarillo
        tortuga.goto(-25, -30)
        tortuga.pendown()
        tortuga.color("yellow")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(25, -30)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del gato rojo
        tortuga.goto(200, -100)
        tortuga.pendown()
        tortuga.color("red")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del gato
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del gato rojo
        tortuga.goto(185, -50)
        tortuga.dot(10, "black")
        tortuga.goto(215, -50)
        tortuga.dot(10, "black")
        tortuga.goto(200, -70)
        tortuga.dot(5, "black")

        # Orejas del gato rojo
        tortuga.goto(225, -30)
        tortuga.pendown()
        tortuga.color("red")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(175, -30)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        tortuga.hideturtle()
        tortuga.stamp()
        tortuga.penup()
    def escena5(tortuga, width, height, color):

        # Dibujar el marco 1
        tortuga.penup()
        tortuga.setpos(-450, 335)  
        tortuga.pendown()
        tortuga.color("black")
        for _ in range(2):
            tortuga.forward(900)  
            tortuga.right(90)
            tortuga.forward(500)  
            tortuga.right(90)

        # Dibujar el marco 2
        tortuga.penup()
        tortuga.setpos(-450, 280)  
        tortuga.pendown()
        tortuga.color("black")
        for _ in range(2):
            tortuga.forward(900)  
            tortuga.right(90)
            tortuga.forward(600)  
            tortuga.right(90)


            ventana = turtle.Screen()
            ventana.bgcolor("sky blue")
            tortuga.speed(40)
        tortuga.penup()

        # Dibujo del perro café
        tortuga.goto(-200, -100)
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del perro
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del perro café
        tortuga.goto(-205, -40)
        tortuga.dot(10, "black")
        tortuga.goto(-185, -40)
        tortuga.dot(10, "black")
        tortuga.goto(-190, -55)
        tortuga.dot(5, "black")
        tortuga.goto(-190, -70)
        tortuga.dot(10, "black")

        # Orejas del perro café
        tortuga.goto(-235, -40)
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(-170, -40)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del perro amarillo
        tortuga.goto(-300, 0)
        tortuga.pendown()
        tortuga.color("yellow")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del perro
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del perro amarillo
        tortuga.goto(-305, 60)
        tortuga.dot(10, "black")
        tortuga.goto(-290, 60)
        tortuga.dot(10, "black")
        tortuga.goto(-295, 50)
        tortuga.dot(5, "black")
        tortuga.goto(-295, 35)
        tortuga.dot(10, "black")

        # Orejas del perro amarillo
        tortuga.goto(-335, 65)
        tortuga.pendown()
        tortuga.color("yellow")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(-275, 65)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del gato rojo
        tortuga.goto(-142, 0)
        tortuga.pendown()
        tortuga.color("red")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del gato
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del gato rojo
        tortuga.goto(-145, 60)
        tortuga.dot(10, "black")
        tortuga.goto(-125, 60)
        tortuga.dot(10, "black")
        tortuga.goto(-130, 50)
        tortuga.dot(5, "black")
        tortuga.goto(-130, 35)
        tortuga.dot(10, "black")

        # Orejas del gato rojo
        tortuga.goto(-175, 65)
        tortuga.pendown()
        tortuga.color("red")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(-120, 65)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibuja dos pizzas pequeñas
        tortuga.penup()
        tortuga.goto(-50, -50)  # Posición de la primera pizza
        tortuga.pendown()
        tortuga.color("sandy brown")
        tortuga.begin_fill()
        tortuga.circle(40)  # Radio para una pizza pequeña
        tortuga.end_fill()

        # Toppings para la primera pizza
        tortuga.penup()
        tortuga.goto(-60, 10)
        tortuga.color("red")
        for _ in range(2):  # Simula algunos pepperonis
            tortuga.dot(10)
            tortuga.forward(20)
        tortuga.penup()
        tortuga.goto(-60, 0)
        tortuga.color("red")
        for _ in range(2):  # Simula algunos pepperonis
            tortuga.dot(10)
            tortuga.forward(20)
        tortuga.penup()
        tortuga.goto(-60, -10)
        tortuga.color("red")
        for _ in range(2):  # Simula algunos pepperonis
            tortuga.dot(10)
            tortuga.forward(20)
        tortuga.penup()
        tortuga.goto(-60, -20)
        tortuga.color("red")
        for _ in range(2):  # Simula algunos pepperonis
            tortuga.dot(10)
            tortuga.forward(20)
        tortuga.penup()
        tortuga.goto(-60, -30)
        tortuga.color("red")
        for _ in range(2):  # Simula algunos pepperonis
            tortuga.dot(10)
            tortuga.forward(20)
        # Segunda pizza
        tortuga.penup()
        tortuga.goto(40, -50)  # Posición de la segunda pizza
        tortuga.pendown()
        tortuga.color("sandy brown")
        tortuga.begin_fill()
        tortuga.circle(40)  # Radio para la segunda pizza pequeña
        tortuga.end_fill()

        # Toppings para la segunda pizza
        tortuga.penup()
        tortuga.goto(30, 10)
        tortuga.color("red")
        for _ in range(2):  # Simula algunos pepperonis
            tortuga.dot(10)
            tortuga.forward(20)
        tortuga.penup()
        tortuga.goto(30, 0)
        tortuga.color("red")
        for _ in range(2):  # Simula algunos pepperonis
            tortuga.dot(10)
            tortuga.forward(20)
        tortuga.penup()
        tortuga.goto(30, -10)
        tortuga.color("red")
        for _ in range(2):  # Simula algunos pepperonis
            tortuga.dot(10)
            tortuga.forward(20)
        tortuga.penup()
        tortuga.goto(30, -20)
        tortuga.color("red")
        for _ in range(2):  # Simula algunos pepperonis
            tortuga.dot(10)
            tortuga.forward(20)
        tortuga.penup()
        tortuga.goto(30, -30)
        tortuga.color("red")
        for _ in range(2):  # Simula algunos pepperonis
            tortuga.dot(10)
            tortuga.forward(20)

       # Dibuja el edificio principal
        tortuga.penup()
        tortuga.goto(100, -100)  # Nueva posición ajustada para la base del edificio
        tortuga.pendown()
        tortuga.color("yellow")  # Color del edificio
        tortuga.begin_fill()
        for _ in range(2):  # Crea un rectángulo
            tortuga.forward(300)
            tortuga.left(90)
            tortuga.forward(200)
            tortuga.left(90)
        tortuga.end_fill()

        # Dibuja el techo
        tortuga.penup()
        tortuga.goto(100, 100)
        tortuga.pendown()
        tortuga.color("red")  # Color del techo
        tortuga.begin_fill()
        tortuga.goto(250, 150)  # Punto medio del techo
        tortuga.goto(400, 100)  # Completa el triángulo del techo
        tortuga.goto(100, 100)
        tortuga.end_fill()

        # Dibuja una puerta
        tortuga.penup()
        tortuga.goto(220, -100)  # Posición de la puerta ajustada
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        for _ in range(2):
            tortuga.forward(50)
            tortuga.left(90)
            tortuga.forward(80)
            tortuga.left(90)
        tortuga.end_fill()

        # Dibuja ventanas
        tortuga.penup()
        tortuga.goto(125, -20)  # Ventana izquierda ajustada
        tortuga.pendown()
        tortuga.color("blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(40)
            tortuga.left(90)
        tortuga.end_fill()

        tortuga.penup()
        tortuga.goto(325, -20)  # Ventana derecha ajustada
        tortuga.pendown()
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(40)
            tortuga.left(90)
        tortuga.end_fill()

        # Dibuja el letrero de la pizzería
        tortuga.penup()
        tortuga.goto(210, 100)  # Posición del letrero ajustada
        tortuga.pendown()
        tortuga.color("white")
        tortuga.write("Pizzería", font=("Arial", 18, "bold"))
        tortuga.penup()

        # Dibujo de las nubes
        for x, y in [(0, 205), (200, 185), (-200,190)]:
            tortuga.goto(x, y)
            tortuga.color("white")
            tortuga.pendown()
            tortuga.begin_fill()
            tortuga.circle(30)
            tortuga.end_fill()
            tortuga.penup()
            tortuga.goto(x + 45, y)
            tortuga.pendown()
            tortuga.begin_fill()
            tortuga.circle(30)
            tortuga.end_fill()
            tortuga.penup()

        # Dibujo del sol amarillo
        tortuga.goto(-350, 160)
        tortuga.color("yellow")
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(50)
        tortuga.end_fill()
        tortuga.penup()

        tortuga.hideturtle()
        tortuga.stamp()
        tortuga.penup()
if colorfavorito == "azul":
    def escena1(tortuga, width, height, color):
        # Dibujar el marco 1
        tortuga.penup()
        tortuga.setpos(-450, 335)  
        tortuga.pendown()
        tortuga.color("black")
        for _ in range(2):
            tortuga.forward(900)  
            tortuga.right(90)
            tortuga.forward(500)  
            tortuga.right(90)

        # Dibujar el marco 2
        tortuga.penup()
        tortuga.setpos(-450, 280)  # Start from the top-left corner
        tortuga.pendown()
        tortuga.color("black")
        for _ in range(2):
            tortuga.forward(900)  
            tortuga.right(90)
            tortuga.forward(600)  
            tortuga.right(90)


        ventana = turtle.Screen()
        ventana.bgcolor("sky blue")
        tortuga.speed(40)
        tortuga.penup()
         # Dibujo del perro café
        tortuga.goto(-200, -100)
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del perro
        tortuga.end_fill()
        tortuga.penup()
          # Ojos y nariz del perro café
        tortuga.goto(-215, -50)
        tortuga.dot(10, "black")
        tortuga.goto(-185, -50)
        tortuga.dot(10, "black")
        tortuga.goto(-200, -70)
        tortuga.dot(5, "black")

        # Orejas del perro café
        tortuga.goto(-225, -30)
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(-175, -30)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del perro amarillo
        tortuga.goto(0, -100)
        tortuga.pendown()
        tortuga.color("yellow")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del perro
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del perro amarillo
        tortuga.goto(-15, -50)
        tortuga.dot(10, "black")
        tortuga.goto(15, -50)
        tortuga.dot(10, "black")
        tortuga.goto(0, -70)
        tortuga.dot(5, "black")
          # Orejas del perro amarillo
        tortuga.goto(-25, -30)
        tortuga.pendown()
        tortuga.color("yellow")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(25, -30)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del gato rojo
        tortuga.goto(200, -100)
        tortuga.pendown()
        tortuga.color("blue")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del gato
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del gato rojo
        tortuga.goto(185, -50)
        tortuga.dot(10, "black")
        tortuga.goto(215, -50)
        tortuga.dot(10, "black")
        tortuga.goto(200, -70)
        tortuga.dot(5, "black")

        # Orejas del gato rojo
        tortuga.goto(225, -30)
        tortuga.pendown()
        tortuga.color("blue")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(175, -30)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del primer árbol
        tortuga.goto(-300, 0)
        tortuga.color("brown")
        tortuga.pendown()
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(20)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(-290, 20)  # Posición ajustada para el follaje
        tortuga.pendown()
        tortuga.color("green")
        tortuga.begin_fill()
        tortuga.circle(40)
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del segundo árbol
        tortuga.goto(250, 0)
        tortuga.color("brown")
        tortuga.pendown()
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(20)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(260, 20)  # Posición ajustada para el follaje
        tortuga.pendown()
        tortuga.color("green")
        tortuga.begin_fill()
        tortuga.circle(40)
        tortuga.end_fill()
        tortuga.penup()
        # Dibujo de unos arbustos
        for x in [-150, -120, -90, -60, 150, 180, 210, 240]:
            tortuga.goto(x, -130)
            tortuga.color("dark green")
            tortuga.pendown()
            tortuga.begin_fill()
            tortuga.circle(20)
            tortuga.end_fill()
            tortuga.penup()

        # Dibujo del sol amarillo
        tortuga.goto(-350, 160)
        tortuga.color("yellow")
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(50)
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo de las nubes
        for x, y in [(0, 205), (200, 185), (-200,190)]:
            tortuga.goto(x, y)
            tortuga.color("white")
            tortuga.pendown()
            tortuga.begin_fill()
            tortuga.circle(30)
            tortuga.end_fill()
            tortuga.penup()
            tortuga.goto(x + 45, y)
            tortuga.pendown()
            tortuga.begin_fill()
            tortuga.circle(30)
            tortuga.end_fill()
            tortuga.penup()
            
             # Finalizar y mostrar ventana
        tortuga.hideturtle()
        tortuga.stamp()
        tortuga.penup()

    def escena2(tortuga, width, height, color):

        # Dibujar el marco 1
        tortuga.penup()
        tortuga.setpos(-450, 335)  
        tortuga.pendown()
        tortuga.color("black")
        for _ in range(2):
            tortuga.forward(900)  
            tortuga.right(90)
            tortuga.forward(500)  
            tortuga.right(90)

        # Dibujar el marco 2
        tortuga.penup()
        tortuga.setpos(-450, 280)  
        tortuga.pendown()
        tortuga.color("black")
        for _ in range(2):
            tortuga.forward(900)  
            tortuga.right(90)
            tortuga.forward(600)  
            tortuga.right(90)


            ventana = turtle.Screen()
            ventana.bgcolor("sky blue")
            tortuga.speed(40)
        tortuga.penup()
            

        # Dibujo de la primera casa
        # Cuerpo de la casa
        tortuga.goto(-350, -100)
        tortuga.pendown()
        tortuga.fillcolor("orange")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(100)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        # Techo de la casa
        tortuga.goto(-350, 0)
        tortuga.pendown()
        tortuga.fillcolor("green")
        tortuga.begin_fill()
        for _ in range(3):
            tortuga.forward(100)
            tortuga.left(120)
        tortuga.end_fill()
        tortuga.penup()

        # Ventanas
        tortuga.goto(-340, -40)  # Ajuste de coordenada x de la ventana izquierda
        tortuga.pendown()
        tortuga.fillcolor("sky blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(30)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        tortuga.goto(-290, -40)  # Ajuste de coordenada x de la ventana derecha
        tortuga.pendown()
        tortuga.fillcolor("sky blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(30)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        # Puerta
        tortuga.goto(-310, -60)  # Ajuste de coordenada x de la puerta
        tortuga.pendown()
        tortuga.fillcolor("brown")
        tortuga.begin_fill()
        for _ in range(2):
            tortuga.forward(20)
            tortuga.right(90)
            tortuga.forward(40)
            tortuga.right(90)
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo de la cuarta casa
        # Cuerpo de la casa
        tortuga.goto(-175, 0)
        tortuga.pendown()
        tortuga.fillcolor("orange")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(100)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        # Techo de la casa
        tortuga.goto(-175, 100)
        tortuga.pendown()
        tortuga.fillcolor("green")
        tortuga.begin_fill()
        for _ in range(3):
            tortuga.forward(100)
            tortuga.left(120)
        tortuga.end_fill()
        tortuga.penup()

        # Ventanas
        tortuga.goto(-165, 60)  # Ajuste de coordenada x de la ventana izquierda
        tortuga.pendown()
        tortuga.fillcolor("sky blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(30)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        tortuga.goto(-115, 60)  # Ajuste de coordenada x de la ventana derecha
        tortuga.pendown()
        tortuga.fillcolor("sky blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(30)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        # Puerta
        tortuga.goto(-135, 40)  # Ajuste de coordenada x de la puerta
        tortuga.pendown()
        tortuga.fillcolor("brown")
        tortuga.begin_fill()
        for _ in range(2):
            tortuga.forward(20)
            tortuga.right(90)
            tortuga.forward(40)
            tortuga.right(90)
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo de la segunda casa
        # Cuerpo de la casa
        tortuga.goto(300, -100)
        tortuga.pendown()
        tortuga.fillcolor("orange")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(100)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        # Techo de la casa
        tortuga.goto(300, 0)
        tortuga.pendown()
        tortuga.fillcolor("green")
        tortuga.begin_fill()
        for _ in range(3):
            tortuga.forward(100)
            tortuga.left(120)
        tortuga.end_fill()
        tortuga.penup()

        # Ventanas
        tortuga.goto(310, -40)  # Ajuste de coordenada x de la ventana izquierda
        tortuga.pendown()
        tortuga.fillcolor("sky blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(30)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        tortuga.goto(360, -40)  # Ajuste de coordenada x de la ventana derecha
        tortuga.pendown()
        tortuga.fillcolor("sky blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(30)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        # Puerta
        tortuga.goto(340, -60)  # Ajuste de coordenada x de la puerta
        tortuga.pendown()
        tortuga.fillcolor("brown")
        tortuga.begin_fill()
        for _ in range(2):
            tortuga.forward(20)
            tortuga.right(90)
            tortuga.forward(40)
            tortuga.right(90)
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo de la tercera casa
        # Cuerpo de la casa
        tortuga.goto(150, 0)
        tortuga.pendown()
        tortuga.fillcolor("orange")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(100)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        # Techo de la casa
        tortuga.goto(150, 100)
        tortuga.pendown()
        tortuga.fillcolor("green")
        tortuga.begin_fill()
        for _ in range(3):
            tortuga.forward(100)
            tortuga.left(120)
        tortuga.end_fill()
        tortuga.penup()

        # Ventanas
        tortuga.goto(160, 60)  # Ajuste de coordenada x de la ventana izquierda
        tortuga.pendown()
        tortuga.fillcolor("sky blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(30)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        tortuga.goto(210, 60)  # Ajuste de coordenada x de la ventana derecha
        tortuga.pendown()
        tortuga.fillcolor("sky blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(30)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        # Puerta
        tortuga.goto(190, 40)  # Ajuste de coordenada x de la puerta
        tortuga.pendown()
        tortuga.fillcolor("brown")
        tortuga.begin_fill()
        for _ in range(2):
            tortuga.forward(20)
            tortuga.right(90)
            tortuga.forward(40)
            tortuga.right(90)
        tortuga.end_fill()
        tortuga.penup()

         # Dibujo del perro café
        tortuga.goto(-200, -100)
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del perro
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del perro café
        tortuga.goto(-215, -50)
        tortuga.dot(10, "black")
        tortuga.goto(-185, -50)
        tortuga.dot(10, "black")
        tortuga.goto(-200, -70)
        tortuga.dot(5, "black")

        # Orejas del perro café
        tortuga.goto(-225, -30)
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(-175, -30)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del perro amarillo
        tortuga.goto(0, -100)
        tortuga.pendown()
        tortuga.color("yellow")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del perro
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del perro amarillo
        tortuga.goto(-15, -50)
        tortuga.dot(10, "black")
        tortuga.goto(15, -50)
        tortuga.dot(10, "black")
        tortuga.goto(0, -70)
        tortuga.dot(5, "black")

        # Orejas del perro amarillo
        tortuga.goto(-25, -30)
        tortuga.pendown()
        tortuga.color("yellow")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(25, -30)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del gato rojo
        tortuga.goto(200, -100)
        tortuga.pendown()
        tortuga.color("blue")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del gato
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del gato rojo
        tortuga.goto(185, -50)
        tortuga.dot(10, "black")
        tortuga.goto(215, -50)
        tortuga.dot(10, "black")
        tortuga.goto(200, -70)
        tortuga.dot(5, "black")

        # Orejas del gato rojo
        tortuga.goto(225, -30)
        tortuga.pendown()
        tortuga.color("blue")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(175, -30)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo de las nubes
        for x, y in [(0, 205), (200, 185), (-200,190)]:
            tortuga.goto(x, y)
            tortuga.color("white")
            tortuga.pendown()
            tortuga.begin_fill()
            tortuga.circle(30)
            tortuga.end_fill()
            tortuga.penup()
            tortuga.goto(x + 45, y)
            tortuga.pendown()
            tortuga.begin_fill()
            tortuga.circle(30)
            tortuga.end_fill()
            tortuga.penup()

        # Dibujo del sol amarillo
        tortuga.goto(-350, 160)
        tortuga.color("yellow")
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(50)
        tortuga.end_fill()
        tortuga.penup()
        

        # Finalizar y mostrar ventana
        tortuga.hideturtle()
        tortuga.stamp()
        tortuga.penup()
    
    def escena3(tortuga, width, height, color):

        # Dibujar el marco 1
        tortuga.penup()
        tortuga.setpos(-450, 335)  
        tortuga.pendown()
        tortuga.color("black")
        for _ in range(2):
            tortuga.forward(900)  
            tortuga.right(90)
            tortuga.forward(500)  
            tortuga.right(90)

        # Dibujar el marco 2
        tortuga.penup()
        tortuga.setpos(-450, 280)  
        tortuga.pendown()
        tortuga.color("black")
        for _ in range(2):
            tortuga.forward(900)  
            tortuga.right(90)
            tortuga.forward(600)  
            tortuga.right(90)

            ventana = turtle.Screen()
            ventana.bgcolor("skyblue")  # Fondo celeste para mejor contraste
            tortuga.speed(30)
        tortuga.penup()

        # Dibuja un charco en forma ovalada más grande
        tortuga.penup()
        tortuga.goto(0, -100)  # Ajusta la posición inicial del charco hacia abajo para más espacio
        tortuga.pendown()
        tortuga.color("blue")
        tortuga.begin_fill()
        tortuga.left(45)  # Inclina la elipse para el charco
        for _ in range(2):  # Dibuja una elipse más grande
            tortuga.circle(150, 90)  # Aumenta el radio largo de la elipse
            tortuga.circle(150//2, 90)  # Aumenta el radio corto de la elipse
        tortuga.end_fill()
        tortuga.penup()

        # Dibuja las piedras
        # Primera piedra
        tortuga.penup()
        tortuga.goto(-90, 10)  # Ajusta la posición para que coincida con el charco más grande
        tortuga.pendown()
        tortuga.color("gray")
        tortuga.begin_fill()
        tortuga.circle(20)  # Tamaño de la primera piedra
        tortuga.end_fill()
        tortuga.penup()

        # Segunda piedra
        tortuga.penup()
        tortuga.goto(-40, -20)  # Ajusta la posición para que coincida con el charco más grande
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(15)  # Tamaño de la segunda piedra
        tortuga.end_fill()
        tortuga.penup()

        # Tercera piedra
        tortuga.penup()
        tortuga.goto(10, -5)  # Ajusta la posición para que coincida con el charco más grande
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(15)  # Tamaño de la tercera piedra
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del perro café
        tortuga.goto(-200, -100)
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del perro
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del perro café
        tortuga.goto(-240, -50)
        tortuga.dot(10, "black")
        tortuga.goto(-210, -50)
        tortuga.dot(10, "black")
        tortuga.goto(-225, -70)
        tortuga.dot(5, "black")

        # Orejas del perro café
        tortuga.goto(-245, -40)
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(-200, -40)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del perro amarillo
        tortuga.goto(-300, 0)
        tortuga.pendown()
        tortuga.color("yellow")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del perro
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del perro amarillo
        tortuga.goto(-340, 45)
        tortuga.dot(10, "black")
        tortuga.goto(-310, 45)
        tortuga.dot(10, "black")
        tortuga.goto(-325, 30)
        tortuga.dot(5, "black")

        # Orejas del perro amarillo
        tortuga.goto(-355, 50)
        tortuga.pendown()
        tortuga.color("yellow")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(-285, 50)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del gato rojo
        tortuga.goto(-150, 0)
        tortuga.pendown()
        tortuga.color("blue")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del gato
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del gato rojo
        tortuga.goto(-190, 45)
        tortuga.dot(10, "black")
        tortuga.goto(-160, 45)
        tortuga.dot(10, "black")
        tortuga.goto(-175, 30)
        tortuga.dot(5, "black")

        # Orejas del gato rojo
        tortuga.goto(-205, 50)
        tortuga.pendown()
        tortuga.color("blue")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(-135, 50)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo de las nubes
        for x, y in [(0, 205), (200, 185), (-200,190)]:
            tortuga.goto(x, y)
            tortuga.color("white")
            tortuga.pendown()
            tortuga.begin_fill()
            tortuga.circle(30)
            tortuga.end_fill()
            tortuga.penup()
            tortuga.goto(x + 45, y)
            tortuga.pendown()
            tortuga.begin_fill()
            tortuga.circle(30)
            tortuga.end_fill()
            tortuga.penup()

        # Dibujo del sol amarillo
        tortuga.goto(-350, 160)
        tortuga.color("yellow")
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(50)
        tortuga.end_fill()
    
        tortuga.penup()

    def escena4(tortuga, width, height, color):

        # Dibujar el marco 1
        tortuga.penup()
        tortuga.setpos(-450, 335)  
        tortuga.pendown()
        tortuga.color("black")
        for _ in range(2):
            tortuga.forward(900)  
            tortuga.right(90)
            tortuga.forward(500)  
            tortuga.right(90)

        # Dibujar el marco 2
        tortuga.penup()
        tortuga.setpos(-450, 280)  
        tortuga.pendown()
        tortuga.color("black")
        for _ in range(2):
            tortuga.forward(900)  
            tortuga.right(90)
            tortuga.forward(600)  
            tortuga.right(90)
            ventana = turtle.Screen()
            ventana.bgcolor("gray")
            tortuga.speed(40)
        tortuga.penup()

        # Dibujo de la primera casa
        # Cuerpo de la casa
        tortuga.goto(-350, -100)
        tortuga.pendown()
        tortuga.fillcolor("pink")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(100)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        # Techo de la casa
        tortuga.goto(-350, 0)
        tortuga.pendown()
        tortuga.fillcolor("purple")
        tortuga.begin_fill()
        for _ in range(3):
            tortuga.forward(100)
            tortuga.left(120)
        tortuga.end_fill()
        tortuga.penup()

        # Ventanas
        tortuga.goto(-340, -40)  # Ajuste de coordenada x de la ventana izquierda
        tortuga.pendown()
        tortuga.fillcolor("sky blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(30)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        tortuga.goto(-290, -40)  # Ajuste de coordenada x de la ventana derecha
        tortuga.pendown()
        tortuga.fillcolor("sky blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(30)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        # Puerta
        tortuga.goto(-310, -60)  # Ajuste de coordenada x de la puerta
        tortuga.pendown()
        tortuga.fillcolor("brown")
        tortuga.begin_fill()
        for _ in range(2):
            tortuga.forward(20)
            tortuga.right(90)
            tortuga.forward(40)
            tortuga.right(90)
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo de las nubes
        for x, y in [(0, 205), (200, 185), (-200, 190)]:
            for offset in [0, 45]:  # Dibuja dos partes de cada nube
                tortuga.goto(x + offset, y)
                tortuga.color("white")
                tortuga.pendown()
                tortuga.begin_fill()
                tortuga.circle(30)
                tortuga.end_fill()
                tortuga.penup()

        # Agregar lluvia
        tortuga.color("blue")
        for x, y in [(0, 205), (200, 185), (-200, 190)]:
            for offset in [0, 45]:  # Agrega lluvia debajo de cada parte de la nube
                for i in range(-10, 10, 5):  # Varias gotas de lluvia por nube
                    tortuga.goto(x + offset + i, y - 30)  # Posición inicial de la lluvia
                    tortuga.pendown()
                    tortuga.right(90)  # Asegura que la tortuga apunte hacia abajo
                    tortuga.forward(20)  # Longitud de la lluvia
                    tortuga.penup()
                    tortuga.left(90)  # Reestablece la orientación de la tortuga


        # Dibujo del perro café
        tortuga.goto(-200, -100)
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del perro
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del perro café
        tortuga.goto(-215, -50)
        tortuga.dot(10, "black")
        tortuga.goto(-185, -50)
        tortuga.dot(10, "black")
        tortuga.goto(-200, -70)
        tortuga.dot(10, "black")
        tortuga.goto(-200, -90)
        tortuga.dot(12, "black")

        # Orejas del perro café
        tortuga.goto(-225, -30)
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(-175, -30)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del perro amarillo
        tortuga.goto(0, -100)
        tortuga.pendown()
        tortuga.color("yellow")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del perro
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del perro amarillo
        tortuga.goto(-15, -50)
        tortuga.dot(10, "black")
        tortuga.goto(15, -50)
        tortuga.dot(10, "black")
        tortuga.goto(0, -70)
        tortuga.dot(5, "black")

        # Orejas del perro amarillo
        tortuga.goto(-25, -30)
        tortuga.pendown()
        tortuga.color("yellow")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(25, -30)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del gato rojo
        tortuga.goto(200, -100)
        tortuga.pendown()
        tortuga.color("blue")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del gato
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del gato rojo
        tortuga.goto(185, -50)
        tortuga.dot(10, "black")
        tortuga.goto(215, -50)
        tortuga.dot(10, "black")
        tortuga.goto(200, -70)
        tortuga.dot(5, "black")

        # Orejas del gato rojo
        tortuga.goto(225, -30)
        tortuga.pendown()
        tortuga.color("blue")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(175, -30)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        tortuga.penup()

    def escena5(tortuga, width, height, color):

        # Dibujar el marco 1
        tortuga.penup()
        tortuga.setpos(-450, 335)  
        tortuga.pendown()
        tortuga.color("black")
        for _ in range(2):
            tortuga.forward(900)  
            tortuga.right(90)
            tortuga.forward(500)
            tortuga.right(90)

        # Dibujar el marco 2
        tortuga.penup()
        tortuga.setpos(-450, 280)  
        tortuga.pendown()
        tortuga.color("black")
        for _ in range(2):
            tortuga.forward(900)  
            tortuga.right(90)
            tortuga.forward(600)  
            tortuga.right(90)

            
            ventana = turtle.Screen()
            ventana.bgcolor("sky blue")
            tortuga.speed(40)
        tortuga.penup()

        # Dibujo del perro café
        tortuga.goto(-200, -100)
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del perro
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del perro café
        tortuga.goto(-205, -40)
        tortuga.dot(10, "black")
        tortuga.goto(-185, -40)
        tortuga.dot(10, "black")
        tortuga.goto(-190, -55)
        tortuga.dot(5, "black")
        tortuga.goto(-190, -70)
        tortuga.dot(10, "black")

        # Orejas del perro café
        tortuga.goto(-235, -40)
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(-170, -40)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del perro amarillo
        tortuga.goto(-300, 0)
        tortuga.pendown()
        tortuga.color("yellow")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del perro
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del perro amarillo
        tortuga.goto(-305, 60)
        tortuga.dot(10, "black")
        tortuga.goto(-290, 60)
        tortuga.dot(10, "black")
        tortuga.goto(-295, 50)
        tortuga.dot(5, "black")
        tortuga.goto(-295, 35)
        tortuga.dot(10, "black")

        # Orejas del perro amarillo
        tortuga.goto(-335, 65)
        tortuga.pendown()
        tortuga.color("yellow")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(-275, 65)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del gato rojo
        tortuga.goto(-142, 0)
        tortuga.pendown()
        tortuga.color("blue")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del gato
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del gato rojo
        tortuga.goto(-145, 60)
        tortuga.dot(10, "black")
        tortuga.goto(-125, 60)
        tortuga.dot(10, "black")
        tortuga.goto(-130, 50)
        tortuga.dot(5, "black")
        tortuga.goto(-130, 35)
        tortuga.dot(10, "black")

        # Orejas del gato rojo
        tortuga.goto(-175, 65)
        tortuga.pendown()
        tortuga.color("blue")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(-120, 65)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibuja dos pizzas pequeñas
        tortuga.penup()
        tortuga.goto(-50, -50)  # Posición de la primera pizza
        tortuga.pendown()
        tortuga.color("sandy brown")
        tortuga.begin_fill()
        tortuga.circle(40)  # Radio para una pizza pequeña
        tortuga.end_fill()

        # Toppings para la primera pizza
        tortuga.penup()
        tortuga.goto(-60, 10)
        tortuga.color("red")
        for _ in range(2):  # Simula algunos pepperonis
            tortuga.dot(10)
            tortuga.forward(20)
        tortuga.penup()
        tortuga.goto(-60, 0)
        tortuga.color("red")
        for _ in range(2):  # Simula algunos pepperonis
            tortuga.dot(10)
            tortuga.forward(20)
        tortuga.penup()
        tortuga.goto(-60, -10)
        tortuga.color("red")
        for _ in range(2):  # Simula algunos pepperonis
            tortuga.dot(10)
            tortuga.forward(20)
        tortuga.penup()
        tortuga.goto(-60, -20)
        tortuga.color("red")
        for _ in range(2):  # Simula algunos pepperonis
            tortuga.dot(10)
            tortuga.forward(20)
        tortuga.penup()
        tortuga.goto(-60, -30)
        tortuga.color("red")
        for _ in range(2):  # Simula algunos pepperonis
            tortuga.dot(10)
            tortuga.forward(20)
        # Segunda pizza
        tortuga.penup()
        tortuga.goto(40, -50)  # Posición de la segunda pizza
        tortuga.pendown()
        tortuga.color("sandy brown")
        tortuga.begin_fill()
        tortuga.circle(40)  # Radio para la segunda pizza pequeña
        tortuga.end_fill()

        # Toppings para la segunda pizza
        tortuga.penup()
        tortuga.goto(30, 10)
        tortuga.color("red")
        for _ in range(2):  # Simula algunos pepperonis
            tortuga.dot(10)
            tortuga.forward(20)
        tortuga.penup()
        tortuga.goto(30, 0)
        tortuga.color("red")
        for _ in range(2):  # Simula algunos pepperonis
            tortuga.dot(10)
            tortuga.forward(20)
        tortuga.penup()
        tortuga.goto(30, -10)
        tortuga.color("red")
        for _ in range(2):  # Simula algunos pepperonis
            tortuga.dot(10)
            tortuga.forward(20)
        tortuga.penup()
        tortuga.goto(30, -20)
        tortuga.color("red")
        for _ in range(2):  # Simula algunos pepperonis
            tortuga.dot(10)
            tortuga.forward(20)
        tortuga.penup()
        tortuga.goto(30, -30)
        tortuga.color("red")
        for _ in range(2):  # Simula algunos pepperonis
            tortuga.dot(10)
            tortuga.forward(20)

       # Dibuja el edificio principal
        tortuga.penup()
        tortuga.goto(100, -100)  # Nueva posición ajustada para la base del edificio
        tortuga.pendown()
        tortuga.color("yellow")  # Color del edificio
        tortuga.begin_fill()
        for _ in range(2):  # Crea un rectángulo
            tortuga.forward(300)
            tortuga.left(90)
            tortuga.forward(200)
            tortuga.left(90)
        tortuga.end_fill()

        # Dibuja el techo
        tortuga.penup()
        tortuga.goto(100, 100)
        tortuga.pendown()
        tortuga.color("red")  # Color del techo
        tortuga.begin_fill()
        tortuga.goto(250, 150)  # Punto medio del techo
        tortuga.goto(400, 100)  # Completa el triángulo del techo
        tortuga.goto(100, 100)
        tortuga.end_fill()

        # Dibuja una puerta
        tortuga.penup()
        tortuga.goto(220, -100)  # Posición de la puerta ajustada
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        for _ in range(2):
            tortuga.forward(50)
            tortuga.left(90)
            tortuga.forward(80)
            tortuga.left(90)
        tortuga.end_fill()

        # Dibuja ventanas
        tortuga.penup()
        tortuga.goto(125, -20)  # Ventana izquierda ajustada
        tortuga.pendown()
        tortuga.color("blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(40)
            tortuga.left(90)
        tortuga.end_fill()

        tortuga.penup()
        tortuga.goto(325, -20)  # Ventana derecha ajustada
        tortuga.pendown()
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(40)
            tortuga.left(90)
        tortuga.end_fill()

        # Dibuja el letrero de la pizzería
        tortuga.penup()
        tortuga.goto(210, 100)  # Posición del letrero ajustada
        tortuga.pendown()
        tortuga.color("white")
        tortuga.write("Pizzería", font=("Arial", 18, "bold"))
        tortuga.penup()

        # Dibujo de las nubes
        for x, y in [(0, 205), (200, 185), (-200,190)]:
            tortuga.goto(x, y)
            tortuga.color("white")
            tortuga.pendown()
            tortuga.begin_fill()
            tortuga.circle(30)
            tortuga.end_fill()
            tortuga.penup()
            tortuga.goto(x + 45, y)
            tortuga.pendown()
            tortuga.begin_fill()
            tortuga.circle(30)
            tortuga.end_fill()
            tortuga.penup()

        # Dibujo del sol amarillo
        tortuga.goto(-350, 160)
        tortuga.color("yellow")
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(50)
        tortuga.end_fill()
        tortuga.penup()

if colorfavorito== "verde":
    def escena1(tortuga, width, height, color):
        # Dibujar el marco 1
        tortuga.penup()
        tortuga.setpos(-450, 335)  
        tortuga.pendown()
        tortuga.color("black")
        for _ in range(2):
            tortuga.forward(900)  
            tortuga.right(90)
            tortuga.forward(500)  
            tortuga.right(90)

        # Dibujar el marco 2
        tortuga.penup()
        tortuga.setpos(-450, 280)  # Start from the top-left corner
        tortuga.pendown()
        tortuga.color("black")
        for _ in range(2):
            tortuga.forward(900)  
            tortuga.right(90)
            tortuga.forward(600)  
            tortuga.right(90)


        ventana = turtle.Screen()
        ventana.bgcolor("sky blue")
        tortuga.speed(40)
        tortuga.penup()
         # Dibujo del perro café
        tortuga.goto(-200, -100)
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del perro
        tortuga.end_fill()
        tortuga.penup()
          # Ojos y nariz del perro café
        tortuga.goto(-215, -50)
        tortuga.dot(10, "black")
        tortuga.goto(-185, -50)
        tortuga.dot(10, "black")
        tortuga.goto(-200, -70)
        tortuga.dot(5, "black")

        # Orejas del perro café
        tortuga.goto(-225, -30)
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(-175, -30)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del perro amarillo
        tortuga.goto(0, -100)
        tortuga.pendown()
        tortuga.color("yellow")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del perro
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del perro amarillo
        tortuga.goto(-15, -50)
        tortuga.dot(10, "black")
        tortuga.goto(15, -50)
        tortuga.dot(10, "black")
        tortuga.goto(0, -70)
        tortuga.dot(5, "black")
          # Orejas del perro amarillo
        tortuga.goto(-25, -30)
        tortuga.pendown()
        tortuga.color("yellow")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(25, -30)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del gato rojo
        tortuga.goto(200, -100)
        tortuga.pendown()
        tortuga.color("green")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del gato
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del gato rojo
        tortuga.goto(185, -50)
        tortuga.dot(10, "black")
        tortuga.goto(215, -50)
        tortuga.dot(10, "black")
        tortuga.goto(200, -70)
        tortuga.dot(5, "black")

        # Orejas del gato rojo
        tortuga.goto(225, -30)
        tortuga.pendown()
        tortuga.color("green")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(175, -30)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del primer árbol
        tortuga.goto(-300, 0)
        tortuga.color("brown")
        tortuga.pendown()
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(20)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(-290, 20)  # Posición ajustada para el follaje
        tortuga.pendown()
        tortuga.color("green")
        tortuga.begin_fill()
        tortuga.circle(40)
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del segundo árbol
        tortuga.goto(250, 0)
        tortuga.color("brown")
        tortuga.pendown()
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(20)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(260, 20)  # Posición ajustada para el follaje
        tortuga.pendown()
        tortuga.color("green")
        tortuga.begin_fill()
        tortuga.circle(40)
        tortuga.end_fill()
        tortuga.penup()
        # Dibujo de unos arbustos
        for x in [-150, -120, -90, -60, 150, 180, 210, 240]:
            tortuga.goto(x, -130)
            tortuga.color("dark green")
            tortuga.pendown()
            tortuga.begin_fill()
            tortuga.circle(20)
            tortuga.end_fill()
            tortuga.penup()

        # Dibujo del sol amarillo
        tortuga.goto(-350, 160)
        tortuga.color("yellow")
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(50)
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo de las nubes
        for x, y in [(0, 205), (200, 185), (-200,190)]:
            tortuga.goto(x, y)
            tortuga.color("white")
            tortuga.pendown()
            tortuga.begin_fill()
            tortuga.circle(30)
            tortuga.end_fill()
            tortuga.penup()
            tortuga.goto(x + 45, y)
            tortuga.pendown()
            tortuga.begin_fill()
            tortuga.circle(30)
            tortuga.end_fill()
            tortuga.penup()
            
             # Finalizar y mostrar ventana
        tortuga.hideturtle()
        tortuga.stamp()
        tortuga.penup()

    def escena2(tortuga, width, height, color):

        # Dibujar el marco 1
        tortuga.penup()
        tortuga.setpos(-450, 335)  
        tortuga.pendown()
        tortuga.color("black")
        for _ in range(2):
            tortuga.forward(900)  
            tortuga.right(90)
            tortuga.forward(500)  
            tortuga.right(90)

        # Dibujar el marco 2
        tortuga.penup()
        tortuga.setpos(-450, 280)  
        tortuga.pendown()
        tortuga.color("black")
        for _ in range(2):
            tortuga.forward(900)  
            tortuga.right(90)
            tortuga.forward(600)  
            tortuga.right(90)


            ventana = turtle.Screen()
            ventana.bgcolor("sky blue")
            tortuga.speed(40)
        tortuga.penup()
            

        # Dibujo de la primera casa
        # Cuerpo de la casa
        tortuga.goto(-350, -100)
        tortuga.pendown()
        tortuga.fillcolor("orange")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(100)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        # Techo de la casa
        tortuga.goto(-350, 0)
        tortuga.pendown()
        tortuga.fillcolor("green")
        tortuga.begin_fill()
        for _ in range(3):
            tortuga.forward(100)
            tortuga.left(120)
        tortuga.end_fill()
        tortuga.penup()

        # Ventanas
        tortuga.goto(-340, -40)  # Ajuste de coordenada x de la ventana izquierda
        tortuga.pendown()
        tortuga.fillcolor("sky blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(30)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        tortuga.goto(-290, -40)  # Ajuste de coordenada x de la ventana derecha
        tortuga.pendown()
        tortuga.fillcolor("sky blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(30)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        # Puerta
        tortuga.goto(-310, -60)  # Ajuste de coordenada x de la puerta
        tortuga.pendown()
        tortuga.fillcolor("brown")
        tortuga.begin_fill()
        for _ in range(2):
            tortuga.forward(20)
            tortuga.right(90)
            tortuga.forward(40)
            tortuga.right(90)
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo de la cuarta casa
        # Cuerpo de la casa
        tortuga.goto(-175, 0)
        tortuga.pendown()
        tortuga.fillcolor("orange")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(100)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        # Techo de la casa
        tortuga.goto(-175, 100)
        tortuga.pendown()
        tortuga.fillcolor("green")
        tortuga.begin_fill()
        for _ in range(3):
            tortuga.forward(100)
            tortuga.left(120)
        tortuga.end_fill()
        tortuga.penup()

        # Ventanas
        tortuga.goto(-165, 60)  # Ajuste de coordenada x de la ventana izquierda
        tortuga.pendown()
        tortuga.fillcolor("sky blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(30)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        tortuga.goto(-115, 60)  # Ajuste de coordenada x de la ventana derecha
        tortuga.pendown()
        tortuga.fillcolor("sky blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(30)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        # Puerta
        tortuga.goto(-135, 40)  # Ajuste de coordenada x de la puerta
        tortuga.pendown()
        tortuga.fillcolor("brown")
        tortuga.begin_fill()
        for _ in range(2):
            tortuga.forward(20)
            tortuga.right(90)
            tortuga.forward(40)
            tortuga.right(90)
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo de la segunda casa
        # Cuerpo de la casa
        tortuga.goto(300, -100)
        tortuga.pendown()
        tortuga.fillcolor("orange")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(100)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        # Techo de la casa
        tortuga.goto(300, 0)
        tortuga.pendown()
        tortuga.fillcolor("green")
        tortuga.begin_fill()
        for _ in range(3):
            tortuga.forward(100)
            tortuga.left(120)
        tortuga.end_fill()
        tortuga.penup()

        # Ventanas
        tortuga.goto(310, -40)  # Ajuste de coordenada x de la ventana izquierda
        tortuga.pendown()
        tortuga.fillcolor("sky blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(30)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        tortuga.goto(360, -40)  # Ajuste de coordenada x de la ventana derecha
        tortuga.pendown()
        tortuga.fillcolor("sky blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(30)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        # Puerta
        tortuga.goto(340, -60)  # Ajuste de coordenada x de la puerta
        tortuga.pendown()
        tortuga.fillcolor("brown")
        tortuga.begin_fill()
        for _ in range(2):
            tortuga.forward(20)
            tortuga.right(90)
            tortuga.forward(40)
            tortuga.right(90)
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo de la tercera casa
        # Cuerpo de la casa
        tortuga.goto(150, 0)
        tortuga.pendown()
        tortuga.fillcolor("orange")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(100)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        # Techo de la casa
        tortuga.goto(150, 100)
        tortuga.pendown()
        tortuga.fillcolor("green")
        tortuga.begin_fill()
        for _ in range(3):
            tortuga.forward(100)
            tortuga.left(120)
        tortuga.end_fill()
        tortuga.penup()

        # Ventanas
        tortuga.goto(160, 60)  # Ajuste de coordenada x de la ventana izquierda
        tortuga.pendown()
        tortuga.fillcolor("sky blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(30)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        tortuga.goto(210, 60)  # Ajuste de coordenada x de la ventana derecha
        tortuga.pendown()
        tortuga.fillcolor("sky blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(30)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        # Puerta
        tortuga.goto(190, 40)  # Ajuste de coordenada x de la puerta
        tortuga.pendown()
        tortuga.fillcolor("brown")
        tortuga.begin_fill()
        for _ in range(2):
            tortuga.forward(20)
            tortuga.right(90)
            tortuga.forward(40)
            tortuga.right(90)
        tortuga.end_fill()
        tortuga.penup()

         # Dibujo del perro café
        tortuga.goto(-200, -100)
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del perro
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del perro café
        tortuga.goto(-215, -50)
        tortuga.dot(10, "black")
        tortuga.goto(-185, -50)
        tortuga.dot(10, "black")
        tortuga.goto(-200, -70)
        tortuga.dot(5, "black")

        # Orejas del perro café
        tortuga.goto(-225, -30)
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(-175, -30)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del perro amarillo
        tortuga.goto(0, -100)
        tortuga.pendown()
        tortuga.color("yellow")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del perro
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del perro amarillo
        tortuga.goto(-15, -50)
        tortuga.dot(10, "black")
        tortuga.goto(15, -50)
        tortuga.dot(10, "black")
        tortuga.goto(0, -70)
        tortuga.dot(5, "black")

        # Orejas del perro amarillo
        tortuga.goto(-25, -30)
        tortuga.pendown()
        tortuga.color("yellow")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(25, -30)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del gato rojo
        tortuga.goto(200, -100)
        tortuga.pendown()
        tortuga.color("green")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del gato
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del gato rojo
        tortuga.goto(185, -50)
        tortuga.dot(10, "black")
        tortuga.goto(215, -50)
        tortuga.dot(10, "black")
        tortuga.goto(200, -70)
        tortuga.dot(5, "black")

        # Orejas del gato rojo
        tortuga.goto(225, -30)
        tortuga.pendown()
        tortuga.color("green")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(175, -30)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo de las nubes
        for x, y in [(0, 205), (200, 185), (-200,190)]:
            tortuga.goto(x, y)
            tortuga.color("white")
            tortuga.pendown()
            tortuga.begin_fill()
            tortuga.circle(30)
            tortuga.end_fill()
            tortuga.penup()
            tortuga.goto(x + 45, y)
            tortuga.pendown()
            tortuga.begin_fill()
            tortuga.circle(30)
            tortuga.end_fill()
            tortuga.penup()

        # Dibujo del sol amarillo
        tortuga.goto(-350, 160)
        tortuga.color("yellow")
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(50)
        tortuga.end_fill()
        tortuga.penup()
        

        # Finalizar y mostrar ventana
        tortuga.hideturtle()
        tortuga.stamp()
        tortuga.penup()
    
    def escena3(tortuga, width, height, color):

        # Dibujar el marco 1
        tortuga.penup()
        tortuga.setpos(-450, 335)  
        tortuga.pendown()
        tortuga.color("black")
        for _ in range(2):
            tortuga.forward(900)  
            tortuga.right(90)
            tortuga.forward(500)  
            tortuga.right(90)

        # Dibujar el marco 2
        tortuga.penup()
        tortuga.setpos(-450, 280)  
        tortuga.pendown()
        tortuga.color("black")
        for _ in range(2):
            tortuga.forward(900)  
            tortuga.right(90)
            tortuga.forward(600)  
            tortuga.right(90)

            ventana = turtle.Screen()
            ventana.bgcolor("skyblue")  # Fondo celeste para mejor contraste
            tortuga.speed(30)
        tortuga.penup()

        # Dibuja un charco en forma ovalada más grande
        tortuga.penup()
        tortuga.goto(0, -100)  # Ajusta la posición inicial del charco hacia abajo para más espacio
        tortuga.pendown()
        tortuga.color("blue")
        tortuga.begin_fill()
        tortuga.left(45)  # Inclina la elipse para el charco
        for _ in range(2):  # Dibuja una elipse más grande
            tortuga.circle(150, 90)  # Aumenta el radio largo de la elipse
            tortuga.circle(150//2, 90)  # Aumenta el radio corto de la elipse
        tortuga.end_fill()
        tortuga.penup()

        # Dibuja las piedras
        # Primera piedra
        tortuga.penup()
        tortuga.goto(-90, 10)  # Ajusta la posición para que coincida con el charco más grande
        tortuga.pendown()
        tortuga.color("gray")
        tortuga.begin_fill()
        tortuga.circle(20)  # Tamaño de la primera piedra
        tortuga.end_fill()
        tortuga.penup()

        # Segunda piedra
        tortuga.penup()
        tortuga.goto(-40, -20)  # Ajusta la posición para que coincida con el charco más grande
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(15)  # Tamaño de la segunda piedra
        tortuga.end_fill()
        tortuga.penup()

        # Tercera piedra
        tortuga.penup()
        tortuga.goto(10, -5)  # Ajusta la posición para que coincida con el charco más grande
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(15)  # Tamaño de la tercera piedra
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del perro café
        tortuga.goto(-200, -100)
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del perro
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del perro café
        tortuga.goto(-240, -50)
        tortuga.dot(10, "black")
        tortuga.goto(-210, -50)
        tortuga.dot(10, "black")
        tortuga.goto(-225, -70)
        tortuga.dot(5, "black")

        # Orejas del perro café
        tortuga.goto(-245, -40)
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(-200, -40)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del perro amarillo
        tortuga.goto(-300, 0)
        tortuga.pendown()
        tortuga.color("yellow")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del perro
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del perro amarillo
        tortuga.goto(-340, 45)
        tortuga.dot(10, "black")
        tortuga.goto(-310, 45)
        tortuga.dot(10, "black")
        tortuga.goto(-325, 30)
        tortuga.dot(5, "black")

        # Orejas del perro amarillo
        tortuga.goto(-355, 50)
        tortuga.pendown()
        tortuga.color("yellow")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(-285, 50)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del gato rojo
        tortuga.goto(-150, 0)
        tortuga.pendown()
        tortuga.color("green")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del gato
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del gato rojo
        tortuga.goto(-190, 45)
        tortuga.dot(10, "black")
        tortuga.goto(-160, 45)
        tortuga.dot(10, "black")
        tortuga.goto(-175, 30)
        tortuga.dot(5, "black")

        # Orejas del gato rojo
        tortuga.goto(-205, 50)
        tortuga.pendown()
        tortuga.color("green")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(-135, 50)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo de las nubes
        for x, y in [(0, 205), (200, 185), (-200,190)]:
            tortuga.goto(x, y)
            tortuga.color("white")
            tortuga.pendown()
            tortuga.begin_fill()
            tortuga.circle(30)
            tortuga.end_fill()
            tortuga.penup()
            tortuga.goto(x + 45, y)
            tortuga.pendown()
            tortuga.begin_fill()
            tortuga.circle(30)
            tortuga.end_fill()
            tortuga.penup()

        # Dibujo del sol amarillo
        tortuga.goto(-350, 160)
        tortuga.color("yellow")
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(50)
        tortuga.end_fill()
    
        tortuga.penup()

    def escena4(tortuga, width, height, color):

        # Dibujar el marco 1
        tortuga.penup()
        tortuga.setpos(-450, 335)  
        tortuga.pendown()
        tortuga.color("black")
        for _ in range(2):
            tortuga.forward(900)  
            tortuga.right(90)
            tortuga.forward(500)  
            tortuga.right(90)

        # Dibujar el marco 2
        tortuga.penup()
        tortuga.setpos(-450, 280)  
        tortuga.pendown()
        tortuga.color("black")
        for _ in range(2):
            tortuga.forward(900)  
            tortuga.right(90)
            tortuga.forward(600)  
            tortuga.right(90)
            ventana = turtle.Screen()
            ventana.bgcolor("gray")
            tortuga.speed(40)
        tortuga.penup()

        # Dibujo de la primera casa
        # Cuerpo de la casa
        tortuga.goto(-350, -100)
        tortuga.pendown()
        tortuga.fillcolor("pink")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(100)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        # Techo de la casa
        tortuga.goto(-350, 0)
        tortuga.pendown()
        tortuga.fillcolor("purple")
        tortuga.begin_fill()
        for _ in range(3):
            tortuga.forward(100)
            tortuga.left(120)
        tortuga.end_fill()
        tortuga.penup()

        # Ventanas
        tortuga.goto(-340, -40)  # Ajuste de coordenada x de la ventana izquierda
        tortuga.pendown()
        tortuga.fillcolor("sky blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(30)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        tortuga.goto(-290, -40)  # Ajuste de coordenada x de la ventana derecha
        tortuga.pendown()
        tortuga.fillcolor("sky blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(30)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        # Puerta
        tortuga.goto(-310, -60)  # Ajuste de coordenada x de la puerta
        tortuga.pendown()
        tortuga.fillcolor("brown")
        tortuga.begin_fill()
        for _ in range(2):
            tortuga.forward(20)
            tortuga.right(90)
            tortuga.forward(40)
            tortuga.right(90)
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo de las nubes
        for x, y in [(0, 205), (200, 185), (-200, 190)]:
            for offset in [0, 45]:  # Dibuja dos partes de cada nube
                tortuga.goto(x + offset, y)
                tortuga.color("white")
                tortuga.pendown()
                tortuga.begin_fill()
                tortuga.circle(30)
                tortuga.end_fill()
                tortuga.penup()

        # Agregar lluvia
        tortuga.color("blue")
        for x, y in [(0, 205), (200, 185), (-200, 190)]:
            for offset in [0, 45]:  # Agrega lluvia debajo de cada parte de la nube
                for i in range(-10, 10, 5):  # Varias gotas de lluvia por nube
                    tortuga.goto(x + offset + i, y - 30)  # Posición inicial de la lluvia
                    tortuga.pendown()
                    tortuga.right(90)  # Asegura que la tortuga apunte hacia abajo
                    tortuga.forward(20)  # Longitud de la lluvia
                    tortuga.penup()
                    tortuga.left(90)  # Reestablece la orientación de la tortuga


        # Dibujo del perro café
        tortuga.goto(-200, -100)
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del perro
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del perro café
        tortuga.goto(-215, -50)
        tortuga.dot(10, "black")
        tortuga.goto(-185, -50)
        tortuga.dot(10, "black")
        tortuga.goto(-200, -70)
        tortuga.dot(10, "black")
        tortuga.goto(-200, -90)
        tortuga.dot(12, "black")

        # Orejas del perro café
        tortuga.goto(-225, -30)
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(-175, -30)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del perro amarillo
        tortuga.goto(0, -100)
        tortuga.pendown()
        tortuga.color("yellow")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del perro
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del perro amarillo
        tortuga.goto(-15, -50)
        tortuga.dot(10, "black")
        tortuga.goto(15, -50)
        tortuga.dot(10, "black")
        tortuga.goto(0, -70)
        tortuga.dot(5, "black")

        # Orejas del perro amarillo
        tortuga.goto(-25, -30)
        tortuga.pendown()
        tortuga.color("yellow")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(25, -30)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del gato rojo
        tortuga.goto(200, -100)
        tortuga.pendown()
        tortuga.color("green")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del gato
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del gato rojo
        tortuga.goto(185, -50)
        tortuga.dot(10, "black")
        tortuga.goto(215, -50)
        tortuga.dot(10, "black")
        tortuga.goto(200, -70)
        tortuga.dot(5, "black")

        # Orejas del gato rojo
        tortuga.goto(225, -30)
        tortuga.pendown()
        tortuga.color("green")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(175, -30)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        tortuga.penup()

    def escena5(tortuga, width, height, color):

        # Dibujar el marco 1
        tortuga.penup()
        tortuga.setpos(-450, 335)  
        tortuga.pendown()
        tortuga.color("black")
        for _ in range(2):
            tortuga.forward(900)  
            tortuga.right(90)
            tortuga.forward(500)
            tortuga.right(90)

        # Dibujar el marco 2
        tortuga.penup()
        tortuga.setpos(-450, 280)  
        tortuga.pendown()
        tortuga.color("black")
        for _ in range(2):
            tortuga.forward(900)  
            tortuga.right(90)
            tortuga.forward(600)  
            tortuga.right(90)

            
            ventana = turtle.Screen()
            ventana.bgcolor("sky blue")
            tortuga.speed(40)
        tortuga.penup()

        # Dibujo del perro café
        tortuga.goto(-200, -100)
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del perro
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del perro café
        tortuga.goto(-205, -40)
        tortuga.dot(10, "black")
        tortuga.goto(-185, -40)
        tortuga.dot(10, "black")
        tortuga.goto(-190, -55)
        tortuga.dot(5, "black")
        tortuga.goto(-190, -70)
        tortuga.dot(10, "black")

        # Orejas del perro café
        tortuga.goto(-235, -40)
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(-170, -40)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del perro amarillo
        tortuga.goto(-300, 0)
        tortuga.pendown()
        tortuga.color("yellow")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del perro
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del perro amarillo
        tortuga.goto(-305, 60)
        tortuga.dot(10, "black")
        tortuga.goto(-290, 60)
        tortuga.dot(10, "black")
        tortuga.goto(-295, 50)
        tortuga.dot(5, "black")
        tortuga.goto(-295, 35)
        tortuga.dot(10, "black")

        # Orejas del perro amarillo
        tortuga.goto(-335, 65)
        tortuga.pendown()
        tortuga.color("yellow")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(-275, 65)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del gato rojo
        tortuga.goto(-142, 0)
        tortuga.pendown()
        tortuga.color("green")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del gato
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del gato rojo
        tortuga.goto(-145, 60)
        tortuga.dot(10, "black")
        tortuga.goto(-125, 60)
        tortuga.dot(10, "black")
        tortuga.goto(-130, 50)
        tortuga.dot(5, "black")
        tortuga.goto(-130, 35)
        tortuga.dot(10, "black")

        # Orejas del gato rojo
        tortuga.goto(-175, 65)
        tortuga.pendown()
        tortuga.color("green")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(-120, 65)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibuja dos pizzas pequeñas
        tortuga.penup()
        tortuga.goto(-50, -50)  # Posición de la primera pizza
        tortuga.pendown()
        tortuga.color("sandy brown")
        tortuga.begin_fill()
        tortuga.circle(40)  # Radio para una pizza pequeña
        tortuga.end_fill()

        # Toppings para la primera pizza
        tortuga.penup()
        tortuga.goto(-60, 10)
        tortuga.color("red")
        for _ in range(2):  # Simula algunos pepperonis
            tortuga.dot(10)
            tortuga.forward(20)
        tortuga.penup()
        tortuga.goto(-60, 0)
        tortuga.color("red")
        for _ in range(2):  # Simula algunos pepperonis
            tortuga.dot(10)
            tortuga.forward(20)
        tortuga.penup()
        tortuga.goto(-60, -10)
        tortuga.color("red")
        for _ in range(2):  # Simula algunos pepperonis
            tortuga.dot(10)
            tortuga.forward(20)
        tortuga.penup()
        tortuga.goto(-60, -20)
        tortuga.color("red")
        for _ in range(2):  # Simula algunos pepperonis
            tortuga.dot(10)
            tortuga.forward(20)
        tortuga.penup()
        tortuga.goto(-60, -30)
        tortuga.color("red")
        for _ in range(2):  # Simula algunos pepperonis
            tortuga.dot(10)
            tortuga.forward(20)
        # Segunda pizza
        tortuga.penup()
        tortuga.goto(40, -50)  # Posición de la segunda pizza
        tortuga.pendown()
        tortuga.color("sandy brown")
        tortuga.begin_fill()
        tortuga.circle(40)  # Radio para la segunda pizza pequeña
        tortuga.end_fill()

        # Toppings para la segunda pizza
        tortuga.penup()
        tortuga.goto(30, 10)
        tortuga.color("red")
        for _ in range(2):  # Simula algunos pepperonis
            tortuga.dot(10)
            tortuga.forward(20)
        tortuga.penup()
        tortuga.goto(30, 0)
        tortuga.color("red")
        for _ in range(2):  # Simula algunos pepperonis
            tortuga.dot(10)
            tortuga.forward(20)
        tortuga.penup()
        tortuga.goto(30, -10)
        tortuga.color("red")
        for _ in range(2):  # Simula algunos pepperonis
            tortuga.dot(10)
            tortuga.forward(20)
        tortuga.penup()
        tortuga.goto(30, -20)
        tortuga.color("red")
        for _ in range(2):  # Simula algunos pepperonis
            tortuga.dot(10)
            tortuga.forward(20)
        tortuga.penup()
        tortuga.goto(30, -30)
        tortuga.color("red")
        for _ in range(2):  # Simula algunos pepperonis
            tortuga.dot(10)
            tortuga.forward(20)

       # Dibuja el edificio principal
        tortuga.penup()
        tortuga.goto(100, -100)  # Nueva posición ajustada para la base del edificio
        tortuga.pendown()
        tortuga.color("yellow")  # Color del edificio
        tortuga.begin_fill()
        for _ in range(2):  # Crea un rectángulo
            tortuga.forward(300)
            tortuga.left(90)
            tortuga.forward(200)
            tortuga.left(90)
        tortuga.end_fill()

        # Dibuja el techo
        tortuga.penup()
        tortuga.goto(100, 100)
        tortuga.pendown()
        tortuga.color("red")  # Color del techo
        tortuga.begin_fill()
        tortuga.goto(250, 150)  # Punto medio del techo
        tortuga.goto(400, 100)  # Completa el triángulo del techo
        tortuga.goto(100, 100)
        tortuga.end_fill()

        # Dibuja una puerta
        tortuga.penup()
        tortuga.goto(220, -100)  # Posición de la puerta ajustada
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        for _ in range(2):
            tortuga.forward(50)
            tortuga.left(90)
            tortuga.forward(80)
            tortuga.left(90)
        tortuga.end_fill()

        # Dibuja ventanas
        tortuga.penup()
        tortuga.goto(125, -20)  # Ventana izquierda ajustada
        tortuga.pendown()
        tortuga.color("blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(40)
            tortuga.left(90)
        tortuga.end_fill()

        tortuga.penup()
        tortuga.goto(325, -20)  # Ventana derecha ajustada
        tortuga.pendown()
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(40)
            tortuga.left(90)
        tortuga.end_fill()

        # Dibuja el letrero de la pizzería
        tortuga.penup()
        tortuga.goto(210, 100)  # Posición del letrero ajustada
        tortuga.pendown()
        tortuga.color("white")
        tortuga.write("Pizzería", font=("Arial", 18, "bold"))
        tortuga.penup()

        # Dibujo de las nubes
        for x, y in [(0, 205), (200, 185), (-200,190)]:
            tortuga.goto(x, y)
            tortuga.color("white")
            tortuga.pendown()
            tortuga.begin_fill()
            tortuga.circle(30)
            tortuga.end_fill()
            tortuga.penup()
            tortuga.goto(x + 45, y)
            tortuga.pendown()
            tortuga.begin_fill()
            tortuga.circle(30)
            tortuga.end_fill()
            tortuga.penup()

        # Dibujo del sol amarillo
        tortuga.goto(-350, 160)
        tortuga.color("yellow")
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(50)
        tortuga.end_fill()
        tortuga.penup()
if colorfavorito == "morado":
    def escena1(tortuga, width, height, color):
        # Dibujar el marco 1
        tortuga.penup()
        tortuga.setpos(-450, 335)  
        tortuga.pendown()
        tortuga.color("black")
        for _ in range(2):
            tortuga.forward(900)  
            tortuga.right(90)
            tortuga.forward(500)  
            tortuga.right(90)

        # Dibujar el marco 2
        tortuga.penup()
        tortuga.setpos(-450, 280)  # Start from the top-left corner
        tortuga.pendown()
        tortuga.color("black")
        for _ in range(2):
            tortuga.forward(900)  
            tortuga.right(90)
            tortuga.forward(600)  
            tortuga.right(90)


        ventana = turtle.Screen()
        ventana.bgcolor("sky blue")
        tortuga.speed(40)
        tortuga.penup()
         # Dibujo del perro café
        tortuga.goto(-200, -100)
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del perro
        tortuga.end_fill()
        tortuga.penup()
          # Ojos y nariz del perro café
        tortuga.goto(-215, -50)
        tortuga.dot(10, "black")
        tortuga.goto(-185, -50)
        tortuga.dot(10, "black")
        tortuga.goto(-200, -70)
        tortuga.dot(5, "black")

        # Orejas del perro café
        tortuga.goto(-225, -30)
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(-175, -30)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del perro amarillo
        tortuga.goto(0, -100)
        tortuga.pendown()
        tortuga.color("yellow")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del perro
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del perro amarillo
        tortuga.goto(-15, -50)
        tortuga.dot(10, "black")
        tortuga.goto(15, -50)
        tortuga.dot(10, "black")
        tortuga.goto(0, -70)
        tortuga.dot(5, "black")
          # Orejas del perro amarillo
        tortuga.goto(-25, -30)
        tortuga.pendown()
        tortuga.color("yellow")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(25, -30)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del gato rojo
        tortuga.goto(200, -100)
        tortuga.pendown()
        tortuga.color("purple")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del gato
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del gato rojo
        tortuga.goto(185, -50)
        tortuga.dot(10, "black")
        tortuga.goto(215, -50)
        tortuga.dot(10, "black")
        tortuga.goto(200, -70)
        tortuga.dot(5, "black")

        # Orejas del gato rojo
        tortuga.goto(225, -30)
        tortuga.pendown()
        tortuga.color("purple")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(175, -30)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del primer árbol
        tortuga.goto(-300, 0)
        tortuga.color("brown")
        tortuga.pendown()
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(20)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(-290, 20)  # Posición ajustada para el follaje
        tortuga.pendown()
        tortuga.color("green")
        tortuga.begin_fill()
        tortuga.circle(40)
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del segundo árbol
        tortuga.goto(250, 0)
        tortuga.color("brown")
        tortuga.pendown()
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(20)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(260, 20)  # Posición ajustada para el follaje
        tortuga.pendown()
        tortuga.color("green")
        tortuga.begin_fill()
        tortuga.circle(40)
        tortuga.end_fill()
        tortuga.penup()
        # Dibujo de unos arbustos
        for x in [-150, -120, -90, -60, 150, 180, 210, 240]:
            tortuga.goto(x, -130)
            tortuga.color("dark green")
            tortuga.pendown()
            tortuga.begin_fill()
            tortuga.circle(20)
            tortuga.end_fill()
            tortuga.penup()

        # Dibujo del sol amarillo
        tortuga.goto(-350, 160)
        tortuga.color("yellow")
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(50)
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo de las nubes
        for x, y in [(0, 205), (200, 185), (-200,190)]:
            tortuga.goto(x, y)
            tortuga.color("white")
            tortuga.pendown()
            tortuga.begin_fill()
            tortuga.circle(30)
            tortuga.end_fill()
            tortuga.penup()
            tortuga.goto(x + 45, y)
            tortuga.pendown()
            tortuga.begin_fill()
            tortuga.circle(30)
            tortuga.end_fill()
            tortuga.penup()
            
             # Finalizar y mostrar ventana
        tortuga.hideturtle()
        tortuga.stamp()
        tortuga.penup()

    def escena2(tortuga, width, height, color):

        # Dibujar el marco 1
        tortuga.penup()
        tortuga.setpos(-450, 335)  
        tortuga.pendown()
        tortuga.color("black")
        for _ in range(2):
            tortuga.forward(900)  
            tortuga.right(90)
            tortuga.forward(500)  
            tortuga.right(90)

        # Dibujar el marco 2
        tortuga.penup()
        tortuga.setpos(-450, 280)  
        tortuga.pendown()
        tortuga.color("black")
        for _ in range(2):
            tortuga.forward(900)  
            tortuga.right(90)
            tortuga.forward(600)  
            tortuga.right(90)


            ventana = turtle.Screen()
            ventana.bgcolor("sky blue")
            tortuga.speed(40)
        tortuga.penup()
            

        # Dibujo de la primera casa
        # Cuerpo de la casa
        tortuga.goto(-350, -100)
        tortuga.pendown()
        tortuga.fillcolor("orange")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(100)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        # Techo de la casa
        tortuga.goto(-350, 0)
        tortuga.pendown()
        tortuga.fillcolor("green")
        tortuga.begin_fill()
        for _ in range(3):
            tortuga.forward(100)
            tortuga.left(120)
        tortuga.end_fill()
        tortuga.penup()

        # Ventanas
        tortuga.goto(-340, -40)  # Ajuste de coordenada x de la ventana izquierda
        tortuga.pendown()
        tortuga.fillcolor("sky blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(30)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        tortuga.goto(-290, -40)  # Ajuste de coordenada x de la ventana derecha
        tortuga.pendown()
        tortuga.fillcolor("sky blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(30)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        # Puerta
        tortuga.goto(-310, -60)  # Ajuste de coordenada x de la puerta
        tortuga.pendown()
        tortuga.fillcolor("brown")
        tortuga.begin_fill()
        for _ in range(2):
            tortuga.forward(20)
            tortuga.right(90)
            tortuga.forward(40)
            tortuga.right(90)
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo de la cuarta casa
        # Cuerpo de la casa
        tortuga.goto(-175, 0)
        tortuga.pendown()
        tortuga.fillcolor("orange")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(100)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        # Techo de la casa
        tortuga.goto(-175, 100)
        tortuga.pendown()
        tortuga.fillcolor("green")
        tortuga.begin_fill()
        for _ in range(3):
            tortuga.forward(100)
            tortuga.left(120)
        tortuga.end_fill()
        tortuga.penup()

        # Ventanas
        tortuga.goto(-165, 60)  # Ajuste de coordenada x de la ventana izquierda
        tortuga.pendown()
        tortuga.fillcolor("sky blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(30)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        tortuga.goto(-115, 60)  # Ajuste de coordenada x de la ventana derecha
        tortuga.pendown()
        tortuga.fillcolor("sky blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(30)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        # Puerta
        tortuga.goto(-135, 40)  # Ajuste de coordenada x de la puerta
        tortuga.pendown()
        tortuga.fillcolor("brown")
        tortuga.begin_fill()
        for _ in range(2):
            tortuga.forward(20)
            tortuga.right(90)
            tortuga.forward(40)
            tortuga.right(90)
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo de la segunda casa
        # Cuerpo de la casa
        tortuga.goto(300, -100)
        tortuga.pendown()
        tortuga.fillcolor("orange")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(100)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        # Techo de la casa
        tortuga.goto(300, 0)
        tortuga.pendown()
        tortuga.fillcolor("green")
        tortuga.begin_fill()
        for _ in range(3):
            tortuga.forward(100)
            tortuga.left(120)
        tortuga.end_fill()
        tortuga.penup()

        # Ventanas
        tortuga.goto(310, -40)  # Ajuste de coordenada x de la ventana izquierda
        tortuga.pendown()
        tortuga.fillcolor("sky blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(30)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        tortuga.goto(360, -40)  # Ajuste de coordenada x de la ventana derecha
        tortuga.pendown()
        tortuga.fillcolor("sky blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(30)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        # Puerta
        tortuga.goto(340, -60)  # Ajuste de coordenada x de la puerta
        tortuga.pendown()
        tortuga.fillcolor("brown")
        tortuga.begin_fill()
        for _ in range(2):
            tortuga.forward(20)
            tortuga.right(90)
            tortuga.forward(40)
            tortuga.right(90)
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo de la tercera casa
        # Cuerpo de la casa
        tortuga.goto(150, 0)
        tortuga.pendown()
        tortuga.fillcolor("orange")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(100)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        # Techo de la casa
        tortuga.goto(150, 100)
        tortuga.pendown()
        tortuga.fillcolor("green")
        tortuga.begin_fill()
        for _ in range(3):
            tortuga.forward(100)
            tortuga.left(120)
        tortuga.end_fill()
        tortuga.penup()

        # Ventanas
        tortuga.goto(160, 60)  # Ajuste de coordenada x de la ventana izquierda
        tortuga.pendown()
        tortuga.fillcolor("sky blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(30)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        tortuga.goto(210, 60)  # Ajuste de coordenada x de la ventana derecha
        tortuga.pendown()
        tortuga.fillcolor("sky blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(30)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        # Puerta
        tortuga.goto(190, 40)  # Ajuste de coordenada x de la puerta
        tortuga.pendown()
        tortuga.fillcolor("brown")
        tortuga.begin_fill()
        for _ in range(2):
            tortuga.forward(20)
            tortuga.right(90)
            tortuga.forward(40)
            tortuga.right(90)
        tortuga.end_fill()
        tortuga.penup()

         # Dibujo del perro café
        tortuga.goto(-200, -100)
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del perro
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del perro café
        tortuga.goto(-215, -50)
        tortuga.dot(10, "black")
        tortuga.goto(-185, -50)
        tortuga.dot(10, "black")
        tortuga.goto(-200, -70)
        tortuga.dot(5, "black")

        # Orejas del perro café
        tortuga.goto(-225, -30)
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(-175, -30)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del perro amarillo
        tortuga.goto(0, -100)
        tortuga.pendown()
        tortuga.color("yellow")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del perro
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del perro amarillo
        tortuga.goto(-15, -50)
        tortuga.dot(10, "black")
        tortuga.goto(15, -50)
        tortuga.dot(10, "black")
        tortuga.goto(0, -70)
        tortuga.dot(5, "black")

        # Orejas del perro amarillo
        tortuga.goto(-25, -30)
        tortuga.pendown()
        tortuga.color("yellow")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(25, -30)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del gato rojo
        tortuga.goto(200, -100)
        tortuga.pendown()
        tortuga.color("purple")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del gato
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del gato rojo
        tortuga.goto(185, -50)
        tortuga.dot(10, "black")
        tortuga.goto(215, -50)
        tortuga.dot(10, "black")
        tortuga.goto(200, -70)
        tortuga.dot(5, "black")

        # Orejas del gato rojo
        tortuga.goto(225, -30)
        tortuga.pendown()
        tortuga.color("purple")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(175, -30)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo de las nubes
        for x, y in [(0, 205), (200, 185), (-200,190)]:
            tortuga.goto(x, y)
            tortuga.color("white")
            tortuga.pendown()
            tortuga.begin_fill()
            tortuga.circle(30)
            tortuga.end_fill()
            tortuga.penup()
            tortuga.goto(x + 45, y)
            tortuga.pendown()
            tortuga.begin_fill()
            tortuga.circle(30)
            tortuga.end_fill()
            tortuga.penup()

        # Dibujo del sol amarillo
        tortuga.goto(-350, 160)
        tortuga.color("yellow")
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(50)
        tortuga.end_fill()
        tortuga.penup()
        

        # Finalizar y mostrar ventana
        tortuga.hideturtle()
        tortuga.stamp()
        tortuga.penup()
    
    def escena3(tortuga, width, height, color):

        # Dibujar el marco 1
        tortuga.penup()
        tortuga.setpos(-450, 335)  
        tortuga.pendown()
        tortuga.color("black")
        for _ in range(2):
            tortuga.forward(900)  
            tortuga.right(90)
            tortuga.forward(500)  
            tortuga.right(90)

        # Dibujar el marco 2
        tortuga.penup()
        tortuga.setpos(-450, 280)  
        tortuga.pendown()
        tortuga.color("black")
        for _ in range(2):
            tortuga.forward(900)  
            tortuga.right(90)
            tortuga.forward(600)  
            tortuga.right(90)

            ventana = turtle.Screen()
            ventana.bgcolor("skyblue")  # Fondo celeste para mejor contraste
            tortuga.speed(30)
        tortuga.penup()

        # Dibuja un charco en forma ovalada más grande
        tortuga.penup()
        tortuga.goto(0, -100)  # Ajusta la posición inicial del charco hacia abajo para más espacio
        tortuga.pendown()
        tortuga.color("blue")
        tortuga.begin_fill()
        tortuga.left(45)  # Inclina la elipse para el charco
        for _ in range(2):  # Dibuja una elipse más grande
            tortuga.circle(150, 90)  # Aumenta el radio largo de la elipse
            tortuga.circle(150//2, 90)  # Aumenta el radio corto de la elipse
        tortuga.end_fill()
        tortuga.penup()

        # Dibuja las piedras
        # Primera piedra
        tortuga.penup()
        tortuga.goto(-90, 10)  # Ajusta la posición para que coincida con el charco más grande
        tortuga.pendown()
        tortuga.color("gray")
        tortuga.begin_fill()
        tortuga.circle(20)  # Tamaño de la primera piedra
        tortuga.end_fill()
        tortuga.penup()

        # Segunda piedra
        tortuga.penup()
        tortuga.goto(-40, -20)  # Ajusta la posición para que coincida con el charco más grande
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(15)  # Tamaño de la segunda piedra
        tortuga.end_fill()
        tortuga.penup()

        # Tercera piedra
        tortuga.penup()
        tortuga.goto(10, -5)  # Ajusta la posición para que coincida con el charco más grande
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(15)  # Tamaño de la tercera piedra
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del perro café
        tortuga.goto(-200, -100)
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del perro
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del perro café
        tortuga.goto(-240, -50)
        tortuga.dot(10, "black")
        tortuga.goto(-210, -50)
        tortuga.dot(10, "black")
        tortuga.goto(-225, -70)
        tortuga.dot(5, "black")

        # Orejas del perro café
        tortuga.goto(-245, -40)
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(-200, -40)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del perro amarillo
        tortuga.goto(-300, 0)
        tortuga.pendown()
        tortuga.color("yellow")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del perro
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del perro amarillo
        tortuga.goto(-340, 45)
        tortuga.dot(10, "black")
        tortuga.goto(-310, 45)
        tortuga.dot(10, "black")
        tortuga.goto(-325, 30)
        tortuga.dot(5, "black")

        # Orejas del perro amarillo
        tortuga.goto(-355, 50)
        tortuga.pendown()
        tortuga.color("yellow")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(-285, 50)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del gato rojo
        tortuga.goto(-150, 0)
        tortuga.pendown()
        tortuga.color("purple")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del gato
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del gato rojo
        tortuga.goto(-190, 45)
        tortuga.dot(10, "black")
        tortuga.goto(-160, 45)
        tortuga.dot(10, "black")
        tortuga.goto(-175, 30)
        tortuga.dot(5, "black")

        # Orejas del gato rojo
        tortuga.goto(-205, 50)
        tortuga.pendown()
        tortuga.color("purple")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(-135, 50)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo de las nubes
        for x, y in [(0, 205), (200, 185), (-200,190)]:
            tortuga.goto(x, y)
            tortuga.color("white")
            tortuga.pendown()
            tortuga.begin_fill()
            tortuga.circle(30)
            tortuga.end_fill()
            tortuga.penup()
            tortuga.goto(x + 45, y)
            tortuga.pendown()
            tortuga.begin_fill()
            tortuga.circle(30)
            tortuga.end_fill()
            tortuga.penup()

        # Dibujo del sol amarillo
        tortuga.goto(-350, 160)
        tortuga.color("yellow")
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(50)
        tortuga.end_fill()
    
        tortuga.penup()

    def escena4(tortuga, width, height, color):

        # Dibujar el marco 1
        tortuga.penup()
        tortuga.setpos(-450, 335)  
        tortuga.pendown()
        tortuga.color("black")
        for _ in range(2):
            tortuga.forward(900)  
            tortuga.right(90)
            tortuga.forward(500)  
            tortuga.right(90)

        # Dibujar el marco 2
        tortuga.penup()
        tortuga.setpos(-450, 280)  
        tortuga.pendown()
        tortuga.color("black")
        for _ in range(2):
            tortuga.forward(900)  
            tortuga.right(90)
            tortuga.forward(600)  
            tortuga.right(90)
            ventana = turtle.Screen()
            ventana.bgcolor("gray")
            tortuga.speed(40)
        tortuga.penup()

        # Dibujo de la primera casa
        # Cuerpo de la casa
        tortuga.goto(-350, -100)
        tortuga.pendown()
        tortuga.fillcolor("pink")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(100)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        # Techo de la casa
        tortuga.goto(-350, 0)
        tortuga.pendown()
        tortuga.fillcolor("purple")
        tortuga.begin_fill()
        for _ in range(3):
            tortuga.forward(100)
            tortuga.left(120)
        tortuga.end_fill()
        tortuga.penup()

        # Ventanas
        tortuga.goto(-340, -40)  # Ajuste de coordenada x de la ventana izquierda
        tortuga.pendown()
        tortuga.fillcolor("sky blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(30)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        tortuga.goto(-290, -40)  # Ajuste de coordenada x de la ventana derecha
        tortuga.pendown()
        tortuga.fillcolor("sky blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(30)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        # Puerta
        tortuga.goto(-310, -60)  # Ajuste de coordenada x de la puerta
        tortuga.pendown()
        tortuga.fillcolor("brown")
        tortuga.begin_fill()
        for _ in range(2):
            tortuga.forward(20)
            tortuga.right(90)
            tortuga.forward(40)
            tortuga.right(90)
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo de las nubes
        for x, y in [(0, 205), (200, 185), (-200, 190)]:
            for offset in [0, 45]:  # Dibuja dos partes de cada nube
                tortuga.goto(x + offset, y)
                tortuga.color("white")
                tortuga.pendown()
                tortuga.begin_fill()
                tortuga.circle(30)
                tortuga.end_fill()
                tortuga.penup()

        # Agregar lluvia
        tortuga.color("blue")
        for x, y in [(0, 205), (200, 185), (-200, 190)]:
            for offset in [0, 45]:  # Agrega lluvia debajo de cada parte de la nube
                for i in range(-10, 10, 5):  # Varias gotas de lluvia por nube
                    tortuga.goto(x + offset + i, y - 30)  # Posición inicial de la lluvia
                    tortuga.pendown()
                    tortuga.right(90)  # Asegura que la tortuga apunte hacia abajo
                    tortuga.forward(20)  # Longitud de la lluvia
                    tortuga.penup()
                    tortuga.left(90)  # Reestablece la orientación de la tortuga


        # Dibujo del perro café
        tortuga.goto(-200, -100)
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del perro
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del perro café
        tortuga.goto(-215, -50)
        tortuga.dot(10, "black")
        tortuga.goto(-185, -50)
        tortuga.dot(10, "black")
        tortuga.goto(-200, -70)
        tortuga.dot(10, "black")
        tortuga.goto(-200, -90)
        tortuga.dot(12, "black")

        # Orejas del perro café
        tortuga.goto(-225, -30)
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(-175, -30)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del perro amarillo
        tortuga.goto(0, -100)
        tortuga.pendown()
        tortuga.color("yellow")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del perro
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del perro amarillo
        tortuga.goto(-15, -50)
        tortuga.dot(10, "black")
        tortuga.goto(15, -50)
        tortuga.dot(10, "black")
        tortuga.goto(0, -70)
        tortuga.dot(5, "black")

        # Orejas del perro amarillo
        tortuga.goto(-25, -30)
        tortuga.pendown()
        tortuga.color("yellow")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(25, -30)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del gato rojo
        tortuga.goto(200, -100)
        tortuga.pendown()
        tortuga.color("purple")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del gato
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del gato rojo
        tortuga.goto(185, -50)
        tortuga.dot(10, "black")
        tortuga.goto(215, -50)
        tortuga.dot(10, "black")
        tortuga.goto(200, -70)
        tortuga.dot(5, "black")

        # Orejas del gato rojo
        tortuga.goto(225, -30)
        tortuga.pendown()
        tortuga.color("purple")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(175, -30)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        tortuga.penup()

    def escena5(tortuga, width, height, color):

        # Dibujar el marco 1
        tortuga.penup()
        tortuga.setpos(-450, 335)  
        tortuga.pendown()
        tortuga.color("black")
        for _ in range(2):
            tortuga.forward(900)  
            tortuga.right(90)
            tortuga.forward(500)
            tortuga.right(90)

        # Dibujar el marco 2
        tortuga.penup()
        tortuga.setpos(-450, 280)  
        tortuga.pendown()
        tortuga.color("black")
        for _ in range(2):
            tortuga.forward(900)  
            tortuga.right(90)
            tortuga.forward(600)  
            tortuga.right(90)

            
            ventana = turtle.Screen()
            ventana.bgcolor("sky blue")
            tortuga.speed(40)
        tortuga.penup()

        # Dibujo del perro café
        tortuga.goto(-200, -100)
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del perro
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del perro café
        tortuga.goto(-205, -40)
        tortuga.dot(10, "black")
        tortuga.goto(-185, -40)
        tortuga.dot(10, "black")
        tortuga.goto(-190, -55)
        tortuga.dot(5, "black")
        tortuga.goto(-190, -70)
        tortuga.dot(10, "black")

        # Orejas del perro café
        tortuga.goto(-235, -40)
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(-170, -40)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del perro amarillo
        tortuga.goto(-300, 0)
        tortuga.pendown()
        tortuga.color("yellow")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del perro
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del perro amarillo
        tortuga.goto(-305, 60)
        tortuga.dot(10, "black")
        tortuga.goto(-290, 60)
        tortuga.dot(10, "black")
        tortuga.goto(-295, 50)
        tortuga.dot(5, "black")
        tortuga.goto(-295, 35)
        tortuga.dot(10, "black")

        # Orejas del perro amarillo
        tortuga.goto(-335, 65)
        tortuga.pendown()
        tortuga.color("yellow")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(-275, 65)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del gato rojo
        tortuga.goto(-142, 0)
        tortuga.pendown()
        tortuga.color("purple")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del gato
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del gato rojo
        tortuga.goto(-145, 60)
        tortuga.dot(10, "black")
        tortuga.goto(-125, 60)
        tortuga.dot(10, "black")
        tortuga.goto(-130, 50)
        tortuga.dot(5, "black")
        tortuga.goto(-130, 35)
        tortuga.dot(10, "black")

        # Orejas del gato rojo
        tortuga.goto(-175, 65)
        tortuga.pendown()
        tortuga.color("purple")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(-120, 65)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibuja dos pizzas pequeñas
        tortuga.penup()
        tortuga.goto(-50, -50)  # Posición de la primera pizza
        tortuga.pendown()
        tortuga.color("sandy brown")
        tortuga.begin_fill()
        tortuga.circle(40)  # Radio para una pizza pequeña
        tortuga.end_fill()

        # Toppings para la primera pizza
        tortuga.penup()
        tortuga.goto(-60, 10)
        tortuga.color("red")
        for _ in range(2):  # Simula algunos pepperonis
            tortuga.dot(10)
            tortuga.forward(20)
        tortuga.penup()
        tortuga.goto(-60, 0)
        tortuga.color("red")
        for _ in range(2):  # Simula algunos pepperonis
            tortuga.dot(10)
            tortuga.forward(20)
        tortuga.penup()
        tortuga.goto(-60, -10)
        tortuga.color("red")
        for _ in range(2):  # Simula algunos pepperonis
            tortuga.dot(10)
            tortuga.forward(20)
        tortuga.penup()
        tortuga.goto(-60, -20)
        tortuga.color("red")
        for _ in range(2):  # Simula algunos pepperonis
            tortuga.dot(10)
            tortuga.forward(20)
        tortuga.penup()
        tortuga.goto(-60, -30)
        tortuga.color("red")
        for _ in range(2):  # Simula algunos pepperonis
            tortuga.dot(10)
            tortuga.forward(20)
        # Segunda pizza
        tortuga.penup()
        tortuga.goto(40, -50)  # Posición de la segunda pizza
        tortuga.pendown()
        tortuga.color("sandy brown")
        tortuga.begin_fill()
        tortuga.circle(40)  # Radio para la segunda pizza pequeña
        tortuga.end_fill()

        # Toppings para la segunda pizza
        tortuga.penup()
        tortuga.goto(30, 10)
        tortuga.color("red")
        for _ in range(2):  # Simula algunos pepperonis
            tortuga.dot(10)
            tortuga.forward(20)
        tortuga.penup()
        tortuga.goto(30, 0)
        tortuga.color("red")
        for _ in range(2):  # Simula algunos pepperonis
            tortuga.dot(10)
            tortuga.forward(20)
        tortuga.penup()
        tortuga.goto(30, -10)
        tortuga.color("red")
        for _ in range(2):  # Simula algunos pepperonis
            tortuga.dot(10)
            tortuga.forward(20)
        tortuga.penup()
        tortuga.goto(30, -20)
        tortuga.color("red")
        for _ in range(2):  # Simula algunos pepperonis
            tortuga.dot(10)
            tortuga.forward(20)
        tortuga.penup()
        tortuga.goto(30, -30)
        tortuga.color("red")
        for _ in range(2):  # Simula algunos pepperonis
            tortuga.dot(10)
            tortuga.forward(20)

       # Dibuja el edificio principal
        tortuga.penup()
        tortuga.goto(100, -100)  # Nueva posición ajustada para la base del edificio
        tortuga.pendown()
        tortuga.color("yellow")  # Color del edificio
        tortuga.begin_fill()
        for _ in range(2):  # Crea un rectángulo
            tortuga.forward(300)
            tortuga.left(90)
            tortuga.forward(200)
            tortuga.left(90)
        tortuga.end_fill()

        # Dibuja el techo
        tortuga.penup()
        tortuga.goto(100, 100)
        tortuga.pendown()
        tortuga.color("red")  # Color del techo
        tortuga.begin_fill()
        tortuga.goto(250, 150)  # Punto medio del techo
        tortuga.goto(400, 100)  # Completa el triángulo del techo
        tortuga.goto(100, 100)
        tortuga.end_fill()

        # Dibuja una puerta
        tortuga.penup()
        tortuga.goto(220, -100)  # Posición de la puerta ajustada
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        for _ in range(2):
            tortuga.forward(50)
            tortuga.left(90)
            tortuga.forward(80)
            tortuga.left(90)
        tortuga.end_fill()

        # Dibuja ventanas
        tortuga.penup()
        tortuga.goto(125, -20)  # Ventana izquierda ajustada
        tortuga.pendown()
        tortuga.color("blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(40)
            tortuga.left(90)
        tortuga.end_fill()

        tortuga.penup()
        tortuga.goto(325, -20)  # Ventana derecha ajustada
        tortuga.pendown()
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(40)
            tortuga.left(90)
        tortuga.end_fill()

        # Dibuja el letrero de la pizzería
        tortuga.penup()
        tortuga.goto(210, 100)  # Posición del letrero ajustada
        tortuga.pendown()
        tortuga.color("white")
        tortuga.write("Pizzería", font=("Arial", 18, "bold"))
        tortuga.penup()

        # Dibujo de las nubes
        for x, y in [(0, 205), (200, 185), (-200,190)]:
            tortuga.goto(x, y)
            tortuga.color("white")
            tortuga.pendown()
            tortuga.begin_fill()
            tortuga.circle(30)
            tortuga.end_fill()
            tortuga.penup()
            tortuga.goto(x + 45, y)
            tortuga.pendown()
            tortuga.begin_fill()
            tortuga.circle(30)
            tortuga.end_fill()
            tortuga.penup()

        # Dibujo del sol amarillo
        tortuga.goto(-350, 160)
        tortuga.color("yellow")
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(50)
        tortuga.end_fill()
        tortuga.penup()
if colorfavorito == "naranja":
    def escena1(tortuga, width, height, color):
        # Dibujar el marco 1
        tortuga.penup()
        tortuga.setpos(-450, 335)  
        tortuga.pendown()
        tortuga.color("black")
        for _ in range(2):
            tortuga.forward(900)  
            tortuga.right(90)
            tortuga.forward(500)  
            tortuga.right(90)

        # Dibujar el marco 2
        tortuga.penup()
        tortuga.setpos(-450, 280)  # Start from the top-left corner
        tortuga.pendown()
        tortuga.color("black")
        for _ in range(2):
            tortuga.forward(900)  
            tortuga.right(90)
            tortuga.forward(600)  
            tortuga.right(90)


        ventana = turtle.Screen()
        ventana.bgcolor("sky blue")
        tortuga.speed(40)
        tortuga.penup()
         # Dibujo del perro café
        tortuga.goto(-200, -100)
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del perro
        tortuga.end_fill()
        tortuga.penup()
          # Ojos y nariz del perro café
        tortuga.goto(-215, -50)
        tortuga.dot(10, "black")
        tortuga.goto(-185, -50)
        tortuga.dot(10, "black")
        tortuga.goto(-200, -70)
        tortuga.dot(5, "black")

        # Orejas del perro café
        tortuga.goto(-225, -30)
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(-175, -30)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del perro amarillo
        tortuga.goto(0, -100)
        tortuga.pendown()
        tortuga.color("yellow")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del perro
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del perro amarillo
        tortuga.goto(-15, -50)
        tortuga.dot(10, "black")
        tortuga.goto(15, -50)
        tortuga.dot(10, "black")
        tortuga.goto(0, -70)
        tortuga.dot(5, "black")
          # Orejas del perro amarillo
        tortuga.goto(-25, -30)
        tortuga.pendown()
        tortuga.color("yellow")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(25, -30)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del gato rojo
        tortuga.goto(200, -100)
        tortuga.pendown()
        tortuga.color("orange")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del gato
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del gato rojo
        tortuga.goto(185, -50)
        tortuga.dot(10, "black")
        tortuga.goto(215, -50)
        tortuga.dot(10, "black")
        tortuga.goto(200, -70)
        tortuga.dot(5, "black")

        # Orejas del gato rojo
        tortuga.goto(225, -30)
        tortuga.pendown()
        tortuga.color("orange")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(175, -30)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del primer árbol
        tortuga.goto(-300, 0)
        tortuga.color("brown")
        tortuga.pendown()
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(20)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(-290, 20)  # Posición ajustada para el follaje
        tortuga.pendown()
        tortuga.color("green")
        tortuga.begin_fill()
        tortuga.circle(40)
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del segundo árbol
        tortuga.goto(250, 0)
        tortuga.color("brown")
        tortuga.pendown()
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(20)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(260, 20)  # Posición ajustada para el follaje
        tortuga.pendown()
        tortuga.color("green")
        tortuga.begin_fill()
        tortuga.circle(40)
        tortuga.end_fill()
        tortuga.penup()
        # Dibujo de unos arbustos
        for x in [-150, -120, -90, -60, 150, 180, 210, 240]:
            tortuga.goto(x, -130)
            tortuga.color("dark green")
            tortuga.pendown()
            tortuga.begin_fill()
            tortuga.circle(20)
            tortuga.end_fill()
            tortuga.penup()

        # Dibujo del sol amarillo
        tortuga.goto(-350, 160)
        tortuga.color("yellow")
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(50)
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo de las nubes
        for x, y in [(0, 205), (200, 185), (-200,190)]:
            tortuga.goto(x, y)
            tortuga.color("white")
            tortuga.pendown()
            tortuga.begin_fill()
            tortuga.circle(30)
            tortuga.end_fill()
            tortuga.penup()
            tortuga.goto(x + 45, y)
            tortuga.pendown()
            tortuga.begin_fill()
            tortuga.circle(30)
            tortuga.end_fill()
            tortuga.penup()
            
             # Finalizar y mostrar ventana
        tortuga.hideturtle()
        tortuga.stamp()
        tortuga.penup()

    def escena2(tortuga, width, height, color):

        # Dibujar el marco 1
        tortuga.penup()
        tortuga.setpos(-450, 335)  
        tortuga.pendown()
        tortuga.color("black")
        for _ in range(2):
            tortuga.forward(900)  
            tortuga.right(90)
            tortuga.forward(500)  
            tortuga.right(90)

        # Dibujar el marco 2
        tortuga.penup()
        tortuga.setpos(-450, 280)  
        tortuga.pendown()
        tortuga.color("black")
        for _ in range(2):
            tortuga.forward(900)  
            tortuga.right(90)
            tortuga.forward(600)  
            tortuga.right(90)


            ventana = turtle.Screen()
            ventana.bgcolor("sky blue")
            tortuga.speed(40)
        tortuga.penup()
            

        # Dibujo de la primera casa
        # Cuerpo de la casa
        tortuga.goto(-350, -100)
        tortuga.pendown()
        tortuga.fillcolor("orange")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(100)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        # Techo de la casa
        tortuga.goto(-350, 0)
        tortuga.pendown()
        tortuga.fillcolor("green")
        tortuga.begin_fill()
        for _ in range(3):
            tortuga.forward(100)
            tortuga.left(120)
        tortuga.end_fill()
        tortuga.penup()

        # Ventanas
        tortuga.goto(-340, -40)  # Ajuste de coordenada x de la ventana izquierda
        tortuga.pendown()
        tortuga.fillcolor("sky blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(30)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        tortuga.goto(-290, -40)  # Ajuste de coordenada x de la ventana derecha
        tortuga.pendown()
        tortuga.fillcolor("sky blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(30)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        # Puerta
        tortuga.goto(-310, -60)  # Ajuste de coordenada x de la puerta
        tortuga.pendown()
        tortuga.fillcolor("brown")
        tortuga.begin_fill()
        for _ in range(2):
            tortuga.forward(20)
            tortuga.right(90)
            tortuga.forward(40)
            tortuga.right(90)
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo de la cuarta casa
        # Cuerpo de la casa
        tortuga.goto(-175, 0)
        tortuga.pendown()
        tortuga.fillcolor("orange")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(100)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        # Techo de la casa
        tortuga.goto(-175, 100)
        tortuga.pendown()
        tortuga.fillcolor("green")
        tortuga.begin_fill()
        for _ in range(3):
            tortuga.forward(100)
            tortuga.left(120)
        tortuga.end_fill()
        tortuga.penup()

        # Ventanas
        tortuga.goto(-165, 60)  # Ajuste de coordenada x de la ventana izquierda
        tortuga.pendown()
        tortuga.fillcolor("sky blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(30)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        tortuga.goto(-115, 60)  # Ajuste de coordenada x de la ventana derecha
        tortuga.pendown()
        tortuga.fillcolor("sky blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(30)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        # Puerta
        tortuga.goto(-135, 40)  # Ajuste de coordenada x de la puerta
        tortuga.pendown()
        tortuga.fillcolor("brown")
        tortuga.begin_fill()
        for _ in range(2):
            tortuga.forward(20)
            tortuga.right(90)
            tortuga.forward(40)
            tortuga.right(90)
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo de la segunda casa
        # Cuerpo de la casa
        tortuga.goto(300, -100)
        tortuga.pendown()
        tortuga.fillcolor("orange")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(100)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        # Techo de la casa
        tortuga.goto(300, 0)
        tortuga.pendown()
        tortuga.fillcolor("green")
        tortuga.begin_fill()
        for _ in range(3):
            tortuga.forward(100)
            tortuga.left(120)
        tortuga.end_fill()
        tortuga.penup()

        # Ventanas
        tortuga.goto(310, -40)  # Ajuste de coordenada x de la ventana izquierda
        tortuga.pendown()
        tortuga.fillcolor("sky blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(30)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        tortuga.goto(360, -40)  # Ajuste de coordenada x de la ventana derecha
        tortuga.pendown()
        tortuga.fillcolor("sky blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(30)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        # Puerta
        tortuga.goto(340, -60)  # Ajuste de coordenada x de la puerta
        tortuga.pendown()
        tortuga.fillcolor("brown")
        tortuga.begin_fill()
        for _ in range(2):
            tortuga.forward(20)
            tortuga.right(90)
            tortuga.forward(40)
            tortuga.right(90)
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo de la tercera casa
        # Cuerpo de la casa
        tortuga.goto(150, 0)
        tortuga.pendown()
        tortuga.fillcolor("orange")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(100)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        # Techo de la casa
        tortuga.goto(150, 100)
        tortuga.pendown()
        tortuga.fillcolor("green")
        tortuga.begin_fill()
        for _ in range(3):
            tortuga.forward(100)
            tortuga.left(120)
        tortuga.end_fill()
        tortuga.penup()

        # Ventanas
        tortuga.goto(160, 60)  # Ajuste de coordenada x de la ventana izquierda
        tortuga.pendown()
        tortuga.fillcolor("sky blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(30)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        tortuga.goto(210, 60)  # Ajuste de coordenada x de la ventana derecha
        tortuga.pendown()
        tortuga.fillcolor("sky blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(30)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        # Puerta
        tortuga.goto(190, 40)  # Ajuste de coordenada x de la puerta
        tortuga.pendown()
        tortuga.fillcolor("brown")
        tortuga.begin_fill()
        for _ in range(2):
            tortuga.forward(20)
            tortuga.right(90)
            tortuga.forward(40)
            tortuga.right(90)
        tortuga.end_fill()
        tortuga.penup()

         # Dibujo del perro café
        tortuga.goto(-200, -100)
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del perro
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del perro café
        tortuga.goto(-215, -50)
        tortuga.dot(10, "black")
        tortuga.goto(-185, -50)
        tortuga.dot(10, "black")
        tortuga.goto(-200, -70)
        tortuga.dot(5, "black")

        # Orejas del perro café
        tortuga.goto(-225, -30)
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(-175, -30)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del perro amarillo
        tortuga.goto(0, -100)
        tortuga.pendown()
        tortuga.color("yellow")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del perro
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del perro amarillo
        tortuga.goto(-15, -50)
        tortuga.dot(10, "black")
        tortuga.goto(15, -50)
        tortuga.dot(10, "black")
        tortuga.goto(0, -70)
        tortuga.dot(5, "black")

        # Orejas del perro amarillo
        tortuga.goto(-25, -30)
        tortuga.pendown()
        tortuga.color("yellow")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(25, -30)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del gato rojo
        tortuga.goto(200, -100)
        tortuga.pendown()
        tortuga.color("orange")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del gato
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del gato rojo
        tortuga.goto(185, -50)
        tortuga.dot(10, "black")
        tortuga.goto(215, -50)
        tortuga.dot(10, "black")
        tortuga.goto(200, -70)
        tortuga.dot(5, "black")

        # Orejas del gato rojo
        tortuga.goto(225, -30)
        tortuga.pendown()
        tortuga.color("orange")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(175, -30)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo de las nubes
        for x, y in [(0, 205), (200, 185), (-200,190)]:
            tortuga.goto(x, y)
            tortuga.color("white")
            tortuga.pendown()
            tortuga.begin_fill()
            tortuga.circle(30)
            tortuga.end_fill()
            tortuga.penup()
            tortuga.goto(x + 45, y)
            tortuga.pendown()
            tortuga.begin_fill()
            tortuga.circle(30)
            tortuga.end_fill()
            tortuga.penup()

        # Dibujo del sol amarillo
        tortuga.goto(-350, 160)
        tortuga.color("yellow")
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(50)
        tortuga.end_fill()
        tortuga.penup()
        

        # Finalizar y mostrar ventana
        tortuga.hideturtle()
        tortuga.stamp()
        tortuga.penup()
    
    def escena3(tortuga, width, height, color):

        # Dibujar el marco 1
        tortuga.penup()
        tortuga.setpos(-450, 335)  
        tortuga.pendown()
        tortuga.color("black")
        for _ in range(2):
            tortuga.forward(900)  
            tortuga.right(90)
            tortuga.forward(500)  
            tortuga.right(90)

        # Dibujar el marco 2
        tortuga.penup()
        tortuga.setpos(-450, 280)  
        tortuga.pendown()
        tortuga.color("black")
        for _ in range(2):
            tortuga.forward(900)  
            tortuga.right(90)
            tortuga.forward(600)  
            tortuga.right(90)

            ventana = turtle.Screen()
            ventana.bgcolor("skyblue")  # Fondo celeste para mejor contraste
            tortuga.speed(30)
        tortuga.penup()

        # Dibuja un charco en forma ovalada más grande
        tortuga.penup()
        tortuga.goto(0, -100)  # Ajusta la posición inicial del charco hacia abajo para más espacio
        tortuga.pendown()
        tortuga.color("blue")
        tortuga.begin_fill()
        tortuga.left(45)  # Inclina la elipse para el charco
        for _ in range(2):  # Dibuja una elipse más grande
            tortuga.circle(150, 90)  # Aumenta el radio largo de la elipse
            tortuga.circle(150//2, 90)  # Aumenta el radio corto de la elipse
        tortuga.end_fill()
        tortuga.penup()

        # Dibuja las piedras
        # Primera piedra
        tortuga.penup()
        tortuga.goto(-90, 10)  # Ajusta la posición para que coincida con el charco más grande
        tortuga.pendown()
        tortuga.color("gray")
        tortuga.begin_fill()
        tortuga.circle(20)  # Tamaño de la primera piedra
        tortuga.end_fill()
        tortuga.penup()

        # Segunda piedra
        tortuga.penup()
        tortuga.goto(-40, -20)  # Ajusta la posición para que coincida con el charco más grande
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(15)  # Tamaño de la segunda piedra
        tortuga.end_fill()
        tortuga.penup()

        # Tercera piedra
        tortuga.penup()
        tortuga.goto(10, -5)  # Ajusta la posición para que coincida con el charco más grande
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(15)  # Tamaño de la tercera piedra
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del perro café
        tortuga.goto(-200, -100)
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del perro
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del perro café
        tortuga.goto(-240, -50)
        tortuga.dot(10, "black")
        tortuga.goto(-210, -50)
        tortuga.dot(10, "black")
        tortuga.goto(-225, -70)
        tortuga.dot(5, "black")

        # Orejas del perro café
        tortuga.goto(-245, -40)
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(-200, -40)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del perro amarillo
        tortuga.goto(-300, 0)
        tortuga.pendown()
        tortuga.color("yellow")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del perro
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del perro amarillo
        tortuga.goto(-340, 45)
        tortuga.dot(10, "black")
        tortuga.goto(-310, 45)
        tortuga.dot(10, "black")
        tortuga.goto(-325, 30)
        tortuga.dot(5, "black")

        # Orejas del perro amarillo
        tortuga.goto(-355, 50)
        tortuga.pendown()
        tortuga.color("yellow")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(-285, 50)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del gato rojo
        tortuga.goto(-150, 0)
        tortuga.pendown()
        tortuga.color("orange")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del gato
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del gato rojo
        tortuga.goto(-190, 45)
        tortuga.dot(10, "black")
        tortuga.goto(-160, 45)
        tortuga.dot(10, "black")
        tortuga.goto(-175, 30)
        tortuga.dot(5, "black")

        # Orejas del gato rojo
        tortuga.goto(-205, 50)
        tortuga.pendown()
        tortuga.color("orange")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(-135, 50)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo de las nubes
        for x, y in [(0, 205), (200, 185), (-200,190)]:
            tortuga.goto(x, y)
            tortuga.color("white")
            tortuga.pendown()
            tortuga.begin_fill()
            tortuga.circle(30)
            tortuga.end_fill()
            tortuga.penup()
            tortuga.goto(x + 45, y)
            tortuga.pendown()
            tortuga.begin_fill()
            tortuga.circle(30)
            tortuga.end_fill()
            tortuga.penup()

        # Dibujo del sol amarillo
        tortuga.goto(-350, 160)
        tortuga.color("yellow")
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(50)
        tortuga.end_fill()
    
        tortuga.penup()

    def escena4(tortuga, width, height, color):

        # Dibujar el marco 1
        tortuga.penup()
        tortuga.setpos(-450, 335)  
        tortuga.pendown()
        tortuga.color("black")
        for _ in range(2):
            tortuga.forward(900)  
            tortuga.right(90)
            tortuga.forward(500)  
            tortuga.right(90)

        # Dibujar el marco 2
        tortuga.penup()
        tortuga.setpos(-450, 280)  
        tortuga.pendown()
        tortuga.color("black")
        for _ in range(2):
            tortuga.forward(900)  
            tortuga.right(90)
            tortuga.forward(600)  
            tortuga.right(90)
            ventana = turtle.Screen()
            ventana.bgcolor("gray")
            tortuga.speed(40)
        tortuga.penup()

        # Dibujo de la primera casa
        # Cuerpo de la casa
        tortuga.goto(-350, -100)
        tortuga.pendown()
        tortuga.fillcolor("pink")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(100)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        # Techo de la casa
        tortuga.goto(-350, 0)
        tortuga.pendown()
        tortuga.fillcolor("purple")
        tortuga.begin_fill()
        for _ in range(3):
            tortuga.forward(100)
            tortuga.left(120)
        tortuga.end_fill()
        tortuga.penup()

        # Ventanas
        tortuga.goto(-340, -40)  # Ajuste de coordenada x de la ventana izquierda
        tortuga.pendown()
        tortuga.fillcolor("sky blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(30)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        tortuga.goto(-290, -40)  # Ajuste de coordenada x de la ventana derecha
        tortuga.pendown()
        tortuga.fillcolor("sky blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(30)
            tortuga.left(90)
        tortuga.end_fill()
        tortuga.penup()

        # Puerta
        tortuga.goto(-310, -60)  # Ajuste de coordenada x de la puerta
        tortuga.pendown()
        tortuga.fillcolor("brown")
        tortuga.begin_fill()
        for _ in range(2):
            tortuga.forward(20)
            tortuga.right(90)
            tortuga.forward(40)
            tortuga.right(90)
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo de las nubes
        for x, y in [(0, 205), (200, 185), (-200, 190)]:
            for offset in [0, 45]:  # Dibuja dos partes de cada nube
                tortuga.goto(x + offset, y)
                tortuga.color("white")
                tortuga.pendown()
                tortuga.begin_fill()
                tortuga.circle(30)
                tortuga.end_fill()
                tortuga.penup()

        # Agregar lluvia
        tortuga.color("blue")
        for x, y in [(0, 205), (200, 185), (-200, 190)]:
            for offset in [0, 45]:  # Agrega lluvia debajo de cada parte de la nube
                for i in range(-10, 10, 5):  # Varias gotas de lluvia por nube
                    tortuga.goto(x + offset + i, y - 30)  # Posición inicial de la lluvia
                    tortuga.pendown()
                    tortuga.right(90)  # Asegura que la tortuga apunte hacia abajo
                    tortuga.forward(20)  # Longitud de la lluvia
                    tortuga.penup()
                    tortuga.left(90)  # Reestablece la orientación de la tortuga


        # Dibujo del perro café
        tortuga.goto(-200, -100)
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del perro
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del perro café
        tortuga.goto(-215, -50)
        tortuga.dot(10, "black")
        tortuga.goto(-185, -50)
        tortuga.dot(10, "black")
        tortuga.goto(-200, -70)
        tortuga.dot(10, "black")
        tortuga.goto(-200, -90)
        tortuga.dot(12, "black")

        # Orejas del perro café
        tortuga.goto(-225, -30)
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(-175, -30)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del perro amarillo
        tortuga.goto(0, -100)
        tortuga.pendown()
        tortuga.color("yellow")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del perro
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del perro amarillo
        tortuga.goto(-15, -50)
        tortuga.dot(10, "black")
        tortuga.goto(15, -50)
        tortuga.dot(10, "black")
        tortuga.goto(0, -70)
        tortuga.dot(5, "black")

        # Orejas del perro amarillo
        tortuga.goto(-25, -30)
        tortuga.pendown()
        tortuga.color("yellow")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(25, -30)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del gato rojo
        tortuga.goto(200, -100)
        tortuga.pendown()
        tortuga.color("orange")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del gato
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del gato rojo
        tortuga.goto(185, -50)
        tortuga.dot(10, "black")
        tortuga.goto(215, -50)
        tortuga.dot(10, "black")
        tortuga.goto(200, -70)
        tortuga.dot(5, "black")

        # Orejas del gato rojo
        tortuga.goto(225, -30)
        tortuga.pendown()
        tortuga.color("orange")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(175, -30)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        tortuga.penup()

    def escena5(tortuga, width, height, color):

        # Dibujar el marco 1
        tortuga.penup()
        tortuga.setpos(-450, 335)  
        tortuga.pendown()
        tortuga.color("black")
        for _ in range(2):
            tortuga.forward(900)  
            tortuga.right(90)
            tortuga.forward(500)
            tortuga.right(90)

        # Dibujar el marco 2
        tortuga.penup()
        tortuga.setpos(-450, 280)  
        tortuga.pendown()
        tortuga.color("black")
        for _ in range(2):
            tortuga.forward(900)  
            tortuga.right(90)
            tortuga.forward(600)  
            tortuga.right(90)

            
            ventana = turtle.Screen()
            ventana.bgcolor("sky blue")
            tortuga.speed(40)
        tortuga.penup()

        # Dibujo del perro café
        tortuga.goto(-200, -100)
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del perro
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del perro café
        tortuga.goto(-205, -40)
        tortuga.dot(10, "black")
        tortuga.goto(-185, -40)
        tortuga.dot(10, "black")
        tortuga.goto(-190, -55)
        tortuga.dot(5, "black")
        tortuga.goto(-190, -70)
        tortuga.dot(10, "black")

        # Orejas del perro café
        tortuga.goto(-235, -40)
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(-170, -40)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del perro amarillo
        tortuga.goto(-300, 0)
        tortuga.pendown()
        tortuga.color("yellow")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del perro
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del perro amarillo
        tortuga.goto(-305, 60)
        tortuga.dot(10, "black")
        tortuga.goto(-290, 60)
        tortuga.dot(10, "black")
        tortuga.goto(-295, 50)
        tortuga.dot(5, "black")
        tortuga.goto(-295, 35)
        tortuga.dot(10, "black")

        # Orejas del perro amarillo
        tortuga.goto(-335, 65)
        tortuga.pendown()
        tortuga.color("yellow")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(-275, 65)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibujo del gato rojo
        tortuga.goto(-142, 0)
        tortuga.pendown()
        tortuga.color("orange")
        tortuga.begin_fill()
        tortuga.circle(40)  # cuerpo del gato
        tortuga.end_fill()
        tortuga.penup()

        # Ojos y nariz del gato rojo
        tortuga.goto(-145, 60)
        tortuga.dot(10, "black")
        tortuga.goto(-125, 60)
        tortuga.dot(10, "black")
        tortuga.goto(-130, 50)
        tortuga.dot(5, "black")
        tortuga.goto(-130, 35)
        tortuga.dot(10, "black")

        # Orejas del gato rojo
        tortuga.goto(-175, 65)
        tortuga.pendown()
        tortuga.color("orange")
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja izquierda
        tortuga.end_fill()
        tortuga.penup()
        tortuga.goto(-120, 65)
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(10)  # oreja derecha
        tortuga.end_fill()
        tortuga.penup()

        # Dibuja dos pizzas pequeñas
        tortuga.penup()
        tortuga.goto(-50, -50)  # Posición de la primera pizza
        tortuga.pendown()
        tortuga.color("sandy brown")
        tortuga.begin_fill()
        tortuga.circle(40)  # Radio para una pizza pequeña
        tortuga.end_fill()

        # Toppings para la primera pizza
        tortuga.penup()
        tortuga.goto(-60, 10)
        tortuga.color("red")
        for _ in range(2):  # Simula algunos pepperonis
            tortuga.dot(10)
            tortuga.forward(20)
        tortuga.penup()
        tortuga.goto(-60, 0)
        tortuga.color("red")
        for _ in range(2):  # Simula algunos pepperonis
            tortuga.dot(10)
            tortuga.forward(20)
        tortuga.penup()
        tortuga.goto(-60, -10)
        tortuga.color("red")
        for _ in range(2):  # Simula algunos pepperonis
            tortuga.dot(10)
            tortuga.forward(20)
        tortuga.penup()
        tortuga.goto(-60, -20)
        tortuga.color("red")
        for _ in range(2):  # Simula algunos pepperonis
            tortuga.dot(10)
            tortuga.forward(20)
        tortuga.penup()
        tortuga.goto(-60, -30)
        tortuga.color("red")
        for _ in range(2):  # Simula algunos pepperonis
            tortuga.dot(10)
            tortuga.forward(20)
        # Segunda pizza
        tortuga.penup()
        tortuga.goto(40, -50)  # Posición de la segunda pizza
        tortuga.pendown()
        tortuga.color("sandy brown")
        tortuga.begin_fill()
        tortuga.circle(40)  # Radio para la segunda pizza pequeña
        tortuga.end_fill()

        # Toppings para la segunda pizza
        tortuga.penup()
        tortuga.goto(30, 10)
        tortuga.color("red")
        for _ in range(2):  # Simula algunos pepperonis
            tortuga.dot(10)
            tortuga.forward(20)
        tortuga.penup()
        tortuga.goto(30, 0)
        tortuga.color("red")
        for _ in range(2):  # Simula algunos pepperonis
            tortuga.dot(10)
            tortuga.forward(20)
        tortuga.penup()
        tortuga.goto(30, -10)
        tortuga.color("red")
        for _ in range(2):  # Simula algunos pepperonis
            tortuga.dot(10)
            tortuga.forward(20)
        tortuga.penup()
        tortuga.goto(30, -20)
        tortuga.color("red")
        for _ in range(2):  # Simula algunos pepperonis
            tortuga.dot(10)
            tortuga.forward(20)
        tortuga.penup()
        tortuga.goto(30, -30)
        tortuga.color("red")
        for _ in range(2):  # Simula algunos pepperonis
            tortuga.dot(10)
            tortuga.forward(20)

       # Dibuja el edificio principal
        tortuga.penup()
        tortuga.goto(100, -100)  # Nueva posición ajustada para la base del edificio
        tortuga.pendown()
        tortuga.color("yellow")  # Color del edificio
        tortuga.begin_fill()
        for _ in range(2):  # Crea un rectángulo
            tortuga.forward(300)
            tortuga.left(90)
            tortuga.forward(200)
            tortuga.left(90)
        tortuga.end_fill()

        # Dibuja el techo
        tortuga.penup()
        tortuga.goto(100, 100)
        tortuga.pendown()
        tortuga.color("red")  # Color del techo
        tortuga.begin_fill()
        tortuga.goto(250, 150)  # Punto medio del techo
        tortuga.goto(400, 100)  # Completa el triángulo del techo
        tortuga.goto(100, 100)
        tortuga.end_fill()

        # Dibuja una puerta
        tortuga.penup()
        tortuga.goto(220, -100)  # Posición de la puerta ajustada
        tortuga.pendown()
        tortuga.color("brown")
        tortuga.begin_fill()
        for _ in range(2):
            tortuga.forward(50)
            tortuga.left(90)
            tortuga.forward(80)
            tortuga.left(90)
        tortuga.end_fill()

        # Dibuja ventanas
        tortuga.penup()
        tortuga.goto(125, -20)  # Ventana izquierda ajustada
        tortuga.pendown()
        tortuga.color("blue")
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(40)
            tortuga.left(90)
        tortuga.end_fill()

        tortuga.penup()
        tortuga.goto(325, -20)  # Ventana derecha ajustada
        tortuga.pendown()
        tortuga.begin_fill()
        for _ in range(4):
            tortuga.forward(40)
            tortuga.left(90)
        tortuga.end_fill()

        # Dibuja el letrero de la pizzería
        tortuga.penup()
        tortuga.goto(210, 100)  # Posición del letrero ajustada
        tortuga.pendown()
        tortuga.color("white")
        tortuga.write("Pizzería", font=("Arial", 18, "bold"))
        tortuga.penup()

        # Dibujo de las nubes
        for x, y in [(0, 205), (200, 185), (-200,190)]:
            tortuga.goto(x, y)
            tortuga.color("white")
            tortuga.pendown()
            tortuga.begin_fill()
            tortuga.circle(30)
            tortuga.end_fill()
            tortuga.penup()
            tortuga.goto(x + 45, y)
            tortuga.pendown()
            tortuga.begin_fill()
            tortuga.circle(30)
            tortuga.end_fill()
            tortuga.penup()

        # Dibujo del sol amarillo
        tortuga.goto(-350, 160)
        tortuga.color("yellow")
        tortuga.pendown()
        tortuga.begin_fill()
        tortuga.circle(50)
        tortuga.end_fill()
        tortuga.penup()


def mostrarescena(escena, pantalla, tortuga, nombre):
    # Limpiar pantalla
    tortuga.clear()

    # Mostrar el título de la secuencia
    tortuga.goto(INICIALTEXTO)
    tortuga.color("black")
    tortuga.write(escena["titulo"], font=("Arial", 18, "bold"))
    tortuga.color("black")

    # Llamar a la función correspondiente para dibujar la escena
    if escena["titulo"] == "La Aventura de las mascotas - Encuentro en el Parque":
        escena1(tortuga, ANCHO, ALTO,colorfavorito)  # Llamar a la función scene1 para dibujar la primera escena
    elif escena["titulo"] == "La Aventura de las mascotas - Travesía por la Ciudad":
        escena2(tortuga, ANCHO, ALTO,colorfavorito)  # Llamar a la función scene2 para dibujar la segunda escena
    elif escena["titulo"] == "La Aventura de las mascotas - El Desafío del Charco":
        escena3(tortuga, ANCHO, ALTO,colorfavorito)  # Llamar a la función scene3 para dibujar la tercera escena
    elif escena["titulo"] == "La Aventura de las mascotas - La Búsqueda del Hogar Perdido":
        escena4(tortuga, ANCHO, ALTO, colorfavorito) # Llamar a la función scene4 para dibujar la tercera escena
    elif escena["titulo"] == "La Aventura de las mascotas - Celebración en la Pizzeria":
        escena5(tortuga, ANCHO, ALTO,colorfavorito) # Llamar a la función scene5 para dibujar la tercera escena

    # Mostrar la narrativa de la secuencia
    tortuga.goto(INICIALNARRATIVA)
    tortuga.color("black")
    tortuga.write(escena["narrativa"].format(nombreniño=nombre), font=("Arial", 12), align="left")

def mostrarcuento(escenas, nombre):
    pantalla = turtle.Screen()
    pantalla.setup(width=ANCHOVENTANA, height=ALTOVENTANA)
    pantalla.title("Cuento Infantil (PROYECTO 01)")

    tortuga = turtle.Turtle()
    tortuga.penup()
    tortuga.speed(0)
    tortuga.goto(-200, 200)
    tortuga.hideturtle()

    while True:
        print("¡Bienvenido al cuento infantil interactivo!")
        print("Elige una escena:")
        for i, secuencia in enumerate(escenas):
            print(f"{i+1}. {secuencia['titulo']}")

        seleccion = int(input("Ingrese el número de la escena que desea ver: "))

        if 1 <= seleccion <= len(escenas):
            mostrarescena(escenas[seleccion - 1], pantalla, tortuga, nombre)
        else:
            print("Selección no válida. El número de escena debe estar dentro del rango disponible.")

        continuar = str(input("¿Desea ver otra escena? (Sí/No): ")).lower()
        if continuar != "sí" and continuar != "si":
            print("Gracias por disfrutar. ¡Hasta la próxima!")
            break

    pantalla.mainloop()


# Arreglo con cada escena
historia = [
    {
        "titulo": "La Aventura de las mascotas - Encuentro en el Parque",
        "narrativa": f"""
        Pipo, un perro travieso, se topa con Luna, una perrita perdida. 
        Deciden buscar su hogar juntos. En su búsqueda, se les une {nombreniño} de 
        {edadniño} años, el gato aventurero que curiosea entre los arbustos.
    """
    },
    {
        "titulo": "La Aventura de las mascotas - Travesía por la Ciudad",
        "narrativa": f"""
        Los tres amigos recorren las calles de la ciudad en busca del hogar de Luna. 
        {nombreniño} de {edadniño} años, el gato, se desliza ágilmente 
        entre los callejones mientras Pipo y Luna lo siguen con entusiasmo.
        """
    },
    {
        "titulo": "La Aventura de las mascotas - El Desafío del Charco",
        "narrativa": f"""
        Un gran charco bloquea su camino. Luna teme mojarse, pero con el ingenio de 
        {nombreniño} de {edadniño} años y el ánimo de Pipo, encuentran una 
        manera creativa de cruzarlo saltando de piedra en piedra.
        """
    },
    {
        "titulo": "La Aventura de las mascotas - La Búsqueda del Hogar Perdido",
        "narrativa": f"""
        Llegan a la casa de Luna, pero descubren que su familia se ha mudado.{nombreniño} de {edadniño} años
        alienta a Luna para que se animará, pero no obtuvo ningún resultado. Tristes, deciden formar una nueva familia 
        entre ellos y explorar la ciudad juntos.

        """
    },
    {
         "titulo": "La Aventura de las mascotas - Celebración en la Pizzeria",
        "narrativa": f"""
        Luego los 3 deciden ir a comer pizza para cerrar un gran día dónde los 3 se hicieron una gran familia.
        {nombreniño} de {edadniño} años estaba tan feliz de poder haber conseguido una gran familia.
        """
    }
]

# Mostrar
mostrarcuento(historia, nombreniño)