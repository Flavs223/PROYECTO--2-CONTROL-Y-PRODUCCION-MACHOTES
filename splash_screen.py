import customtkinter as ctk

class SplashScreen(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("")
        self.geometry("400x250")
        self.resizable(False, False)
        self.overrideredirect(True)  # Quita la barra de título

        # Centrar ventana
        self.eval('tk::PlaceWindow . center')

        # Contenido de la pantalla de carga
        label = ctk.CTkLabel(self, text="Cargando...", font=("Arial", 20))
        label.pack(expand=True)

        # Aquí puedes agregar un logo, barra de progreso, etc.
