import copy

class Producto:
    def __init__(self,referencia,nombre,pvp,descripcion):
        self.referencia = referencia
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion

    def __str__(self):
        return """
        REFERENCIA \t{}
        NOMBRE \t\t{}
        PVP\t\t{}
        DESCRIPCION\t{}""".format(self.referencia, self.nombre, self.pvp, self.descripcion)  
        

class Adorno(Producto):
    pass


class Alimento(Producto):
    productor = ""
    distribuidor = ""

    def __str__(self):
        return """
        REFERENCIA \t{}
        NOMBRE \t\t{}
        PVP\t\t{}
        DESCRIPCION\t{}
        PRODUCTOR\t{}
        DISTRIBUIDOR\t{}""".format(self.referencia, self.nombre, self.pvp, self.descripcion,self.productor,self.distribuidor)   



class Libro(Producto):
    isbn = ""
    autor = ""

    def __str__(self):
        return """
        REFERENCIA \t{}
        NOMBRE \t\t{}
        PVP\t\t{}
        DESCRIPCION\t{}
        ISBN\t\t{}
        AUTOR\t\t{}""".format(self.referencia, self.nombre, self.pvp, self.descripcion,self.isbn,self.autor)    


     

al = Alimento(2035, "Botella de aceite de oliva extra",5,"250 ml")
al.productor = "La aceitera"
al.distribuidor="Distribuidor SA"

li = Libro(2034, "Cocina II",9,"Recetas sans y nuevas")
li.isbn = "0-1234545A"
li.autor="Luis Mena"

ad = Adorno(2034, "Vaso adornado", 15, "Vaso de porcelana adornado con arboles")       

productos = [ad,al,li]
print(productos)



for p in productos:
    if isinstance(p, Adorno):
        print(p.referencia, p.nombre)
    elif isinstance(p,Alimento):
        print(p.referencia, p.nombre, p.productor)
    elif isinstance(p,Libro):
        print(p.referencia, p.nombre, p.isbn)         


def rebajar_producto(p, rebaja):
    """Devuelve un ptoducto con una rebaja en el porcentaje de su precio"""
    p.pvp = p.pvp - (p.pvp/100 * rebaja)
    return p         
    

al_rebajado = rebajar_producto(al,10)
print(al_rebajado)


copia_al = al
copia_al.referencia = 2038
print(copia_al)
print(al)


#Copiar un objeto
copia_ad = copy.copy(ad)
copia_ad.pvp = 25
print(copia_ad)
print(ad)




#Herencia multiple
#Problemas
#cuando tiene comportamientos comunes, le da prioridad mas a la izquierda en la declaracion




class A:
    def __init__(self):
        print("Soy de la clase A")
    def a(self):
        print("Este metodo lo heredo de A")    

class B:
    def __init__(self):
        print("Soy de la clase B")    
    def b(self):
        print("Este metodo lo heredo de B")            


class C(A,B):
    def c(self):
        print("Este metodo es de la clase C")    



c = C()
print(c.a())
print(c.b())
print(c.c())


