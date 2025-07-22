#Con este archivo creamos la vista principal del sistema
#y mandamos a llamar los widgets que vamos a usar
# y también sus respectivas funciones de control
#de widgets_home.py y home_controller.py
import customtkinter as ctk
from utils.helpers import get_image_path
from PIL import Image
import os
#Con esto mandamos a llamar  o importamos los widgets que vamos a usar
#de la vista widgets_home.py
from views.widgets import widgets_home as wh

#from utils.rutas import obtener_ruta_imagen #Esta función nos ayuda a obtener la ruta de las imágenes
class HomeView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.configure(fg_color="#F2B28D")  # Fondo durazno claro

        # Imagen
        #Encuentra la ruta de la imagen y la guarda en image_path
        image_path = get_image_path("logo.png")
        # Si la imagen existe, la carga y la muestra
        if image_path:
            logo_image = ctk.CTkImage(Image.open(image_path), size=(350, 350))
            label_logo = ctk.CTkLabel(self, image=logo_image, text="")
            label_logo.image = logo_image  # importante mantener la referencia
            label_logo.pack(pady=10)
            print(f"Imagen cargada desde: {image_path}")
        # Si la imagen no existe, muestra un mensaje de error
        else:
            print(f"Imagen no encontrada en: {image_path}")
            
        # Eslogan
        eslogan_label = ctk.CTkLabel(self, 
                                     text="Gestión y producción eficientes",
                                     text_color="black",
                                     font=("Gotham Rounded", 38, "bold"))
        eslogan_label.pack(pady=(0, 30))

        # ===== FILA 1: Botones 1, 2, 3 =====
        fila1 = ctk.CTkFrame(self, fg_color="transparent")
        fila1.pack(pady=5)

        btn1 = ctk.CTkButton(fila1, text="Machotes", width=120)
        btn2 = ctk.CTkButton(fila1, text="Insumos", width=120)
        btn3 = ctk.CTkButton(fila1, text="Inventario", width=120)

        btn1.pack(side="left", padx=10)
        btn2.pack(side="left", padx=10)
        btn3.pack(side="left", padx=10)

        # ===== FILA 2: Botones 4, 5 =====
        fila2 = ctk.CTkFrame(self, fg_color="transparent")
        fila2.pack(pady=10)

        btn4 = ctk.CTkButton(fila2, text="Reportes", width=120)
        btn5 = ctk.CTkButton(fila2, text="Salir", width=120)

        btn4.pack(side="left", padx=20)
        btn5.pack(side="left", padx=20)