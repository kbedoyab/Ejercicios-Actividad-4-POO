import math
import tkinter as tk
from tkinter import ttk, messagebox

class CalculosNumericos:
    @staticmethod
    def calcular_logaritmo_neperiano(valor):
        if valor <= 0:
            raise ArithmeticError("El valor debe ser un número positivo para calcular el logaritmo.")
        return math.log(valor)

    @staticmethod
    def calcular_raiz_cuadrada(valor):
        if valor <= 0:
            raise ArithmeticError("El valor debe ser un número positivo para calcular la raíz cuadrada.")
        return math.sqrt(valor)

class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        root.title("Ejercicio 6.6 - Cálculos numéricos")
        root.geometry("590x420")
        root.minsize(520, 370)
        marco = ttk.Frame(root, padding=24)
        marco.pack(fill="both", expand=True)
        ttk.Label(marco, text="Cálculos numéricos", font=("Segoe UI", 18, "bold")).pack(anchor="w")
        ttk.Label(marco, text="Calcula el logaritmo neperiano y la raíz cuadrada.", foreground="#526174").pack(anchor="w", pady=(4, 18))
        ttk.Label(marco, text="Valor numérico (double)").pack(anchor="w")
        self.valor = ttk.Entry(marco, width=32)
        self.valor.pack(anchor="w", fill="x", pady=(6, 14))
        ttk.Button(marco, text="Calcular", command=self.calcular).pack(anchor="w")
        self.logaritmo = tk.StringVar(value="Logaritmo neperiano: —")
        self.raiz = tk.StringVar(value="Raíz cuadrada: —")
        panel = ttk.LabelFrame(marco, text="Resultados", padding=16)
        panel.pack(fill="x", pady=22)
        ttk.Label(panel, textvariable=self.logaritmo, font=("Segoe UI", 11)).pack(anchor="w", pady=6)
        ttk.Label(panel, textvariable=self.raiz, font=("Segoe UI", 11)).pack(anchor="w", pady=6)

    def calcular(self):
        try:
            texto = self.valor.get().strip().replace(",", ".")
            if not texto:
                raise ValueError("Ingrese un valor numérico.")
            valor = float(texto)
            logaritmo = CalculosNumericos.calcular_logaritmo_neperiano(valor)
            raiz = CalculosNumericos.calcular_raiz_cuadrada(valor)
            self.logaritmo.set(f"Logaritmo neperiano: {logaritmo:.6f}")
            self.raiz.set(f"Raíz cuadrada: {raiz:.6f}")
        except ArithmeticError as exc:
            messagebox.showerror("Excepción aritmética", str(exc), parent=self.root)
        except ValueError:
            messagebox.showerror("Excepción de entrada", "El valor debe ser numérico.", parent=self.root)

if __name__ == "__main__":
    root = tk.Tk()
    VentanaPrincipal(root)
    root.mainloop()
