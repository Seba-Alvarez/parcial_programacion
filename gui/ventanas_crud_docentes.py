#Aca aplican los mismos comentarios que en ventanas_crud_alumnos.
import tkinter as tk
from tkinter import ttk, messagebox
from logica.Docentes import Docentes
from logica.CrudDocentes import CrudDocentes
from persistencia.pCrudDocentes import pCrudDocentes

class FrameDocentes(ttk.Frame):
    def __init__(self, parent, pers=None):
        super().__init__(parent)
        self.pers = pers or pCrudDocentes()
        self.crud = CrudDocentes(self.pers)
        self.build_ui()

    def build_ui(self):
        form = ttk.Labelframe(self, text="Crear / Modificar Docente", padding=10)
        form.grid(row=0, column=0, sticky="nsew", padx=8, pady=8)

        ttk.Label(form, text="Nombre:").grid(row=0, column=0, sticky="w")
        self.nombre = ttk.Entry(form); self.nombre.grid(row=0, column=1, sticky="ew")
        ttk.Label(form, text="Edad:").grid(row=1, column=0, sticky="w")
        self.edad = ttk.Entry(form); self.edad.grid(row=1, column=1, sticky="ew")
        ttk.Label(form, text="Usuario:").grid(row=2, column=0, sticky="w")
        self.user = ttk.Entry(form); self.user.grid(row=2, column=1, sticky="ew")
        ttk.Label(form, text="Contraseña:").grid(row=3, column=0, sticky="w")
        self.passw = ttk.Entry(form, show="*"); self.passw.grid(row=3, column=1, sticky="ew")

        btn_frame = ttk.Frame(form); btn_frame.grid(row=4, column=0, columnspan=2, pady=6)
        ttk.Button(btn_frame, text="Crear", command=self.crear_docente).grid(row=0, column=0, padx=4)
        ttk.Button(btn_frame, text="Modificar", command=self.modificar_docente).grid(row=0, column=1, padx=4)
        ttk.Button(btn_frame, text="Eliminar", command=self.eliminar_docente).grid(row=0, column=2, padx=4)
        ttk.Button(btn_frame, text="Refrescar lista", command=self.refrescar).grid(row=0, column=3, padx=4)

        tv_frame = ttk.Labelframe(self, text="Listado de Docentes", padding=10)
        tv_frame.grid(row=1, column=0, sticky="nsew", padx=8, pady=8)
        self.tree = ttk.Treeview(tv_frame, columns=("nombre","edad","user","pass"), show="headings", height=10)
        for col, text in [("nombre","Nombre"),("edad","Edad"),("user","Usuario"),("pass","Contraseña")]:
            self.tree.heading(col, text=text)
            self.tree.column(col, width=120)
        self.tree.pack(fill="both", expand=True); self.tree.bind("<<TreeviewSelect>>", self.on_select)
        self.refrescar()

    def crear_docente(self):
        nombre = self.nombre.get().strip(); edad = self.edad.get().strip()
        user = self.user.get().strip(); pw = self.passw.get().strip()
        if not (nombre and edad and user):
            messagebox.showwarning("Faltan datos", "Completa nombre, edad y usuario.")
            return
        try:
            edad_i = int(edad)
        except ValueError:
            messagebox.showerror("Edad inválida", "Edad debe ser un número entero."); return
        docente = Docentes(nombre, edad_i, user, pw)
        ok, msg = self.crud.alta(docente); messagebox.showinfo("Alta", msg); self.refrescar()

    def modificar_docente(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showwarning("Seleccionar", "Selecciona un docente para modificar."); return
        user_old = self.tree.item(sel[0])['values'][2]
        nombre = self.nombre.get().strip() or None
        edad = self.edad.get().strip()
        edad_i = None
        if edad:
            try: edad_i = int(edad)
            except ValueError:
                messagebox.showerror("Edad inválida", "Edad debe ser un número entero."); return
        new_user = self.user.get().strip() or None
        new_pw = self.passw.get().strip() or None
        ok, msg = self.crud.modificar(user_old, new_nombreU=nombre, new_edad=edad_i, new_userD=new_user, new_passD=new_pw)
        messagebox.showinfo("Modificar", msg); self.refrescar()

    def eliminar_docente(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showwarning("Seleccionar", "Selecciona un docente para eliminar."); return
        user = self.tree.item(sel[0])['values'][2]
        ok, msg = self.crud.baja(user)
        if ok: messagebox.showinfo("Eliminar", f"Docente '{user}' eliminado.")
        else: messagebox.showwarning("Eliminar", f"No se encontró el docente '{user}'.")
        self.refrescar()

    def refrescar(self):
        for r in self.tree.get_children(): self.tree.delete(r)
        rows = self.crud.listar()
        if rows and isinstance(rows[0], tuple):
            for r in rows: self.tree.insert("", "end", values=(r[0], r[1], r[2], r[3]))
        else:
            for s in rows:
                try:
                    parts = s.split(",")
                    nombre = parts[0].split("Nombre:")[1].strip()
                    edad = parts[1].split("Edad:")[1].strip()
                    user = parts[2].split("Usuario:")[1].strip()
                    self.tree.insert("", "end", values=(nombre, edad, user, ""))
                except Exception:
                    self.tree.insert("", "end", values=(s, "", "", ""))

    def on_select(self, event):
        sel = self.tree.selection()
        if not sel: return
        vals = self.tree.item(sel[0])['values']
        self.nombre.delete(0, "end"); self.nombre.insert(0, vals[0])
        self.edad.delete(0, "end"); self.edad.insert(0, vals[1])
        self.user.delete(0, "end"); self.user.insert(0, vals[2])
        self.passw.delete(0, "end"); self.passw.insert(0, vals[3] if len(vals)>3 else "")
