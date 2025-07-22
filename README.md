# Sistema de Control de Inventario y Producción
Aplicación que permita un mejor control de inventario de productos y de insumos que se requieren para fabricarlos; también realizará reportes mensuales y contiene Bases de datos.

# Estructura del Proyecto

# `main.py`
Punto de entrada principal de la aplicación. Desde aquí se inicializa la interfaz gráfica y se gestiona el flujo principal.

# `controllers/`
Contiene los controladores que manejan la lógica entre las vistas y los modelos. Actúan como intermediarios.

- `machote_controller.py` – Lógica para los machotes de producción.
- `insumo_controller.py` – Lógica para el CRUD de insumos.
- `inventario_controller.py` – Lógica para manejo de inventario.
- `movimiento_controller.py` – Manejo de entradas y salidas de inventario.
- `produccion_controller.py` – Gestión de procesos de producción.


# `models/`
Define las clases y estructuras de datos que representan la base de datos.

- `machote.py` – Modelo del machote (plantilla de producción).
- `insumo.py` – Modelo de insumo.
- `inventario.py` – Modelo del estado del inventario.
- `movimiento.py` – Modelo para los movimientos (entradas/salidas).
- `produccion.py` – Modelo de cada proceso de producción.

---

# `views/`
Aquí se definen las interfaces gráficas (pantallas) del sistema.

- `home_view.py` – Pantalla principal.
- `machote_view.py` – Interfaz para gestionar machotes.
- `insumo_view.py` – Interfaz de insumos.
- `inventario_view.py` – Interfaz del inventario.
- `movimiento_view.py` – Interfaz para registrar movimientos.
- `produccion_view.py` – Interfaz para controlar la producción.



#  `config/`
Archivos de configuración del sistema.

- `database.py` – Configuración de conexión a la base de datos (SQLite u otra).


# `utils/`
Funciones auxiliares o herramientas reutilizables.

- `helpers.py` – Funciones generales de utilidad.
- `exportador_word.py` – Funcionalidad para exportar documentos Word (por ejemplo, reportes o formatos de producción).



# `assets/`
Archivos estáticos y recursos visuales de la aplicación.

- `iconos/` – Íconos utilizados en la interfaz.
- `estilo/` – Archivos relacionados con estilos visuales, como temas o colores.



# Requisitos

- Python 3.10+
- Paquetes recomendados:
  - `customtkinter`
  - `python-docx`
  - `sqlite3` (incluido en Python estándar)

Puedes instalar los requisitos con:

```bash
pip install -r requirements.txt
