import os 
from PIL import Image


rutaActual = os.path.dirname(os.path.abspath(__file__))

def formatRuta(ruta):
    clean = ""

    for caracter in ruta:
        if caracter in ruta: 
            if caracter == '\\':
                clean = clean + '/'

            else:
                clean = clean + caracter
            
    return clean

descargasFolder = formatRuta(rutaActual) + '/'

organized_files = descargasFolder + '/ArchivosOrganizados'
organized_filesImagenes = descargasFolder + '/ArchivosOrganizados/ImagenesDescargadas'
organized_filesAudios = descargasFolder + '/ArchivosOrganizados/AudiosDescargadas'
organized_filesVideos = descargasFolder + '/ArchivosOrganizados/VideosDescargadas'
organized_filesPoint = descargasFolder + '/ArchivosOrganizados/PowerPointDescargadas'
organized_filesExe = descargasFolder + '/ArchivosOrganizados/ExeDescargadas'
organized_filesRar = descargasFolder + '/ArchivosOrganizados/RARDescargadas'
organized_filesWord = descargasFolder + '/ArchivosOrganizados/WordDescargadas'
organized_filesTxt = descargasFolder + '/ArchivosOrganizados/ArchivosTxt'
organized_filesPdf = descargasFolder + '/ArchivosOrganizados/PDFDescargados'



os.mkdir(organized_files)
os.mkdir(organized_filesImagenes)
os.mkdir(organized_filesAudios)
os.mkdir(organized_filesVideos)
os.mkdir(organized_filesPoint)
os.mkdir(organized_filesExe)
os.mkdir(organized_filesRar)
os.mkdir(organized_filesWord) 
os.mkdir(organized_filesTxt)
os.mkdir(organized_filesPdf)

if __name__ == "__main__":
    for filename in os.listdir(descargasFolder):
        name, extension = os.path.splitext(descargasFolder + filename)

        if extension in [".jpg", ".jpeg", ".png", ".gif"]:
            picture = Image.open(descargasFolder + filename)
            picture.save(organized_filesImagenes + '/' + "compressed_" + filename, optimized = True, quality = 60 )
            os.remove(descargasFolder + filename)
            print(name + ":" + extension)

        if extension in [".mp3", ".flac"]:
            os.rename(descargasFolder + filename, organized_filesAudios + "/" + filename)

        if extension in [".mp4", ".mov"]:    
            os.rename(descargasFolder + filename, organized_filesVideos + "/" + filename)

        if extension in [".pptx"]:
            os.rename(descargasFolder + filename, organized_filesPoint + "/" + filename)

        if extension in [".exe"]:
            os.rename(descargasFolder + filename, organized_filesExe + "/" + filename)
            
        if extension in [".rar", ".zip"]:    
            os.rename(descargasFolder + filename, organized_filesRar + "/" + filename)
            
        if extension in [".doc"]:    
            os.rename(descargasFolder + filename, organized_filesWord + "/" + filename)

        if extension in [".txt"]:    
            os.rename(descargasFolder + filename, organized_filesTxt + "/" + filename)
            
        if extension in [".pdf"]:    
            os.rename(descargasFolder + filename, organized_filesPdf + "/" + filename)


