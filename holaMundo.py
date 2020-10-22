print("Hola mundo")

#suma
print(3+5)

#Multiplicion
print(3*2)

#Comentario
print(3/2)

#modulo
print(3%2)

#potencia
print(3**2)

#Jerarquia de operaciones
print(3-2+4*10)

n=3
print(n)
print(n+3)
print(n*2)
print(n*n)

print("""Texto en distintas
linea 1
linea 2
linea 3
""")

palabra="Python"
print(palabra[0])
print(palabra[1])
print(palabra[2])

print(palabra[-1])
print(palabra[-2])
print(palabra[-3])

#slicing
print(palabra[0:2]) #se excluye el ultimo

print(palabra[0:-1]) #se excluye el ultimo

print(palabra[2:]) #toma el ultimo

print(palabra[:2]) #del inicio al final

print(palabra[:]) #Toda la cadena

#Una cadena en python es inmutable

print("Listas ======================")

numeros = [1,2,3,4,5,6,7,8,9,10]
datos = [4,"Uno",-15,-10,5,"Otra cadena"]

print(numeros)
print(datos)

#Agregar
numeros.append(11)
print(numeros)

#longitud
print(len(numeros))


""" ==================================================
Leer consola
"""
#num1 = input("Ingresa el numero 1: ")
#num2 = input("Ingresa el numero 2: ")
num1 = 22
num2 = 11
print(type(num1))
print(type(num2))
num1 = int(num1)
num2 = int(num2)
print(type(num1))
print(type(num2))
num1 = float(num1)
num2 = float(num2)
print(type(num1))
print(type(num2))
print(num1)
print(num2)

#operadores
c = "Hola mundo"
res = len(c) >= 20 and c[0] == "H"
print(res)

x = "SALIR"
res2 = x == "EXIT" or x =="FIN" or x == "SALIR"
print(res2)

#Incrementador
inc = 0
print(inc)
inc += 5
print(inc)
inc += 5
print(inc)
inc += 5
print(inc)
inc += 5
print(inc)

inc -= 2
print(inc)
inc -= 2
print(inc)
inc -= 2
print(inc)
inc -= 2
print(inc)
inc -= 2
print(inc)


n = 20
while n < 30:
    if (n % 2) == 0:
        print(n,"es un numero par")
    else:
        print(n,"es un numero impar")
    n = n + 1    
    
comando = "SALIR"
if comando == "ENTRAR":
    print("Bienvenido al sistema") 
elif comando == "SALUDAR":
    print("HOLA, espero que la estes pasando super")
elif comando == "SALIR":
     print("Saliendo del sistema.....")    
else:
    print("Este comando no se reconoce")            



var1 = 0
while var1 <= 5:
    var1+=1
    if (var1==4):
        print("Rompemos el bucle cuando var1 vale", var1)
        break
    print("var1 vale", var1)
else:
    print("Se ha completado toda la iteracion")    



var2 = 0
while var2 <= 5:
    var2+=1
    if (var2==3 or var2==4):
        continue
    print("var2 vale", var2)
else:
    print("Se ha completado toda la iteracion y var2 vale: ", var2)   


print("Bienvenido al menu interactivo")
while(True):
    print(""" 
    ¿Que quieres hacer? Escribe una opción
    1) Saludar
    2) Sumar dos números
    3) Salir
    """)    
    opcion = input()
    if(opcion == "1"):
        print("Hola, espero y estes bien")
    elif (opcion == "2"):
        numero1 = float(input("Introduce el numero 1"))    
        numero2 = float(input("Introduce el numero 2"))    
        print("EL resultado es :: ", numero1+numero2)
    elif(opcion == "3"):
        print("Hasta luego.........") 
        break
    else:
        print("Comando desconocido.............")       

#Recorrer listas


for num in numeros:
    print(num)

for index,num in enumerate(numeros):
    print("[",index,"]",num)

cadena = "Hola amigos"
for car in cadena:
    cadena += car * 2
print(cadena)    


for i in range(10):
    print(i)