import urllib.request

# DEVUELVE EL CODIGO HTML DE UNA URL 
def get_html(url):
    req = urllib.request.urlopen(url)
    html = req.read().decode('utf-8')
    return html

#### MAIN ####
if __name__ == '__main__':
    #varianle con la url a la que queremos acceder
    url = "https://campus-escuelademaestros.buenosaires.gob.ar/mod/quiz/review.php?attempt=50797&cmid=22014"
    # abrimos un archivo en modo escritura
    f = open("pagina.html", "w" ,encoding="utf-8")

    #guardamos el contenido HTML de la página
    f.write(get_html(url))
    # cerramos el archivo
    f.close()
    #informamos que el proceso ha finalizado
    print("Fin del programa")