import time, datetime

print(time.time(),"\n")

print(time.localtime(),"\n")

print(time.strftime("%d/%m/%Y %H:%M:%S", time.localtime()),"\n")

for n in range(5):
    print(n)
    time.sleep(1)

inicio = datetime.datetime.now()
print(type(inicio))

# solicitamos una fecha en formato DD-MM-AAAA
fecha = input ("Introduce tu fecha de nacimiento (dia-mes-año): ")

# convertimos la fecha string en formato datetime
fecha_dt = datetime.datetime.strptime(fecha, "%d-%m-%Y")

# tupla con los nombres de los días  de la semana 
dias = ("lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo")

# obtenemos el indice del día de la semana de la fecha
indice = datetime.date.weekday(fecha_dt)
print (indice)

# mostramos el día de la semana que corresponde a la fecha indicada
print(f"Has nacido un {dias[indice]}")
