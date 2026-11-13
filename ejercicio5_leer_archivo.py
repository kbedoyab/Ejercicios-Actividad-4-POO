import io
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

class LeerArchivo:

    @staticmethod
    def leer(ruta):
        
        with open(ruta, "rb") as archivo_bytes:
            with io.TextIOWrapper(archivo_bytes, encoding="utf-8") as lector:
                return lector.read()

class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        root.title("Ejercicio 6.8 - Lectura de archivos")
        root.geometry("760x560")
        root.minsize(620, 460)
        marco = ttk.Frame(root, padding=22)
        marco.pack(fill="both", expand=True)
        ttk.Label(marco, text="Lector de archivos de texto", font=("Segoe UI", 18, "bold")).pack(anchor="w")
        ttk.Label(marco, text="Selecciona un archivo .txt para mostrar su contenido.", foreground="#526174").pack(anchor="w", pady=(4, 14))
        barra = ttk.Frame(marco)
        barra.pack(fill="x", pady=(0, 12))
        self.ruta = tk.StringVar(value="Ningún archivo seleccionado")
        ttk.Button(barra, text="Seleccionar archivo", command=self.seleccionar).pack(side="left")
        ttk.Label(barra, textvariable=self.ruta, wraplength=470).pack(side="left", padx=12)
        self.contenido = tk.Text(marco, wrap="word", font=("Consolas", 10), bg="#101827", fg="#e5edf7", insertbackground="white", relief="flat", padx=14, pady=12)
        self.contenido.pack(fill="both", expand=True)
        self.contenido.insert("end", "El contenido del archivo aparecerá aquí.")
        self.contenido.configure(state="disabled")

    def seleccionar(self):
        ruta = filedialog.askopenfilename(
            parent=self.root,
            title="Seleccionar archivo de texto",
            filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
        )
        if not ruta:
            return
        try:
            texto = LeerArchivo.leer(ruta)
            self.ruta.set(ruta)
            self.contenido.configure(state="normal")
            self.contenido.delete("1.0", "end")
            self.contenido.insert("end", texto if texto else "El archivo está vacío.")
            self.contenido.configure(state="disabled")
        except (OSError, UnicodeError) as exc:
            messagebox.showerror("Error de lectura", f"No se pudo leer el archivo.\n{exc}", parent=self.root)

if __name__ == "__main__":
    root = tk.Tk()
    VentanaPrincipal(root)
    root.mainloop()
