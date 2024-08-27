import sys

# DEVUELVE LA SUMA DE 2 NÚMEROS
def suma(num1, num2):
    return num1 + num2

### MAIN ###
if __name__ == '__main__':
    # si no hay 3 párametros (0: archivo del programa, 1: num1, 2: num2 )
    if len(sys.argv) != 3:
        print("ERROR Parámetros incorrectos")
        print("modo de uso: ")
        print(f'{sys.executable} {sys.argv[0]} número1 número2')
        print("ejemplo: ")
        print(f'{sys.executable} {sys.argv[0]} 4 8')
        sys.exit(1)
    #si hay 3 parametros
    else:
        # guardamos en n1 el primer numero comprobando que sea un entero
        try:
            n1 = int(sys.argv[1])
        except ValueError:
            print ("ERROR El primer parámetro no es un número")
            sys.exit(1)
        # guardamos en n2 el primer numero comprobando que sea un entero
        try:
            n2 = int(sys.argv[2])
        except ValueError:
            print ("ERROR El segundo parámetro no es un número")
            sys.exit(1)
        # mostramos el resultado
        print(f'La suma de {n1} y {n2} es {suma(n1,n2)}')
        sys.exit(0)