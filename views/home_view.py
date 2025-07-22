import customtkinter as ctk

class HomeView(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        label = ctk.CTkLabel(self, text="Bienvenido al sistema", font=("Arial", 24))
        label.pack(pady=40)

        # Aquí podrías agregar más botones o navegación
