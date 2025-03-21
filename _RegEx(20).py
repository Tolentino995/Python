import re

text = "La lluvia en Sevilla es una maravilla y la cama de España es la caña"

x = re.search(r'c..a', text);

print (x.group());

print (type(x));

print (dir(x));

#Nos devuelve el texto que comiencen con "C" y finalicé con "A"
    
y = re.findall(r'c..a', text)

print (type(y));

print(','.join(y));

#Nos devuelve el texto2 con todos los caracteres seleccionados entre []

z = re.findall(r'ca[mñ]a', text)

print(','.join(z));

#Nos devuelve el texto2 con todos los caracteres entre [] pero que no tengan ñ ya que ^ nos sirve para negar

a = re.findall(r'ca[^ñ]a', text);

print(','.join(a));

text2 = """Tengo 2 COCHE: el 1° aunque EXTRAÑE
            costo 12432  $ y el 2° 32433 $ y viva Perú"""

#Nos devuelve el texto2 con todos los caracteres seleccionados entre []

m = re.findall(r'[a-z]', text2)

print(','.join(m));

#Nos devuelve el texto2 con todos los caracteres seleccionados entre []

n = re.findall(r'[a-zñ]+', text2);

print(','.join(n));

#Nos devuelve el texto2 con todos los caracteres seleccionados entre []

i = re.findall(r'[a-zñÑA-Z]+', text2);

print(','.join(i));

#Nos devuelve los numeros del 1 al 9 del texto2

q= re.findall(r'\d+', text2);

print(','.join(q));

#Nos devuelve los numeros del 1 al 9 del texto2

w = re.findall(r'[0-9]+', text2);

print(','.join(w));

#Nos devuelve todo menos los numeros del 1 al 9 del texto2

r = re.findall(r'\D+', text2);

print(','.join(r));

#Nos devuelve todo lo que encuentre y forme una palabra texto2

s = re.findall(r'\w+', text2);

print(','.join(s));

#Nos devuelve todos los caracteres y signos texto2

f = re.findall(r'\W+', text2);

print(','.join(f));

#Nos devuelve todos los espacios y Saltos de linea del texto2

g = re.findall(r'\s+', text2);

print(','.join(g));

#Nos devuelve todos monos los espacios y Saltos de linea del texto2

ñ = re.findall(r'\S+', text2);

print(','.join(ñ));

#Otro forma de cuantificadores es con el * y ?

text3 = """111
            inglés: colour
            español: color
            cantando: colouuuuur 
            2222"""

#1 o mas veces

b = re.findall(r'colou+r', text3);

print(','.join(b));

#0 o mas veces

c = re.findall(r'colou*r', text3);

print(','.join(c));

#0 o uno

e = re.findall(r'colou?r', text3);

print(','.join(e));

#En otro caso podemos solicitar cuantas veces queremos que se repita colocando un número dentro {}

d = re.findall(r'colou{3}r', text3);

print(','.join(d));

#El \b significa que solo las palabres que terminen en doble rr por eso no nos va devolver nada

h = re.findall(r'colou{1,5}rr\b', text3);

print(','.join(h));

# En este ejemplo el ^ esta funcionando como una condicion de 
# que si el principio de la String no comenza con 1 no nos devolveria nada

a = re.findall(r'^1\d+', text3);

print(','.join(a));

#ATENCIÓN si utilizamos flags=re.MULTILINE si nos permitiria
#devolver con cualquier carter sin depender que este al comienzo
#!!IMPORTANTE¡¡¡ si cuenta con saltos de linea tienen que contar con el siguiente comando
# --> text3_normalizado = "\n".join(line.lstrip() for line in text3.splitlines())

text3_normalizado = "\n".join(line.lstrip() for line in text3.splitlines())

z = re.findall(r'^2\d+', text3_normalizado, flags=re.MULTILINE)
print(','.join(z))  # Debería imprimir "2222"


text4 = """
            Suscríbete
            SuScRíBeTe
            SUSCRÍBETE
            suscríBETE
        """

#ATENCIÓN si utilizamos flags=re.IGNORECASE si nos permitiria
#devolver con cualquier carter sin importar si es mayuscula o minuscula el String

#!!IMPORTANTE¡¡¡ si cuenta con saltos de linea tienen que contar con el siguiente comando
# --> text4_normalizado = "\n".join(line.lstrip() for line in text4.splitlines())

text4_normalizado = "\n".join(line.lstrip() for line in text4.splitlines())

y = re.findall(r'Suscríbete', text4_normalizado, flags=re.IGNORECASE)

print(','.join(y))


#En este ultimo caso vamos aplicar varios de los conceptos utilizados
#\S QUE NOS TRAE TODO MENOS LOS ESPACIOS Y LOS CARACTERES
#+ QUE NOS LOS TRAE UNA Y MAS VECES
#$ QUE NOS TRAE SOLO LAS QUE TERMINAN LA PALABRA LAS LETRAS QUE SE LE ASIGNA ATRAS


text5 = """Tengo 2 COCHE: el 1° aunque EXTRAÑA
            costo 12432  $ y esta en España
            el 2° 32433 $ y el otro en Perú"""

text5_normalizado = "\n".join(line.lstrip() for line in text5.splitlines())

o = re.findall(r'\S+ña$', text5_normalizado, flags=re.MULTILINE | re.IGNORECASE)

print(','.join(o))

#-----------ESTO SON TODAS LAS HERRAMIENTAS PARA REGEX FLAGS------------------------
#https?:[a-zA-Z0-9?&%:,=+./_-]+ <- UN TIP