import tkinter as tk

def sumar():
    try:
        n1 = float(entrada1.get())
        n2 = float(entrada2.get())
        resultado = n1 + n2
        etiqueta_res.config(text=f"Resultado: {resultado}")
    except ValueError:
        etiqueta_res.config(text="Error: Ingresa números")

ventana = tk.Tk()
ventana.title("Calculadora Suma")
ventana.geometry("300x250")

tk.Label(ventana, text="Número 1:").pack()
entrada1 = tk.Entry(ventana)
entrada1.pack()

tk.Label(ventana, text="Número 2:").pack()
entrada2 = tk.Entry(ventana)
entrada2.pack()

boton = tk.Button(ventana, text="Calcular Suma", command=sumar)
boton.pack(pady=10)

etiqueta_res = tk.Label(ventana, text="Resultado: 0")
etiqueta_res.pack()

ventana.mainloop()