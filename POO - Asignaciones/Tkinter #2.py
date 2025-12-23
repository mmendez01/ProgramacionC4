import tkinter as tk

def mostrar_texto():
    contenido = entrada.get()  # Obtiene el texto del Entry
    etiqueta_resultado.config(text=f"Escrito: {contenido}") # Cambia el texto del Label

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Captura de Datos")
ventana.geometry("300x250")

# Widgets
entrada = tk.Entry(ventana)
entrada.pack(pady=10)

boton = tk.Button(ventana, text="Mostrar Texto", command=mostrar_texto)
boton.pack(pady=10)

etiqueta_resultado = tk.Label(ventana, text="Esperando entrada...")
etiqueta_resultado.pack(pady=10)

ventana.mainloop()