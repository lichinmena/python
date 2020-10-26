v = "otro numero"
n = 10
print("un texto",v,"y un numero",n)

c = "Un texto {} y un numero {}".format(v,n)
print(c)


c = "Un texto {0} y un numero {1}".format(v,n)
print(c)



c = "Un texto {texto} y un numero {numero}".format(texto=v,numero=n)
print(c)

print("{:>30}".format("Palabra")) #Alineamiento a la derecha

print("{:30}".format("Palabra")) #Alineamiento a la izquierda

print("{:4d}".format(10))
print("{:4d}".format(100))
print("{:4d}".format(1000))

print("{:04d}".format(10))
print("{:04d}".format(100))
print("{:04d}".format(1000))

print("{:4d}".format(10))
print("{:4d}".format(100))
print("{:4d}".format(1000))

print("{:.2f}".format(3.1415926))


print("{:7.3f}".format(3.1415926))
print("{:7.3f}".format(153.21))



print("{:07.3f}".format(3.1415926))
print("{:07.3f}".format(153.21))