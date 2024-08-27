from _Funciones import sumar, limpiar_pantalla
from _Funciones import A,B
#  funciones del paquete Mi_libreria
from Mi_libreria.operaciones import restar
# manera de importar sb paquetes
from Mi_libreria.Vario.prueba import chiste


# de mi paquete
resultado2 = restar(20,16)
print(resultado2)

# de mi sub-paquete
chiste()

# una manera de importar una funcion
print(A)
print(B)
resultado = sumar(40,50)
print(resultado)

input("ntroduci algo: ")
limpiar_pantalla()
