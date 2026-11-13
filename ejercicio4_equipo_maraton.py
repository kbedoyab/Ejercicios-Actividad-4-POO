import tkinter as tk
from tkinter import ttk, messagebox

class Programador:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos

class EquipoMaratonProgramacion:
    MAXIMO_PROGRAMADORES = 3
    MINIMO_PROGRAMADORES = 2

    def __init__(self, nombre_equipo, universidad, lenguaje_programacion):
        self.nombre_equipo = nombre_equipo.strip()
        self.universidad = universidad.strip()
        self.lenguaje_programacion = lenguaje_programacion.strip()
        self.programadores = []
        self.tamaño_equipo = 0

    @staticmethod
    def validar_campo(campo, etiqueta="El campo"):
        texto = campo.strip()
        if not texto:
            raise ValueError(f"{etiqueta} no puede estar vacío.")
        if any(not (caracter.isalpha() or caracter.isspace()) for caracter in texto):
            raise ValueError(f"{etiqueta} debe contener solo texto, sin números ni símbolos.")
        if len(texto) >= 20:
            raise ValueError(f"{etiqueta} debe tener menos de 20 caracteres.")
        return texto

    def esta_completo(self):
        return self.tamaño_equipo == self.MAXIMO_PROGRAMADORES

    def añadir(self, programador):
        if self.esta_completo():
            raise ValueError("El equipo está completo. No se pudo agregar programador.")
        self.programadores.append(programador)
        self.tamaño_equipo += 1

    def validar_composicion(self):
        if self.tamaño_equipo < self.MINIMO_PROGRAMADORES:
            raise ValueError("El equipo debe tener como mínimo dos programadores.")

class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        root.title("Ejercicio 6.7 - Equipo de maratón")
        root.geometry("760x850")
        root.minsize(680, 760)
        marco = ttk.Frame(root, padding=20)
        marco.pack(fill="both", expand=True)
        ttk.Label(marco, text="Equipo de maratón de programación", font=("Segoe UI", 18, "bold")).pack(anchor="w")
        ttk.Label(marco, text="Registra un equipo con dos o tres integrantes.", foreground="#526174").pack(anchor="w", pady=(4, 12))
        equipo = ttk.LabelFrame(marco, text="Datos del equipo", padding=12)
        equipo.pack(fill="x", pady=(0, 12))
        self.nombre_equipo = self.campo(equipo, "Nombre del equipo", 0)
        self.universidad = self.campo(equipo, "Universidad", 1)
        self.lenguaje = self.campo(equipo, "Lenguaje de programación", 2)
        self.integrantes = []
        for i in range(3):
            grupo = ttk.LabelFrame(marco, text=f"Programador {i + 1}", padding=10)
            grupo.pack(fill="x", pady=5)
            nombre = self.campo(grupo, "Nombre", 0)
            apellidos = self.campo(grupo, "Apellidos", 1)
            self.integrantes.append((nombre, apellidos))
        ttk.Button(marco, text="Validar y crear equipo", command=self.crear_equipo).pack(anchor="w", pady=12)
        self.estado = tk.StringVar(value="Aún no se ha creado el equipo.")
        ttk.Label(marco, textvariable=self.estado, foreground="#1d4e89", wraplength=680).pack(anchor="w")

    @staticmethod
    def campo(parent, texto, fila):
        ttk.Label(parent, text=texto).grid(row=fila, column=0, sticky="w", pady=4)
        entrada = ttk.Entry(parent, width=44)
        entrada.grid(row=fila, column=1, sticky="ew", padx=(14, 0), pady=4)
        parent.columnconfigure(1, weight=1)
        return entrada

    def crear_equipo(self):
        try:
            activos = [(n, a) for n, a in self.integrantes if n.get().strip() or a.get().strip()]
            if not 2 <= len(activos) <= 3:
                raise ValueError("Debe ingresar como mínimo dos y como máximo tres programadores.")
            equipo = EquipoMaratonProgramacion(
                self.nombre_equipo.get(), self.universidad.get(), self.lenguaje.get()
            )
            if not all((equipo.nombre_equipo, equipo.universidad, equipo.lenguaje_programacion)):
                raise ValueError("Complete el nombre del equipo, la universidad y el lenguaje.")
            for indice, (campo_nombre, campo_apellidos) in enumerate(activos, start=1):
                nombre = EquipoMaratonProgramacion.validar_campo(campo_nombre.get(), f"Nombre del programador {indice}")
                apellidos = EquipoMaratonProgramacion.validar_campo(campo_apellidos.get(), f"Apellidos del programador {indice}")
                equipo.añadir(Programador(nombre, apellidos))
            equipo.validar_composicion()
            integrantes = "\n".join(f"• {p.nombre} {p.apellidos}" for p in equipo.programadores)
            self.estado.set(f"Equipo creado correctamente: {equipo.nombre_equipo}\nUniversidad: {equipo.universidad}\nLenguaje: {equipo.lenguaje_programacion}\nIntegrantes:\n{integrantes}")
        except ValueError as exc:
            messagebox.showerror("Error de validación", str(exc), parent=self.root)

if __name__ == "__main__":
    root = tk.Tk()
    VentanaPrincipal(root)
    root.mainloop()
