import os

def obtener_ruta_imagen(nombre_archivo, subcarpeta="imagenes"):
    return os.path.join("assets", subcarpeta, nombre_archivo)
