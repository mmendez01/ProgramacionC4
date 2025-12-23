import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from connector import Database

class AppArticulos:
    def __init__(self, root):
        self.root = root
        self.root.title("Mantenimiento de artículos")
        self.db = Database()

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(padx=10, pady=10, expand=True, fill="both")

        self.tab_carga = ttk.Frame(self.notebook)
        self.tab_consulta = ttk.Frame(self.notebook)
        self.tab_listado = ttk.Frame(self.notebook)

        self.notebook.add(self.tab_carga, text="Carga de artículos")
        self.notebook.add(self.tab_consulta, text="Consulta por código")
        self.notebook.add(self.tab_listado, text="Listado completo")

        self.setup_tab_carga()
        self.setup_tab_consulta()
        self.setup_tab_listado()

    def setup_tab_carga(self):
        frame = tk.LabelFrame(self.tab_carga, text="Artículo", fg="blue", padx=20, pady=20)
        frame.pack(padx=20, pady=20)

        # NUEVO: Campo para el código en la carga
        tk.Label(frame, text="Código:").grid(row=0, column=0, sticky="e")
        self.cod_carga = tk.Entry(frame)
        self.cod_carga.grid(row=0, column=1, pady=5)

        tk.Label(frame, text="Descripción:").grid(row=1, column=0, sticky="e")
        self.desc_carga = tk.Entry(frame)
        self.desc_carga.grid(row=1, column=1, pady=5)

        tk.Label(frame, text="Precio:").grid(row=2, column=0, sticky="e")
        self.precio_carga = tk.Entry(frame)
        self.precio_carga.grid(row=2, column=1, pady=5)

        tk.Button(frame, text="Confirmar", command=self.cargar).grid(row=3, column=0, columnspan=2, pady=10)

    def cargar(self):
        codigo = self.cod_carga.get()
        
        # VALIDACIÓN: Verificar si el código ya existe
        if self.db.consultar(codigo):
            messagebox.showerror("Error de Duplicado", f"El código {codigo} ya existe en la base de datos.")
            return # Detiene la ejecución para no insertar

        try:
            self.db.insertar(codigo, self.desc_carga.get(), self.precio_carga.get())
            messagebox.showinfo("Éxito", "Artículo cargado correctamente")
            self.limpiar_carga()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar: {e}")

    # ... (Los métodos setup_tab_consulta, setup_tab_listado, consultar y listar se mantienen igual que antes)

    def setup_tab_consulta(self):
        frame = tk.LabelFrame(self.tab_consulta, text="Artículo", fg="blue", padx=20, pady=20)
        frame.pack(padx=20, pady=20)
        tk.Label(frame, text="Código:").grid(row=0, column=0, sticky="e")
        self.cod_cons = tk.Entry(frame)
        self.cod_cons.grid(row=0, column=1, pady=5)
        tk.Label(frame, text="Descripción:").grid(row=1, column=0, sticky="e")
        self.desc_cons = tk.Entry(frame)
        self.desc_cons.grid(row=1, column=1, pady=5)
        tk.Label(frame, text="Precio:").grid(row=2, column=0, sticky="e")
        self.precio_cons = tk.Entry(frame)
        self.precio_cons.grid(row=2, column=1, pady=5)
        tk.Button(frame, text="Consultar", command=self.consultar).grid(row=3, column=0, columnspan=2, pady=10)

    def setup_tab_listado(self):
        tk.Button(self.tab_listado, text="Listado completo", command=self.listar).pack(pady=10)
        self.txt_listado = scrolledtext.ScrolledText(self.tab_listado, width=40, height=10)
        self.txt_listado.pack(padx=10, pady=10)

    def consultar(self):
        res = self.db.consultar(self.cod_cons.get())
        if res:
            self.desc_cons.delete(0, tk.END)
            self.desc_cons.insert(0, res[0])
            self.precio_cons.delete(0, tk.END)
            self.precio_cons.insert(0, res[1])
        else:
            messagebox.showwarning("Error", "Código no encontrado")

    def listar(self):
        articulos = self.db.listar_todos()
        self.txt_listado.delete(1.0, tk.END)
        for art in articulos:
            self.txt_listado.insert(tk.END, f"Cod: {art[0]} | {art[1]} | ${art[2]}\n")

    def limpiar_carga(self):
        self.cod_carga.delete(0, tk.END)
        self.desc_carga.delete(0, tk.END)
        self.precio_carga.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = AppArticulos(root)
    root.mainloop()