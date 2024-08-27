import urllib.request
import os.path

# DEVUELVE EL CODIGO HTML DE UNA URL 
def get_file(url):
    req = urllib.request.urlopen(url)
    html = req.read()
    return html

#### MAIN ####
if __name__ == '__main__':
    #varianle con la url a la que queremos acceder
    url = "https://www.res.com.ar/media/catalog/product/cache/6c63de560a15562fe08de38c3c766637/c/h/churrasquito_2.jpg"
    # abrimos un archivo en modo escritura
    f = open(os.path.basename(url), "wb")
    #guardamos el contenido HTML de la página
    f.write(get_file(url))
    # cerramos el archivo
    f.close()
    #informamos que el proceso ha finalizado
    print("Fin del programa")