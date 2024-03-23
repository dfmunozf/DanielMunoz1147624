print('ejercicio 1')
n1 = int(input('ingrese el primer numero'))
n2 = int(input('ingrese el segundo numero'))

divisionreal = n1/n2
divisionentera= n1//n2
divisionmodular= n1%n2
suma= n1+n2
resta=n1-n2
multiplicación= n1*n2

print(n1,'+', n2, '=', suma)
print(n1,'-', n2, '=', resta)
print(n1,'*', n2, '=', multiplicación)
print(n1,'/', n2, '=', divisionreal)
print(n1,'//', n2, '=', divisionentera)
print(n1,'%', n2, '=', divisionmodular)

print('ejercicio 2')

igualdad=n1==n2
mayorque= n1>n2
menorque= n1<n2
diferencia= n1!=n2

print(n1,'==', n2, '=', igualdad)
print(n1,'>', n2, '=', mayorque)
print(n1,'<', n2, '=', menorque)
print(n1,'!=', n2, '=', diferencia)

print('ejercicio 3')
a = int(input('ingrese el primer numero'))
b = int(input('ingrese el segundo numero'))
c = int(input('ingrese el tercer numero'))

print('i', a*b+c)
print('ii.', a*(b+c))
print ('iii.', a/(b+c))
print('iv', ((3*a+2*b)/pow(c,2)))

print('actividad3, Ejercicio 1')
metros1 = int(input('ingrese metros:'))

km = metros1/1000
millas = km/1.609
pies = metros1*3.281
pulgadas = pies*12

print('km', km)
print('millas', millas)
print('pies', pies)
print('pulgadas', pulgadas)

print('Actividad 3, Ejercicio 2')

metros2 = float(input('Ingrese la cantidad en metros: '))

yardas = metros2 // 0.9144
modyardas = metros2 % 0.9144
pies = modyardas // 0.3
modpies = modyardas % 0.3
pulgadas = int((modpies / 0.3) * 12)  


print('Yardas:', yardas)
print('Pies:', pies)
print('Pulgadas:', pulgadas)

