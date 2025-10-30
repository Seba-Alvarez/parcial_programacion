#ejecutar con python -m gui.main

# GUI - main.py
import tkinter as tk
from tkinter import ttk
import sys


def ensure_theme(root):
    style = ttk.Style(root)
    try:
        style.theme_use('xpnative')
    except Exception:
        # si no existe, usar default pero no fallar
        pass

from gui.ventanas_crud_alumnos import FrameAlumnos
from gui.ventanas_crud_docentes import FrameDocentes
from gui.ventanas_crud_problemas import FrameProblemas

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema - GUI (Tkinter) - Capas")
        self.geometry("900x600")
        ensure_theme(self)

        # Menu o botones principales
        menubar = tk.Menu(self)
        self.config(menu=menubar)
        archivo_menu = tk.Menu(menubar, tearoff=0)
        archivo_menu.add_command(label="Salir", command=self.quit)
        menubar.add_cascade(label="Archivo", menu=archivo_menu)

        # Botones rápido
        toolbar = ttk.Frame(self, padding=6)
        toolbar.pack(side="top", fill="x")
        ttk.Button(toolbar, text="Alumnos", command=self.open_alumnos).pack(side="left", padx=4)
        ttk.Button(toolbar, text="Docentes", command=self.open_docentes).pack(side="left", padx=4)
        ttk.Button(toolbar, text="Problemas", command=self.open_problemas).pack(side="left", padx=4)

        # Area central: notebook
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True, padx=8, pady=8)

    def open_alumnos(self):
        # evitar duplicados
        for i in range(len(self.notebook.tabs())):
            pass
        frame = FrameAlumnos(self.notebook)
        self.notebook.add(frame, text="Alumnos")
        self.notebook.select(frame)

    def open_docentes(self):
        frame = FrameDocentes(self.notebook)
        self.notebook.add(frame, text="Docentes")
        self.notebook.select(frame)

    def open_problemas(self):
        frame = FrameProblemas(self.notebook)
        self.notebook.add(frame, text="Problemas")
        self.notebook.select(frame)

if __name__ == "__main__":
    app = App()
    app.mainloop()
