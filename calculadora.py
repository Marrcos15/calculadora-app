
import tkinter as tk
import os

# Configuración de ventana
ventana = tk.Tk()
ventana.title("Mi calculadora")
ruta_icono = os.path.join(os.path.dirname(__file__), 'sources', 'calculadora.ico')
ventana.iconbitmap(ruta_icono)

# Variables para almacenar la exp matematica
expresion = ''

# Variable para almacenar el estado del visor (mostrar resultado [True] o la expresion[False])
resultado_mostrado = False

# Funcion para actualizar la expresion en el cuadro de texto
def pulsar_tecla(tecla):
    global expresion, resultado_mostrado
    
    # Revisamos si se ha calculado el resultado
    if resultado_mostrado:
        # Verificamos si es un número para resetear la pantalla
        if tecla.isdigit() or tecla == '.':
            expresion = str(tecla)
        else:
            expresion += str(tecla)
            
        resultado_mostrado = False
    
    else:
        expresion += str(tecla)
    
    visor_texto.set(expresion)
    
# Funcion para borrar el texto
def limpiar():
    global expresion, resultado_mostrado
    
    expresion = ''
    resultado_mostrado = False
    visor_texto.set(expresion)

# Funcion para calcular el resultado y mostrarlo
def calcular():
    global expresion, resultado_mostrado
    
    try:
        resultado = eval(expresion)
        # Verificar si es un numero entero para no mostrar decimales
        if resultado == int(resultado):
            resultado = int(resultado)
        
        visor_texto.set(str(resultado))
        expresion = str(resultado)
        resultado_mostrado = True
    except Exception as e:
        visor_texto.set('ERROR')
        expresion = ''
        resultado_mostrado = False
        

# Crear grid (5 filas y 4 columnas)
for i in range(5):
    ventana.grid_rowconfigure(i, weight=1)

for i in range(4):
    ventana.grid_columnconfigure(i, weight=1)

# Visor de texto para mostrar las expresiones y resultado
visor_texto = tk.StringVar()
visor = tk.Entry(ventana,
                 textvariable=visor_texto,
                 font=('Helvetica', 32, 'bold'),
                 bd=10,
                 insertwidth=4,
                 width=14,
                 borderwidth=2,
                 justify='right',
                 relief="sunken",
                 bg='#e8f0f2',
                 fg="#333333")

visor.grid(row=0,
           column=0,
           columnspan=4,
           sticky="ew",
           padx=10,
           pady=10,
           )

#Configurar botones
botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
]

# Paleta de colores para los botones
color_fondo_numero = '#b3cde0'
color_fondo_operacion = '#7A869A'
color_fondo_especial = '#9B90B6'
color_fondo_calcular = '#b0e57c'
color_fondo_presionado = '#6a51a3'
color_fondo_calcular_presionado = '#76c7c0'
color_texto_numero = '#333333'
color_texto_especial = '#ffffff'


#Crear y posicionar botones (excepto "=")
for (texto, fila, columna) in botones:
    
    if texto in ['/', '*', '-', '+']:
        comando = lambda x=texto: pulsar_tecla(x)
        color_fondo = color_fondo_operacion
        color_texto = color_texto_especial
    elif texto == 'C':
        comando = limpiar
        color_fondo = color_fondo_especial
        color_texto = color_texto_especial
    elif texto == '.':
        comando = lambda x=texto: pulsar_tecla(x)
        color_fondo = color_fondo_especial
        color_texto = color_texto_especial
    else:
        comando = lambda x=texto: pulsar_tecla(x)
        color_fondo = color_fondo_numero
        color_texto = color_texto_numero
        
    tk.Button(ventana,
              text=texto,
              padx=20,
              pady=20,
              font=('Helvetica', 20, 'bold'),
              command=comando,
              bd=1,
              relief='raised',
              bg=color_fondo,
              fg=color_texto,
              activeforeground=color_texto_especial,
              activebackground=color_fondo_presionado,
              ).grid(row=fila, 
                     column=columna, 
                     sticky='nsew',
                     padx=2,
                     pady=2)

# Boton '='
tk.Button(ventana,
          text='=',
          padx=20,
          pady=20,
          font=('Helvetica', 40),
          command=calcular,
          bd=1,
          relief='raised',
          bg=color_fondo_calcular,
          fg=color_texto_numero,
          activeforeground=color_texto_especial,
          activebackground=color_fondo_calcular_presionado,
          ).grid(row=5, 
                column=0,
                columnspan=4, 
                sticky='ew',
                padx=2,
                pady=2)

# Iniciar app
ventana.mainloop()