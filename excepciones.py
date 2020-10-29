#Errores sintacticos


"""
while(True):
    try:
        n=float(input("Introduce un numero: "))
        m=4
        print("{}/{}={}".format(n,m,n/m))
    except:    
        print("Ha ocurrido un error, introduce bien el numero")
    else:
        print("Todo a funcionado correctamente")
        break
    finally:
        print("Fin de la iteracion")
"""




"""
try:
    n2 = input("Introduce un numero: ")
    5/n2
except Exception as e:
    print(type(e).__name__)
"""



"""
def mi_funcion(algo=None):
    if algo is None:
       raise ValueError("Error! no se permite un valor nulo")
mi_funcion()
"""



"""
try:
    n2 = float(input("Introduce un numero: "))
    5/n2
except TypeError:
    print("No se puede dividir el numero entre una cadena")
except ValueError:
    print("Debes introducir una cadena que sea un número!!")    
except ZeroDivisionError:
    print("No se puede dividir entre 0!!")        
except Exception as e:
    print(type(e).__name__)
"""    





def mi_funcion(algo=None):
    try:
        if algo is None:
            raise ValueError("Error! no se permite un valor nulo")
    except ValueError:
        print("Error !! no se permite un valor nulo (desde la excepcion)")
   
mi_funcion()

