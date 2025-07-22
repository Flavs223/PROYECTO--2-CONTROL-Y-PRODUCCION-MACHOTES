#Así creamos nuestros widgets personalizados
#Para la pantalla de inicio o home page
import customtkinter as ctk

def crear_boton_prueba(master, comando):
      return ctk.CTkButton(
            master,
            text="Botón de prueba",
            command=comando,
            fg_color="#E07A5F",  # Color personalizado del botón
            hover_color="#D1603D",  # Color al pasar el mouse
            text_color="white"
      )
