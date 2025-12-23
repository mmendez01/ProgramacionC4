import tkinter as tk

def iniciar_dibujo(event):
    global x_ant, y_ant
    x_ant, y_ant = event.x, event.y

def dibujar(event):
    global x_ant, y_ant
    # Dibuja una línea desde la posición anterior a la actual
    canvas.create_line(x_ant, y_ant, event.x, event.y, width=2, fill="blue", capstyle=tk.ROUND, smooth=True)
    x_ant, y_ant = event.x, event.y

ventana = tk.Tk()
ventana.title("Pizarra de Dibujo INFOTEP")

canvas = tk.Canvas(ventana, bg="white", width=400, height=400)
canvas.pack(pady=20, padx=20)

# Eventos del mouse
canvas.bind("<Button-1>", iniciar_dibujo) 
canvas.bind("<B1-Motion>", dibujar)       

ventana.mainloop()