import os

def get_image_path(filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))  # carpeta utils
    assets_dir = os.path.join(base_dir, '..', 'assets', 'imagenes') # carpeta assets/iconos
    image_path = os.path.join(assets_dir, filename)
    if os.path.isfile(image_path):
        return image_path
    else:
        return None