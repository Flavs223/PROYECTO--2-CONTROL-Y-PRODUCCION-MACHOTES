import customtkinter as ctk
from views.home_view import HomeView
from controllers.home_controller import HomeController
from utils.helpers import registrar_fuentes_personalizadas
import time

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Control y Producción de Machotes")
        #self.geometry("900x600")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        # Establece la geometría de la ventana para que ocupe toda la pantalla
        # y permite que la ventana sea redimensionable (por defecto es True, pero se puede explicitar)
        self.geometry(f"{screen_width}x{screen_height}")
        self.resizable(True, True) # Permite redimensionar la ventana
        
        self.configure(fg_color="#F2B28D") 
        self.current_view = None
        self.show_home()

    def clear_view(self):
        if self.current_view is not None:
            self.current_view.destroy()

    def show_home(self):
        self.clear_view()
        controlador = HomeController(app=self)
        self.current_view = HomeView(self, controller=controlador)
        self.current_view.pack(fill="both", expand=True)

if __name__ == "__main__":
    
    ctk.set_appearance_mode("System")
    registrar_fuentes_personalizadas()
    #ctk.set_default_color_theme("blue")

    app = App()
    app.mainloop()
