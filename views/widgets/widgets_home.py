#Así creamos nuestros widgets personalizados
#Para la pantalla de inicio o home page
import customtkinter as ctk

def crear_boton(parent, texto, comando=None):
      return ctk.CTkButton(
            master=parent,
            text=texto,
            command=comando,
            width=180,
            height=50,
            corner_radius=10,
            fg_color="#099709",
            hover_color="#7FD713",
            text_color="white",
            font=("Gotham Rounded", 18, "bold")
      )

def crear_boton_fila1(parent, texto, comando=None):
      return ctk.CTkButton(
            master=parent,
            text=texto,
            command=comando,
            width=180,
            height=50,
            corner_radius=10,
            fg_color="#E07A5F",
            hover_color="#D1603D",
            text_color="white",
            font=("Gotham Rounded", 18, "bold")
      )

def crear_boton_fila2(parent, texto, comando=None):
      return ctk.CTkButton(
            master=parent,
            text=texto,
            command=comando,
            width=180,
            height=50,
            corner_radius=10,
            fg_color="#CF5534",
            hover_color="#DE8165",
            text_color="white",
            font=("Gotham Rounded", 18, "bold")
      )



def crear_eslogan(parent,texto):
      return ctk.CTkLabel(
            master=parent,
            text=texto,
            text_color="black",
            font=("Gotham Rounded", 28, "bold")
      )
