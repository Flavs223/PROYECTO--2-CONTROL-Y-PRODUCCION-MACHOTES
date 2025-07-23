import os
import ctypes

def get_image_path(filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))  # carpeta utils
    assets_dir = os.path.join(base_dir, '..', 'assets', 'imagenes') # carpeta assets/iconos
    image_path = os.path.join(assets_dir, filename)
    if os.path.isfile(image_path):
        return image_path
    else:
        return None

def registrar_fuentes_personalizadas():
    ruta_fuentes = os.path.abspath("assets/fuentes")
    for archivo in os.listdir(ruta_fuentes):
        if archivo.endswith(".otf"):
            ruta_completa = os.path.join(ruta_fuentes, archivo)
            try:
                FR_PRIVATE = 0x10
                ctypes.windll.gdi32.AddFontResourceExW(ruta_completa, FR_PRIVATE, 0) # Registra la fuente, y permite que se use en la aplicación, también se puede usar AddFontResourceEx para registrar fuentes en Windows
                print(f"Fuente registrada: {archivo}")
            except Exception as e:
                print(f"Error registrando fuente {archivo}: {e}")