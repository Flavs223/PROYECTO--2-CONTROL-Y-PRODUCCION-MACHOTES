#Con este archivo creamos la vista principal del sistema
#y mandamos a llamar los widgets que vamos a usar
# y también sus respectivas funciones de control
#de widgets_home.py y home_controller.py
import customtkinter as ctk
from PIL import Image
import os
#Con esto mandamos a llamar  o importamos los widgets que vamos a usar
#de la vista widgets_home.py
from views.widgets import widgets_home as wh

from utils.rutas import obtener_ruta_imagen #Esta función nos ayuda a obtener la ruta de las imágenes
class HomeView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.configure(fg_color="#F2B28D")  # Fondo durazno claro

        # Imagen
        image_path = os.path.join("assets","imagenes", "modulus_logo.jpeg")
        if not os.path.exists(image_path):
            print(f"❌ Imagen no encontrada en: {image_path}")
        else:
            print(f"✅ Imagen cargada desde: {image_path}")

        
        logo_image = ctk.CTkImage(Image.open(image_path), size=(150, 150))
        logo_label = ctk.CTkLabel(self, image=logo_image, text="")
        logo_label.pack(pady=(30, 10))

        # Eslogan
        eslogan_label = ctk.CTkLabel(self, text="Sistema de Control y Producción",
                                     font=ctk.CTkFont(size=18, weight="bold"))
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