#Así creamos nuestros widgets personalizados
#Para la pantalla de inicio o home page
import customtkinter as ctk

def crear_boton_prueba(parent, comando):
    return ctk.CTkButton(
        parent,
        text="Botón de Prueba",
        command=comando,
        fg_color="#006699",
        corner_radius=10
    )
