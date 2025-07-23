#Con este archivo creamos la vista principal del sistema
#y mandamos a llamar los widgets que vamos a usar
# y también sus respectivas funciones de control
#de widgets_home.py y home_controller.py
import customtkinter as ctk
from PIL import Image
from utils.helpers import get_image_path
from views.widgets import widgets_home as wh #Con esto mandamos a llamar  o importamos los widgets que vamos a usar de la vista widgets_home.py
import os

#from utils.rutas import obtener_ruta_imagen #Esta función nos ayuda a obtener la ruta de las imágenes
class HomeView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.configure(fg_color="#F2AD94")  # Fondo durazno claro
        self.pack(fill="both", expand=True)
        
        #Logo y bienvenida
        #Encuentra la ruta de la imagen y la guarda en image_path
        image_path = get_image_path("logo.png")
        # Si la imagen existe, la carga y la muestra
        if image_path:
            logo_image = ctk.CTkImage(Image.open(image_path), size=(350, 280))
            label_logo = ctk.CTkLabel(self, image=logo_image, text="")
            label_logo.image = logo_image  # Mantener referencia
            #el pady es (espacio arriba, espacio abajo)
            label_logo.pack(pady=(60, 1))
        else:
            ctk.CTkLabel(self, text="[Logo no encontrado]").pack(pady=10)
            print(f"Imagen no encontrada en: {image_path}")
        
        
        #Creación de eslogan
        eslogan = wh.crear_eslogan(self, "Gestiona y controla tus producciones de manera eficiente")
        eslogan.pack(pady=(30, 30))
        
        # ===== FILA 1 de otones 1, 2, 3 =====
        # Aquí creamos los botones de la primera fila
        # y los empaquetamos en un frame para que se vean bien  
        fila1 = ctk.CTkFrame(self, fg_color="transparent")
        fila1.pack(pady=10)

        btn1 = wh.crear_boton_fila1(fila1,"Machotes", lambda: print("Machotes"))
        btn2 = wh.crear_boton_fila1(fila1,"Insumos", lambda: print("Insumos"))
        btn3 = wh.crear_boton_fila1(fila1,"Inventario", lambda: print("Inventario"))

        btn1.pack(side="left", padx=15)
        btn2.pack(side="left", padx=15)
        btn3.pack(side="left", padx=15)

        # ===== FILA 2 de botones 4, 5 =====
        fila2 = ctk.CTkFrame(self, fg_color="transparent")
        fila2.pack(pady=10)

        btn4 = wh.crear_boton_fila2(fila2,"Reportes", lambda: print("Reportes"))
        btn5 = wh.crear_boton_fila2(fila2,"Salir", lambda: self.controller.app.quit())

        # Centrado manual en fila 2
        btn4.pack(side="left", padx=30)
        btn5.pack(side="left", padx=30)