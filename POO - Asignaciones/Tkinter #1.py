import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi Programa")
ventana.geometry("300x200")

etiqueta = tk.Label(ventana, text="¡Bienvenido Profesor Carlos!")
etiqueta.pack()

ventana.mainloop()