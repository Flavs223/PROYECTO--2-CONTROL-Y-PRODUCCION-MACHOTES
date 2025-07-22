import customtkinter as ctk
#Con esto mandamos a llamar  o importamos los widgets que vamos a usar
#de la vista widgets_home.py
#from views.widgets.widgets_home import crear_boton_reportes
from controllers.home_controller import (
      #Portamos las funciones del controlador
      #Es importante que las funciones estén en el controlador
      #para mantener la separación de responsabilidades     
      #saludar_usuario,
      abrir_machotes,
      abrir_insumos,
      abrir_inventario,
      abrir_reportes
)

# Vista principal del sistema
class HomeView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)

        label = ctk.CTkLabel(self, text="Bienvenido a Modulus", font=("Arial", 24))
        label.pack(pady=40)

        btn_machotes = ctk.CTkButton(self, text="Machotes", command=abrir_machotes)
        btn_machotes.pack(pady=10)

        btn_insumos = ctk.CTkButton(self, text="Insumos", command=abrir_insumos)
        btn_insumos.pack(pady=10)

        btn_inventario = ctk.CTkButton(self, text="Inventario", command=abrir_inventario)
        btn_inventario.pack(pady=10)
        
        btn_reportes = ctk.CTkButton(self, text="Reportes", command=abrir_reportes)
        btn_reportes.pack(pady=10)
