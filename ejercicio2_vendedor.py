import tkinter as tk
from tkinter import ttk, messagebox

class Vendedor:
    def __init__(self, nombre, apellidos, edad):
        self.nombre = nombre.strip()
        self.apellidos = apellidos.strip()
        self.edad = self.verificar_edad(edad)

    @staticmethod
    def verificar_edad(edad):
        if edad < 0 or edad > 120:
            raise ValueError("La edad no puede ser negativa ni mayor a 120.")
        if edad <= 18:
            raise ValueError("El vendedor debe ser mayor de 18 años.")
        return edad

    def imprimir(self):
        return (f"Nombre del vendedor: {self.nombre}\n"
                f"Apellidos del vendedor: {self.apellidos}\n"
                f"Edad del vendedor: {self.edad}")

class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        root.title("Ejercicio 6.5 - Vendedor")
        root.geometry("570x430")
        root.minsize(500, 390)
        marco = ttk.Frame(root, padding=24)
        marco.pack(fill="both", expand=True)
        ttk.Label(marco, text="Registro de vendedor", font=("Segoe UI", 18, "bold")).pack(anchor="w")
        ttk.Label(marco, text="La edad debe estar entre 19 y 120 años.", foreground="#526174").pack(anchor="w", pady=(4, 18))
        formulario = ttk.Frame(marco)
        formulario.pack(fill="x")
        self.nombre = self.campo(formulario, "Nombre", 0)
        self.apellidos = self.campo(formulario, "Apellidos", 1)
        self.edad = self.campo(formulario, "Edad", 2)
        ttk.Button(marco, text="Validar y registrar", command=self.registrar).pack(anchor="w", pady=18)
        self.resultado = tk.Text(marco, height=6, wrap="word", font=("Segoe UI", 10), bg="#f1f5f9", fg="#172033", relief="flat", padx=12, pady=10)
        self.resultado.pack(fill="both", expand=True)
        self.resultado.insert("end", "Los datos del vendedor aparecerán aquí.")
        self.resultado.configure(state="disabled")

    @staticmethod
    def campo(parent, texto, fila):
        ttk.Label(parent, text=texto).grid(row=fila, column=0, sticky="w", pady=7)
        entrada = ttk.Entry(parent, width=38)
        entrada.grid(row=fila, column=1, sticky="ew", padx=(18, 0), pady=7)
        parent.columnconfigure(1, weight=1)
        return entrada

    def registrar(self):
        try:
            nombre = self.nombre.get().strip()
            apellidos = self.apellidos.get().strip()
            if not nombre or not apellidos:
                raise ValueError("Debe ingresar el nombre y los apellidos.")
            try:
                edad = int(self.edad.get().strip())
            except ValueError as exc:
                raise ValueError("La edad debe ser un número entero.") from exc
            vendedor = Vendedor(nombre, apellidos, edad)
            self.resultado.configure(state="normal")
            self.resultado.delete("1.0", "end")
            self.resultado.insert("end", vendedor.imprimir())
            self.resultado.configure(state="disabled")
        except ValueError as exc:
            messagebox.showerror("Error de validación", str(exc), parent=self.root)

if __name__ == "__main__":
    root = tk.Tk()
    VentanaPrincipal(root)
    root.mainloop()
