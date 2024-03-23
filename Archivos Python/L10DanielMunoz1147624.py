#Actividad 01
print('Semana No.10, Ejercicio 01')
mesentrada = int(input('Ingrese un número del 1-12: '))
mesSalida= ''
match mesentrada:
    case 1:
      mesSalida='Enero'
    case 2: 
      mesSalida='Febrero'
    case 3:
      mesSalida='Marzo'
    case 4: 
      mesSalida='Abril'  
    case 5:
      mesSalida='Mayo'
    case 6: 
      mesSalida='Junio'
    case 7:
      mesSalida='Julio'
    case 8: 
      mesSalida='Agosto'
    case 9:
      mesSalida='Septiembre'
    case 10: 
      mesSalida='Octubre'
    case 11:
      mesSalida='Noviembre'
    case 12: 
      mesSalida='Diciembre'
    case _:
      mesSalida='Error: Ingrese un número contenido entre 1-12'
      

print ('El mes es:', mesSalida)


#Actividad 02 
print('Semana No.10, Ejercicio 02')

a = int(input('Ingrese el primer número '))
b= int(input('Ingrese el segundo número '))
c = int(input('Ingrese el tercer número '))

if a <= 0 or b<=0 or c <=0:
    print('Error: El número debe de ser mayor a 0')
if a>b:
  if a>c:
    print(a)
  else:
    if a==c:
      print(a, 'y', b)
    else:
      print(c)
elif a==b:
  if a>c:
    print(a, 'y', b)
  elif a==c:
    print(a, 'y', b, 'y', c)
  else:
    print(c)
else:
  if b>c:
    print(b)
  else:
    if b==c:
      print(b, 'y', c)
    else:
      print(c)

#Actividad 03
print('Semana No.10, Ejercicio 03')

año = int(input('Ingrese su año de nacimiento '))
mes= int(input('Ingrese su mes de nacimiento '))
día = int(input('Ingrese su día de nacimiento '))

match mes:
    case 1:
        if (día<=19):
            print("Capricornio")
        else: 
            print("Acuario")
    case 2:
        if (día<=18):
            print("Acuario")
        else: 
            print("Piscis")
    case 3:
        if (día<=20):
            print("Piscis")
        else: 
            print("Aries")
    case 4:
        if (día<=19):
            print("Aries")
        else: 
            print("Tauro")
    case 5:
        if (día<=20):
            print("Tauro")
        else: 
            print("Géminis")
    case 6:
        if (día<=20):
            print("Géminis")
        else: 
            print("Cáncer")
    case 7:
        if (día<=22):
            print("Cáncer")
        else: 
            print("Leo")
    case 8:
        if (día<=22):
            print("Leo")
        else: 
            print("Virgo")
    case 9:
        if (día<=22):
            print("Virgo")
        else: 
            print("Libra")
    case 10:
        if (día<=22):
            print("Libra")
        else: 
            print("Escorpio")
    case 11:
        if (día<=21):
            print("Escorpio")
        else: 
            print("Sagitario")
    case 12:
        if (día<=21):
            print("Sagitario")
        else: 
            print("Capricornio")