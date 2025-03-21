 # TRAEMOS ESTA FUNCION PARA USAR HILOS
import threading
# ESTA PARTE SIN HILOS
from datetime import datetime
import time

#COLORES
verde = "\33[1;32m" 
amarillo = "\33[1;33m"
azul = "\33[1;36m"
magenta = "\33[1;35m"   
gris = "\33[0;37m" 
blanco = "\33[1;37m" 
rojo = "\33[1;31m"

#IMPRIME LA HORA DEL COLO INDICADO 100 VECES

def mostrar_hora(color):
    id_hilo = threading.current_thread().ident
    nombre_hilo = threading.current_thread().name
    for n in range(100):
        n_hilos = threading.active_count()
        hora = datetime.now().strftime("%H:%M:%S.%f")
        print(f'{color}#{n}: {hora} {id_hilo} {nombre_hilo} {n_hilos} {gris}')
        time.sleep(0.01)

#### MAIN ####

if __name__ == '__main__' :
    id_main = threading.main_thread().ident
    nombre_main = threading.main_thread().name
    n_hilos = threading.active_count()
    print("ID main: ", id_main)
    print("Nombre: ", nombre_main)
    print("Hilo..  ", n_hilos)
    input("Pulsar ENTER para empezar")
    #GUARDAMOS LA HORA DE INICIO
    inicio = datetime.now()
        # SIN USAR HILOS
    # mostrar_hora(verde)
    # mostrar_hora(amarillo)
    # mostrar_hora(azul)
    # mostrar_hora(magenta)
    # mostrar_hora(gris)
    # mostrar_hora(blanco)
    # mostrar_hora(rojo)
    h1 = threading.Thread(name="Hilo1", target=mostrar_hora, args=(verde,))
    h2 = threading.Thread(name="Hilo2", target=mostrar_hora, args=(amarillo,))
    h3 = threading.Thread(name="Hilo3", target=mostrar_hora, args=(azul,))
    h4 = threading.Thread(name="Hilo4", target=mostrar_hora, args=(magenta,))
    h5 = threading.Thread(name="Hilo5", target=mostrar_hora, args=(gris,))
    h6 = threading.Thread(name="Hilo6", target=mostrar_hora, args=(blanco,))
    h7 = threading.Thread(name="Hilo7", target=mostrar_hora, args=(rojo,))

    #PARA LLAMAR A LOS HILOS
    h1.start()
    h2.start()
    h3.start()
    h4.start()
    h5.start()
    h6.start()
    h7.start()

    #ES NECESARIO CERRAR LOS HILOS
    h1.join()
    h2.join()
    h3.join()
    h4.join()
    h5.join()
    h6.join()
    h7.join()

#MOSTRAMOS LOS SEGUNDOS QUE A TARDADO

print()
print("Hilo..  ", n_hilos)
print(f'Finalizando en {(datetime.now() - inicio).total_seconds()} segundos')