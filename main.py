import customtkinter as ctk
from views.home_view import HomeView

# Configuración global de la apariencia
ctk.set_appearance_mode("System")  # Opciones: "Dark", "Light", "System"
ctk.set_default_color_theme("blue")  # Puedes usar: "blue", "green", "dark-blue"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.title("Sistema de Control de Inventario y Producción")
        self.geometry("1000x600")
        self.resizable(False, False)

        # Inicializar vista principal
        self.current_view = None
        self.show_home()

    def show_home(self):
        # Cierra vista actual si existe
        if self.current_view:
            self.current_view.destroy()
        self.current_view = HomeView(self)
        self.current_view.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = App()
    app.mainloop()
