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
            fg_color="#ad94f2",
            hover_color="#7651ec",
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
            fg_color="#94d9f2",
            hover_color="#94baf2",
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
