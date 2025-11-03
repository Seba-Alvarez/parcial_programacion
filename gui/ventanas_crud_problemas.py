# GUI - ventanas_crud_problemas.py
import tkinter as tk
from tkinter import ttk, messagebox
from logica.Problemas import Problemas
from logica.CrudProblemas import CrudProblemas
from persistencia.pCrudProblemas import pCrudProblemas

class FrameProblemas(ttk.Frame):
    def __init__(self, parent, pers=None):
        super().__init__(parent)     
        self.pers = pers or pCrudProblemas()
        self.crud = CrudProblemas(self.pers)
        self.build_ui()

    def build_ui(self):
        form = ttk.Labelframe(self, text="Crear / Modificar Problema", padding=10)
        form.grid(row=0, column=0, sticky="nsew", padx=8, pady=8)

        ttk.Label(form, text="Descripción:").grid(row=0, column=0, sticky="w")
        self.desc = ttk.Entry(form); self.desc.grid(row=0, column=1, sticky="ew")
        ttk.Label(form, text="Dificultad:").grid(row=1, column=0, sticky="w")
        self.dif = ttk.Entry(form); self.dif.grid(row=1, column=1, sticky="ew")
        ttk.Label(form, text="Lenguaje:").grid(row=2, column=0, sticky="w")
        self.lang = ttk.Entry(form); self.lang.grid(row=2, column=1, sticky="ew")
        self.aprobado_var = tk.IntVar()
        ttk.Checkbutton(form, text="Aprobado", variable=self.aprobado_var).grid(row=3, column=0, columnspan=2, sticky="w")

        btn_frame = ttk.Frame(form); btn_frame.grid(row=4, column=0, columnspan=2, pady=6)
        ttk.Button(btn_frame, text="Crear", command=self.crear_problema).grid(row=0, column=0, padx=4)
        ttk.Button(btn_frame, text="Modificar", command=self.modificar_problema).grid(row=0, column=1, padx=4)
        ttk.Button(btn_frame, text="Eliminar", command=self.eliminar_problema).grid(row=0, column=2, padx=4)
        ttk.Button(btn_frame, text="Refrescar lista", command=self.refrescar).grid(row=0, column=3, padx=4)

        tv_frame = ttk.Labelframe(self, text="Listado de Problemas", padding=10)
        tv_frame.grid(row=1, column=0, sticky="nsew", padx=8, pady=8)
        self.tree = ttk.Treeview(tv_frame, columns=("desc","dif","lang","aprob"), show="headings", height=10)
        for col, text in [("desc","Descripción"),("dif","Dificultad"),("lang","Lenguaje"),("aprob","Aprobado")]:
            self.tree.heading(col, text=text); self.tree.column(col, width=140)
        self.tree.pack(fill="both", expand=True); self.tree.bind("<<TreeviewSelect>>", self.on_select)
        self.refrescar()

    def crear_problema(self):
        desc = self.desc.get().strip()
        dif = self.dif.get().strip()
        lang = self.lang.get().strip()
        apr = bool(self.aprobado_var.get())
        if not (desc and dif and lang):
            messagebox.showwarning("Faltan datos", "Completa descripción, dificultad y lenguaje.")
            return
        prob = Problemas(desc, dif, lang, apr)
        ok, msg = self.crud.alta(prob)
        messagebox.showinfo("Alta", msg)
        self.refrescar()

    def modificar_problema(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showwarning("Seleccionar", "Selecciona un problema para modificar."); return
        desc_old = self.tree.item(sel[0])['values'][0]
        new_desc = self.desc.get().strip() or None
        new_dif = self.dif.get().strip() or None
        new_lang = self.lang.get().strip() or None
        new_apr = bool(self.aprobado_var.get())
        ok, msg = self.crud.modificar(desc_old, new_desc=new_desc, new_dificultad=new_dif, new_lenguaje=new_lang, new_aprobado=new_apr)
        messagebox.showinfo("Modificar", msg); self.refrescar()

    def eliminar_problema(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showwarning("Seleccionar", "Selecciona un problema para eliminar."); return
        desc = self.tree.item(sel[0])['values'][0]
        ok, msg = self.crud.baja(desc)
        if ok: messagebox.showinfo("Eliminar", f"Problema '{desc}' eliminado.")
        else: messagebox.showwarning("Eliminar", f"No se encontró el problema '{desc}'.")
        self.refrescar()

    def refrescar(self):
        for r in self.tree.get_children(): self.tree.delete(r)
        rows = self.crud.listar()
        # rows may be tuples (descripcion, dificultad, lenguaje, aprobado)
        if rows and isinstance(rows[0], tuple):
            for r in rows:
                self.tree.insert("", "end", values=(r[0], r[1], r[2], "Sí" if r[3] else "No"))
        else:
            for s in rows:
                self.tree.insert("", "end", values=(s, "", "", ""))

    def on_select(self, event):
        sel = self.tree.selection()
        if not sel: return
        vals = self.tree.item(sel[0])['values']
        self.desc.delete(0,"end"); self.desc.insert(0, vals[0])
        self.dif.delete(0,"end"); self.dif.insert(0, vals[1])
        self.lang.delete(0,"end"); self.lang.insert(0, vals[2])
        self.aprobado_var.set(1 if vals[3] == "Sí" else 0)
