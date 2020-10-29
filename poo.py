class Galleta():
    chocolate = False

    #Metodo especial que se ejectuta al crear un objecto,
    #permite enviar argumentos al instanciar
    def __init__(self, sabor=None, forma=None):
        self.sabor = sabor
        self.forma = forma
        print("Se acaba de crear una galleta {} {}".format(sabor, forma))

    def chocolatear(self):
        self.chocolate = True    

    def tiene_chocolate(self):
        if self.chocolate:
            print("Soy una galleta chocolateada :-D") 
        else:       
            print("Soy una galleta sin chocolate :-(") 



class Pelicula():
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha creado la pelicula ", self.titulo)

    #desctructor de clase
    def __del__(self):
        print("Se esta borrando la pelicula ", self.titulo)    

    def __str__(self):
        return "{} lanzada en {} con una duracion de {} minutos".format(self.titulo, self.lanzamiento, self.duracion)    
    

    def __len__(self):
        return self.duracion



class Catalogo():
    peliculas = []

    def __init__(self,peliculas=[]):
        self.peliculas = peliculas

    def agregar(self, p):
        self.peliculas.append(p)


    def mostrar(self):
        for p in self.peliculas:
            print(p)       

class Ejemplo:
    __atributo_privado ="Soy un metodo inalcanzable desde fuera"


    def __metodo_privado(self):
        print("soy un metodo inalcanzable desde fuera")   

    def atributo_publico(self):
        return self.__atributo_privado          

    def metodo_publico(self):
        return self.__metodo_privado                 


e = Ejemplo()
print(e.atributo_publico())
print(e.metodo_publico())
"""
p = Pelicula("El padrino", 175, 1972)
c = Catalogo( [p] )
c.mostrar()
c.agregar(Pelicula("El padrino parte 2", 202, 1974))
c.mostrar()
"""

#p = Pelicula("El padrino", 175, 1972)
#del(p)        
#print(str(p))
#print(len(p))



#g = Galleta("salada", "Cuadrada")
#g.tiene_chocolate()
#g.chocolatear()
#g.tiene_chocolate()


#g=Galleta()

