# home_controller.py

def saludar_usuario():
    return "¡Hola! Bienvenido al sistema de control y producción de machotes."

def obtener_estado_sistema():
    # Aquí podrías más adelante leer de la BD o revisar condiciones
    return "Sistema funcionando correctamente."

def cambiar_apariencia(app, modo):
    """
    Cambia el modo de apariencia del sistema: "Dark" o "Light"
    """
    if modo.lower() == "dark":
        app.set_appearance_mode("dark")
    elif modo.lower() == "light":
        app.set_appearance_mode("light")
    else:
        print("⚠️ Modo no reconocido: Usa 'dark' o 'light'")

def abrir_machotes():
    print("Abriendo machotes...")  # Aquí pondrás la lógica real más adelante

def abrir_insumos():
    print("Abriendo módulo de insumos...")  # Aquí pondrás la lógica real después

def abrir_inventario():
    print("Abriendo inventario...")

def abrir_reportes():
    print("Función abrir_reportes llamada")
    # Aquí iría la lógica para mostrar la vista de reportes o la acción correspondiente.
