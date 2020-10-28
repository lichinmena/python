#funcion
def saludar():
    print("Hola este print se llama desde la funcion saludar")

saludar()    


def dibujar_tabla_del_5():
    for i in range(10):
        print("5 * ", i, " = ",i*5)
dibujar_tabla_del_5()    


def test():
    n=10
    return n
test()    



m=10
def test2():
    print(m)
test2()    


def mi_funcion():
    return "cadena"

miCadena = mi_funcion()
print(miCadena)



def funcion_array():
    return [1,2,3,4,5]
print(funcion_array())    
print(funcion_array()[-1]) 
print(funcion_array()[1:4]) 

l = funcion_array()



#RETURNA UNA TUPLA
def funcion_array_2():
    return "Una cadena", 20, [1,2,3]
print(funcion_array_2())    
cadena, numero, lista = funcion_array_2()
print(cadena)
print(numero)
print(lista)


#Envio de valores
def suma(a,b): #parametros
    return a+b
r = suma(5,10) #argumentos
print(r)    

def resta(a=None, b=None):
    if a==None or b == None:
        print("Error, debes enviar dos numeros a la funcion")
        return
    return a-b
print(resta(5,3))    


#Argumentos por valor
def doblar_valores_1(numero):
    numero*2
n = 10
print(doblar_valores_1(n))
print(n)    




#Argumentos por referencia
def doblar_valores_2(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *= 2
ns = [10,20,30]
print(doblar_valores_2(ns))
print(ns)   


#Truco #1
def doblar_valores_3(numero):
    return numero*2
n=10
n=doblar_valores_3(n)
print(n) 



#Argumentos por referencia Truco #2
def doblar_valores_4(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *= 2
ns = [10,50,100]
print(doblar_valores_4(ns[:]))
print(ns)  



def indeterminados_posicion(*args): #devuelve una tupla, inmutables
    print(args)

indeterminados_posicion(5,"Hola", [1,2,3,4,5])



#Acepta una lista como argumento
def indeterminados_posicion_2(*args): #devuelve una tupla, inmutables
    for arg in args:
        print(arg)

indeterminados_posicion_2(5,"Hola", [1,2,3,4,5])







#Acepta un direccionario como argumento
def indeterminados_posicion_3(**kwargs): #devuelve una diccionario, inmutables
    print(kwargs)

indeterminados_posicion_3(n=5,c="Hola", l=[1,2,3,4,5])





#Acepta un direccionario como argumento
def indeterminados_posicion_4(**kwargs): #devuelve una tupla, inmutables
    for kwarg in kwargs:
        print(kwarg, " " , kwargs[kwarg])

indeterminados_posicion_4(n=5,c="Hola", l=[1,2,3,4,5])




def superfuncion(*args, **kwargs):
    t = 0
    for arg in args:
        t+=arg
    print("sumatorio es: ", t)

    for kwarg in kwargs:
        print(kwarg, " " , kwargs[kwarg])
superfuncion(10,50,-1,1.56, nombre="Hector", edad=27)

#Recursividad sin retorno
def cuenta_atras(num):
    num -= 1
    if(num > 0):
        print(num)
        cuenta_atras(num)
    else:
        print("Booommmmmm!")
    print("Fin de la funcion: ", num)    
cuenta_atras(5)


def factorial(num):
    print("valor inicial -> ", num)  
    if num > 1:
        num= num * factorial(num - 1)
    print("valor final -> ", num)    
    return num    
print(factorial(5))








