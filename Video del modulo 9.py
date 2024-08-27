def limpiar_pantalla():
    print("\33[2J\33[H")

def sumar(num1, num2):
    print("num1 en la función = ", num1 )
    return num1 + num2

# Variable global
num1 = 10
resultado = sumar(3, 2)
print (resultado)
print("num1 en el programa", num1)