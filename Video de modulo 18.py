import pickle

#clase para crear objetos Soldado
class Soldado:
    # atributos de clase (valores por defecto para los nuevos objetos)
    vuela = False
    velocidad = 3
    # metodo constructor
    def __init__(self, nivel):
        #atributos de instancia(se denen al crear el objeto)
        self.nivel = nivel # nivel de la tropa
        self.vida = nivel * 1000 # cantidad de vida inicial 
        self.fuerza = nivel * 100 # fuerza por golpe al rival
    # metodo que habilita al objeto la capacidad de volar
    def coger_alas(self):
        self.vuela= True
    # metodo que resta daño a la vida del objeto
    def recibe_golpe(self, dano):
        self.vida -= dano


# instanciaciaón de Soldado 1
tropa1 = Soldado(13)
print("Soldado 1")
print(tropa1.nivel)
print(tropa1.vida)
print(tropa1.fuerza)

# instanciaciaón de Soldado 2
print("\nSoldado 2")
tropa2 = Soldado(2)
print(tropa2.nivel)
print(tropa2.vida)
print(tropa2.fuerza)

# instaciación de Soldado 3
print("\nSoldado 3")
tropa3 = Soldado(20)
print(tropa3.vuela)
print("voy a coger alas")
tropa3.coger_alas()
print(tropa3.vuela)

# instanciación de Solado 4
print("\nSoldado 4")
tropa4 = Soldado(100)
print(tropa4.vida)
print("recibe 1 de daño")
tropa4.recibe_golpe(1)
print(tropa4.vida)

objetos = [tropa1, tropa2, tropa3, tropa4]

archivo = open ("tropas.pkl", "wb")
pickle.dump(objetos, archivo)
archivo.close()

with open ("tropa.pkl", "wb") as archivo:
    pickle.dump(objetos, archivo)

print("Fin del programa")