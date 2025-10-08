# Calculadora Tkinter

Esta es una calculadora sencilla desarrollada en Python utilizando la biblioteca Tkinter para la interfaz gráfica.

## Características

- Suma, resta, multiplicación y división
- Interfaz gráfica amigable
- Empaquetada como ejecutable con PyInstaller

## Requisitos

- Python 3.12 o superior
- Tkinter (incluido en la instalación estándar de Python)

## Instalación

1. Clona el repositorio:
   ```
   git clone https://github.com/
   ```
2. Instala las dependencias (si es necesario):
   ```
   pip install -r requirements.txt
   ```

## Uso

Ejecuta el archivo principal:
```
python calculadora.py
```

Para generar el ejecutable:
```
python -m PyInstaller --onefile --windowed --icon=sources/calculadora.ico --add-data "sources/calculadora.ico;sources" calculadora.py
```

## Autor

Marcos González Montesinos

## Licencia

Este proyecto está bajo la licencia MIT.