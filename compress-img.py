import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os
import sys
from tkinter import ttk

def seleccionar_archivos():
    # Crea una ventana de diálogo para seleccionar múltiples archivos
    root = tk.Tk()
    root.withdraw()
    archivos = filedialog.askopenfilenames(filetypes=[("Archivos de imagen", "*.png;*.jpg")])
    return archivos

def comprimir_imagenes(archivos, calidad):
    try:
        for archivo in archivos:
            # Abrir la imagen
            imagen = Image.open(archivo)

            # Convertir a modo RGB (si no lo está)
            if imagen.mode != "RGB":
                imagen = imagen.convert("RGB")

            # Guardar la imagen en formato JPEG con la calidad especificada
            ruta_guardar = os.path.dirname(archivo)
            nombre_archivo = os.path.basename(archivo)
            nombre_comprimido = os.path.splitext(nombre_archivo)[0] + "_compressed.jpg"
            ruta_completa = os.path.join(ruta_guardar, nombre_comprimido)
            imagen.save(ruta_completa, optimize=True, quality=calidad)

        messagebox.showinfo("Proceso exitoso", "Imágenes comprimidas y guardadas con éxito.")

    except Exception as e:
        messagebox.showerror("Error", f"Error al comprimir las imágenes: {str(e)}")

    finally:
        # Desactivar el botón "Procesar" y activar los botones "Seleccionar otro archivo" y "Cerrar"
        boton_procesar.config(state=tk.DISABLED)
        boton_seleccionar.config(state=tk.NORMAL)
        boton_cerrar.config(state=tk.NORMAL)

def obtener_calidad():
    calidad = calidad_entry.get()
    if calidad.isdigit() and 0 <= int(calidad) <= 100:
        comprimir_imagenes(archivos_seleccionados, int(calidad))
    else:
        messagebox.showerror("Error", "La calidad de compresión debe ser un número entero entre 0 y 100.")

def seleccionar_otros_archivos():
    global archivos_seleccionados
    archivos_seleccionados = seleccionar_archivos()
    if archivos_seleccionados:
        boton_procesar.config(state=tk.NORMAL)
        boton_seleccionar.config(state=tk.DISABLED)
        boton_cerrar.config(state=tk.DISABLED)

def cerrar_programa():
    ventana_principal.destroy()
    sys.exit()

# Crear la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Compresor de imágenes")

# Estilo personalizado para los botones
estilo = ttk.Style()
estilo.configure("TButton", foreground="black", background="white")

# Botón para seleccionar los archivos
boton_seleccionar = ttk.Button(ventana_principal, text="Seleccionar archivos", command=seleccionar_otros_archivos, style="TButton")
boton_seleccionar.pack()

# Entrada para ingresar la calidad de compresión
calidad_label = ttk.Label(ventana_principal, text="Calidad de compresión (0-100):")
calidad_label.pack()
calidad_entry = ttk.Entry(ventana_principal)
calidad_entry.pack()

# Botón para procesar los archivos seleccionados
boton_procesar = ttk.Button(ventana_principal, text="Procesar", command=obtener_calidad, state=tk.DISABLED, style="TButton")
boton_procesar.pack()

# Botón para cerrar el programa
boton_cerrar = ttk.Button(ventana_principal, text="Cerrar", command=cerrar_programa, state=tk.DISABLED, style="TButton")
boton_cerrar.pack()

# Seleccionar los archivos de imagen inicialmente
archivos_seleccionados = seleccionar_archivos()

if archivos_seleccionados:
    boton_procesar.config(state=tk.NORMAL)
    boton_seleccionar.config(state=tk.DISABLED)

ventana_principal.mainloop()
