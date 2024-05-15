print('Semana No.11')

n=int(input('Ingrese un número mayor a 0:'))
a=0
b=1
c=0
i=2
resultado=''
if(n>0):
    resultado=str(a)

    if(n>1):
        resultado+= ',' + str(b)
        while (i<n):
            c=a+b
            resultado+= ',' + str(c)
            a=b
            b=c
            i=i+1

        print(resultado)
else:
    print(resultado)

print('Semana No.11, Ejercicio #2 INCISO A')

n=int(input('Ingrese un número mayor a 0:'))

if(n<=0): print('Ingrese un numero mayor a 0')

resultadoA=0

for x in range (1, n+1):
    resultadoA+=(1/x)

print('Inciso a: ', resultadoA)

print('Semana No.11, Ejercicio #2 INCISO B')

n=int(input('Ingrese un número mayor a 0:'))

if(n<=0): print('Ingrese un numero mayor a 0')

resultadoB=0

for y in range (1, n+1):
    resultadoB+=(1/pow(2,y))

print('Inciso b: ', resultadoB)

print('Semana No.11, Ejercicio #2 INCISO C')

z = int(input("Ingrese el valor de x : "))
a = int(input("Ingrese el valor de a : "))
n = int(input("Ingrese el valor de n : "))

ResultadoC = 0

for k in range(n + 1): 
    ResultadoC +=(pow(z, k)) * (pow(a, (n - k)))
print("Inciso c:", ResultadoC)

