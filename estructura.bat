@echo off
mkdir controllers
mkdir models
mkdir views
mkdir config
mkdir utils
mkdir assets
mkdir assets\iconos
mkdir assets\estilo

type nul > main.py

type nul > controllers\machote_controller.py
type nul > controllers\insumo_controller.py
type nul > controllers\inventario_controller.py
type nul > controllers\movimiento_controller.py
type nul > controllers\produccion_controller.py

type nul > models\machote.py
type nul > models\insumo.py
type nul > models\inventario.py
type nul > models\movimiento.py
type nul > models\produccion.py

type nul > views\home_view.py
type nul > views\machote_view.py
type nul > views\insumo_view.py
type nul > views\inventario_view.py
type nul > views\movimiento_view.py
type nul > views\produccion_view.py

type nul > config\database.py

type nul > utils\helpers.py
type nul > utils\exportador_word.py
