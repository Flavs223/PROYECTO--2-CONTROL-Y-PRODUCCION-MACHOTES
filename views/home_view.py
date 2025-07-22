#Con este archivo creamos la vista principal del sistema
#y mandamos a llamar los widgets que vamos a usar
# y también sus respectivas funciones de control
#de widgets_home.py y home_controller.py
import customtkinter as ctk
#Con esto mandamos a llamar  o importamos los widgets que vamos a usar
#de la vista widgets_home.py
from views.widgets import widgets_home as wh

# Vista principal del sistema
class HomeView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
#Ya aquí solo mando a llamar los componentes creados en widgets_home.py
        # Ejemplo de uso
        btn_prueba = wh.crear_boton_prueba(self, self.controller.boton_prueba_click)
        btn_prueba.pack(pady=20)
