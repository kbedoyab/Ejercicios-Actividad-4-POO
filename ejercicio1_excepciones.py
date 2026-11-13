import tkinter as tk
from tkinter import ttk

class PruebaExcepciones:

    def ejecutar(self):
        salida = []

        try:
            salida.append("Ingresando al primer try")
            cociente = 10000 / 0
            salida.append(f"Después de la división: {cociente}")
        except ZeroDivisionError:
            salida.append("División por cero")
        finally:
            salida.append("Ingresando al primer finally")

        try:
            salida.append("Ingresando al segundo try")
            objeto = None
            objeto.toString()
            salida.append("Imprimiendo objeto")
        except ArithmeticError:
            salida.append("División por cero")
        except Exception:
            salida.append("Ocurrió una excepción")
        finally:
            salida.append("Ingresando al segundo finally")

        return salida

class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Ejercicio 6.4 - Manejo de excepciones")
        self.root.geometry("650x440")
        self.root.minsize(560, 380)
        self.modelo = PruebaExcepciones()

        marco = ttk.Frame(root, padding=22)
        marco.pack(fill="both", expand=True)
        ttk.Label(marco, text="Prueba de excepciones", font=("Segoe UI", 18, "bold")).pack(anchor="w")
        ttk.Label(marco, text="Ejecuta los dos bloques try / except / finally del ejercicio.", foreground="#526174").pack(anchor="w", pady=(4, 16))
        ttk.Button(marco, text="Ejecutar prueba", command=self.ejecutar).pack(anchor="w", pady=(0, 12))
        self.salida = tk.Text(marco, height=13, wrap="word", font=("Consolas", 11), bg="#101827", fg="#e5edf7", insertbackground="white", relief="flat", padx=14, pady=12)
        self.salida.pack(fill="both", expand=True)
        self.salida.insert("end", "Presiona «Ejecutar prueba» para observar la secuencia.\n")
        self.salida.configure(state="disabled")

    def ejecutar(self):
        self.salida.configure(state="normal")
        self.salida.delete("1.0", "end")
        self.salida.insert("end", "\n".join(self.modelo.ejecutar()))
        self.salida.configure(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    VentanaPrincipal(root)
    root.mainloop()
