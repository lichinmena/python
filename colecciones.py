from collections import deque
#Tuplas son parecidas a las listas, con la diferencia
#de que son inmutables. 

#Declaracion
tupla = (100,"Hola",[1,2,3,4,5], -50,100)
print(tupla)

#Aceptan indexacion y slincing
print(tupla[0])
print(tupla[-1])
print(tupla[2:])
print(tupla[2][-1])
print(len(tupla))
print(tupla.index('Hola'))

print(tupla.count(100)) #Cuantas veces esta el elemento
print(tupla.count('Que onda'))


#==============================================
#Conjunto de colecciones no ordenados de elementos unicos
#Sirve para eliminar elementos duplicados

conjunto = set()
print(conjunto)
conjunto = {1,2,3,4,5}
print(conjunto)
conjunto.add(6)
conjunto.add(0)
print(conjunto)
personas = {'Hector', 'Juan', 'Mario'}
print('Hector' in personas)
print('Maria' in personas)

print('Hector' not in personas)
print('Maria' not in personas)

test = {'Hector', 'Juan', 'Mario', 'Hector', 'Hector'}
print(test)


#De una lista a un conjunto
l = [1,2,3,3,2,1]
c = set(l)
print(c)

#De un conjunto a una lista
l = list(c)
print(l)

#Convertir
lista = [10,20,30,40,50,10,20,30]
print(lista)
lista = list(set(lista))
print(lista)

#Diccionarios
#Clave, Valor
#Son colecciones desordenadas
diccionario_vacio = {}
print(type(diccionario_vacio))
colores = {"amarillo":"yellow", "azul":"blue", "negro":"black"}
print(colores)
print(colores['azul'])
print(colores['amarillo'])


#Agregar
colores["pink"] = "rosado"
print(colores)

#Eliminar
del(colores["pink"])
print(colores)
print("****************")

#Recorrer forma 1
for color in colores:
    print(color)

print("****************")

#Recorrer forma 2
for color in colores:
    print(colores[color])    

print("****************")    

#Recorrer forma 3
for clave in colores:
    print(clave, colores[clave])       

print("****************")   

#Recorrer forma 4
for c,v in colores.items():
    print(c,"-",v)


#Usos avanzados
personajes = []
p = {"Nombre":"Gandalf", "Clase":"Mago","Raza":"Humano"}
personajes.append(p)

p = {"Nombre":"Legolas", "Clase":"Arquero","Raza":"Elfo"}
personajes.append(p)

p = {"Nombre":"Gimli", "Clase":"Guerrero","Raza":"Enano"}
personajes.append(p)
    
print(personajes)    

for p in personajes:
    print(p['Nombre'],p['Clase'], p['Raza'])


#Pilas y colas..................... 
# Se simulan con listas
#PILAAAAAAAAAAAAAA => LIFO
pila = [3,4,5]
pila.append(6)
pila.append(7)
print(pila)
print(pila.pop()) #Saca
print(pila.pop()) #Saca
print(pila.pop()) #Saca



#Colas ==> FIFO
cola = deque()
print(cola)
cola = deque(["Hector", "Juan", "Miguel"])
print(cola)
deque(['Hector', 'Juan', 'Miguel'])
cola.append('Maria')
cola.append('Arnaldo')
print(cola)
print(cola.popleft()) #Saca
print(cola.popleft()) #Saca
print(cola.popleft()) #Saca
print(cola)