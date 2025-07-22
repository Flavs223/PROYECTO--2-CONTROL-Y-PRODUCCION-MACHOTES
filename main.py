import customtkinter as ctk
from views.home_view import HomeView


# Si más vistas necesitan cargarse dinámicamente:
# from views.machote_view import MachoteView
# from views.insumo_view import InsumoView
# etc.

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sistema de Control y Producción de Machotes")
        self.geometry("900x600")
        self.resizable(False, False)

        self.current_view = None
        self.show_home()  # Muestra la pantalla de inicio

    def clear_view(self):
        if self.current_view is not None:
            self.current_view.destroy()

    def show_home(self):
        self.clear_view()
        self.current_view = HomeView(self, controller=self)
        self.current_view.pack(fill="both", expand=True)

    # Puedes definir más métodos para cambiar de vista desde los botones
    # por ejemplo:
    # def show_machote(self):
    #     self.clear_view()
    #     self.current_view = MachoteView(self, controller=self)
    #     self.current_view.pack(fill="both", expand=True)

if __name__ == "__main__":
    ctk.set_appearance_mode("System")  # Opcional: "dark" o "light"
    ctk.set_default_color_theme("blue")
    app = App()
    app.mainloop()
