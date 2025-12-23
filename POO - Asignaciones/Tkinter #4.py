import tkinter as tk

def añadir_elemento():
    item = entrada.get()
    if item:
        # Inserta el texto al final de la lista
        lista.insert(tk.END, item)
        # Limpia el cuadro de entrada
        entrada.delete(0, tk.END)

ventana = tk.Tk()
ventana.title("Gestor de Lista")
ventana.geometry("300x400")

# Cuadro de entrada para nuevos elementos
entrada = tk.Entry(ventana)
entrada.pack(pady=10)

# Botón para activar la función
boton = tk.Button(ventana, text="Añadir a la lista", command=añadir_elemento)
boton.pack(pady=5)

# Widget Listbox para mostrar los elementos
lista = tk.Listbox(ventana)
lista.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)


elementos_iniciales = ["Xay", "Lila", "Zab", "Nader"]
for e in elementos_iniciales:
    lista.insert(tk.END, e)

ventana.mainloop()