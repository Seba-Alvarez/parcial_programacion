#importamos tkinter (el ui) y sus métodos (para no hacerlo a mano)
import tkinter as tk
from tkinter import ttk, messagebox
#clases de la capa lógica
from logica.Alumnos import Alumnos
from logica.CrudAlumnos import CrudAlumnos
#clase de la persistencia
from persistencia.pCrudAlumnos import pCrudAlumnos

#esta clase maneja todo lo relacionado con los alumnos
class FrameAlumnos(ttk.Frame):
    #constructor con la clase padre e inicializar la persistencia
    def __init__(self, parent, pers=None):
        super().__init__(parent)
        #si no se pasa una persistencia por parámetro, se crea una por defecto
        #es decir, si no existe, se crea el archivo
        self.pers = pers or pCrudAlumnos()
        #se creaa el crud con la persistencia correspondiente (la de los alumnos)
        self.crud = CrudAlumnos(self.pers)
        #armamos la interfaz
        self.build_ui()

    #esta función arma toda la interfaz (formularios y listado)
    def build_ui(self):
        #Formulario alta o crear el alumno
        #se importa el template de un label de tkinter
        form = ttk.Labelframe(self, text="Crear Alumno", padding=10)
        #se pone grid en la parte superior del frame
        form.grid(row=0, column=0, sticky="nsew", padx=8, pady=8)

        #lo que se pide en el formulario (técnicamente es un formulario x 2)
        #sticky="w" alinea el label para la derecha
        ttk.Label(form, text="Nombre:").grid(row=0, column=0, sticky="w")
        #entry es un equivalente a input, se esta capturando el contenido del textbox en el form
        self.nombre = ttk.Entry(form)
        #ew extiende el textbox horizontalmente
        self.nombre.grid(row=0, column=1, sticky="ew")

        #lo mismo que arriba
        ttk.Label(form, text="Edad:").grid(row=1, column=0, sticky="w")
        self.edad = ttk.Entry(form)
        self.edad.grid(row=1, column=1, sticky="ew")

        #sigue en la misma
        ttk.Label(form, text="Usuario:").grid(row=2, column=0, sticky="w")
        self.user = ttk.Entry(form)
        self.user.grid(row=2, column=1, sticky="ew")

        #repitiendo lo mismo
        ttk.Label(form, text="Contraseña:").grid(row=3, column=0, sticky="w")
        self.passw = ttk.Entry(form, show="*")
        self.passw.grid(row=3, column=1, sticky="ew")

        #se crea el frame con los botones
        btn_frame = ttk.Frame(form)
        #row 4: va en la fila 4 del grid.
        #column 0: empieza en la primera columna.
        #columnspan 2: ocupa dos columnas de ancho.
        btn_frame.grid(row=4, column=0, columnspan=2, pady=6)

        #botones que llaman a los cruds
        ttk.Button(btn_frame, text="Crear", command=self.crear_alumno).grid(row=0, column=0, padx=4)
        ttk.Button(btn_frame, text="Modificar", command=self.modificar_alumno).grid(row=0, column=1, padx=4)
        ttk.Button(btn_frame, text="Eliminar", command=self.eliminar_alumno).grid(row=0, column=2, padx=4)
        ttk.Button(btn_frame, text="Refrescar lista", command=self.refrescar).grid(row=0, column=3, padx=4)

        #se crea un marco con borde y título (un label) dentro del div
        tv_frame = ttk.Labelframe(self, text="Listado de Alumnos", padding=10)
        #el label se pone dentro del layout del contenedor
        tv_frame.grid(row=1, column=0, sticky="nsew", padx=8, pady=8)
        #se crea el treeview, es decir, que se presenta la información en filas y/o columnas
        self.tree = ttk.Treeview(tv_frame, columns=("nombre","edad","user","pass"), show="headings", height=10)
        #se recorre una lista de tuplas con los valores que tiene cada atributo
        for col, text in [("nombre","Nombre"),("edad","Edad"),("user","Usuario"),("pass","Contraseña")]:
            #como se puede apreciar en este caso, son columnas
            self.tree.heading(col, text=text)
            self.tree.column(col, width=120)
        #pack mete el widget en el div, es de los mas facilitos de usar
        self.tree.pack(fill="both", expand=True)
        #se captura el evento, esto es una funcion de tkinter para manejar la interacción con el user
        self.tree.bind("<<TreeviewSelect>>", self.on_select)
        #refrescar es para actualizar el listado
        self.refrescar()

    #aca ocurre la magia, se crean los alumnos en base a los datos obtenidos de los textbox
    def crear_alumno(self):
        #get busca lo que se ingreso y strip le quita los espacios
        #los nombres de los campos son bastante intuitivos
        #self. es porque estamos instanciando los atributos de la calse  alumno
        nombre = self.nombre.get().strip()
        edad = self.edad.get().strip()
        user = self.user.get().strip()
        pw = self.passw.get().strip()
        #aca se chequea si faltan algunos datos por ingresar
        #técnicamente no se esta chequeando el password, peeeero....
        if not (nombre and edad and user):
            #lo mismo que raise error, se te enoja y te dice "che, te faltan datos" pero mas lindo
            messagebox.showwarning("Faltan datos", "Completa nombre, edad y usuario.")
            return
        try:
            #por si algun listillo quiere poner letras o algo que no sea un numero
            #o un numero con coma
            edad_i = int(edad)
        except ValueError:
            #"che, nadie tiene 23,453 años, es 23"
            messagebox.showerror("Edad inválida", "Edad debe ser un número entero.")
            return
        #Crea un objeto Alumnos con los datos validos y validados
        alumno = Alumnos(nombre, edad_i, user, pw)
        #ok es que puede seguir, es literalmente un ok
        #smg es un mensaje (se suele usar para debuggear y crear apps con feedback)
        #y se llama al metodo alta del crud (pasandole los datos del alumno)
        ok, msg = self.crud.alta(alumno)
        #este es el mensaje que se muestra arriba
        messagebox.showinfo("Alta", msg)
        self.refrescar()

    #aca se modifican los alumnos
    def modificar_alumno(self):
        #aca se devuelve una tupla con el id (interno) de la columna seleccionada
        sel = self.tree.selection()
        #aca se chequea que efectivamente se seleccione una columna
        if not sel:
            #"che, no seleccionaste una columna"
            messagebox.showwarning("Seleccionar", "Selecciona un alumno para modificar (por usuario).")
            return
        
        #sel[0] es el ID de la primera fila seleccionada.
        #tree.item(sel[0])['values'] devuelve todos los valores de esa fila como lista
        #el 2 toma la tercera columna, que corresponde al usuer, que es un unique
        user_old = self.tree.item(sel[0])['values'][2]

        #se obtienen los nuevos valores sin espacios
        nombre = self.nombre.get().strip() or None
        edad = self.edad.get().strip()
        edad_i = None
        #lo mismo de arriba para los listos, cuando se hace if edad (if nombre, etc.)
        #se esta diciendo "hay algo en el campo edad?"
        if edad:
            try:
                edad_i = int(edad)
            except ValueError:
                messagebox.showerror("Edad inválida", "Edad debe ser un número entero.")
                return
        #seguimos capturando los valores nuevos
        new_user = self.user.get().strip() or None
        new_pw = self.passw.get().strip() or None
        #aca se da el ok y se modifican los campos con los valores ingresados
        ok, msg = self.crud.modificar(user_old, new_nombreU=nombre, new_edad=edad_i, new_userA=new_user, new_passA=new_pw)
        messagebox.showinfo("Modificar", msg)
        self.refrescar()

    #se eliminan los alumnos
    def eliminar_alumno(self):
        #se usan los datos seleccionados
        sel = self.tree.selection()
        #se verifica que seleccionen algo antes de borrar
        if not sel:
            messagebox.showwarning("Seleccionar", "Selecciona un alumno para eliminar (por usuario).")
            return
        #lo mismo que arriba, se toma el tercer valor el user que es unico
        #recordar que los indices arrancan desde el 0
        user = self.tree.item(sel[0])['values'][2]
        #se da el ok
        ok, msg = self.crud.baja(user)
        #si todo salio bien y se dio el ok
        if ok:
            #se elimina el alumno
            messagebox.showinfo("Eliminar", f"Alumno '{user}' eliminado.")
        #si se partio algo
        else:
            #por si algo male sal y que no parta el programa
            messagebox.showwarning("Eliminar", f"No se encontró el alumno '{user}'.")
        self.refrescar()

    def refrescar(self):
        #get_children() devuelve todos los IDs de las filas
        #delete(r) elimina cada fila para evitando duplicados
        for r in self.tree.get_children():
            self.tree.delete(r)
        #este metodo cumple otro proposito, si se crea un alumno en otra pestaña, para no tener que cerrar todo
        #o por si sale algo mal o la razon que sea, siempre se puede actualizar la lista dentro del programa mismo
        #aca se recuperan todos los datos de los alumnos
        rows = self.crud.listar()
        #verifica que las rows no esten vacias y que el primer elemento sea una tupla (tecnicamente todos tienen que serlo)
        if rows and isinstance(rows[0], tuple):
            for r in rows:
                #(nombre, edad, userA, passA) son los elementos en cada posicion del indice
                self.tree.insert("", "end", values=(r[0], r[1], r[2], r[3]))
        else:
            #se recorren los datos en cada columna
            for s in rows:
                try:
                    #split separa cada elemento con lo que se le ponga, comas en este caso
                    parts = s.split(",")
                    #se separa cada campo con comas
                    nombre = parts[0].split("Nombre:")[1].strip()
                    edad = parts[1].split("Edad:")[1].strip()
                    user = parts[2].split("Usuario:")[1].strip()
                    #aca se inserta la fila en el treeview, el primer "" es para insertar todos al mismo nivel
                    #el ultimo "" es para no mostrar las password, es mas bien estetico
                    self.tree.insert("", "end", values=(nombre, edad, user, ""))
                except Exception:
                    #Si falla algo, se inserta todo en la primera columna y se deja vacio lo demás
                    self.tree.insert("", "end", values=(s, "", "", ""))

    #on_select es para efectivamente seleccionar cada evento
    def on_select(self, event):
        #desto evuelve una tupla con los IDs de las filas seleccionadas
        #Si no hay ninguna fila seleccionada, se sale de la función con return
        sel = self.tree.selection()
        if not sel:
            return
        #aca se busca el id de la primera fila y se devuelve un diccionario con la info de la fila
        vals = self.tree.item(sel[0])['values']
        #antes de el ; se estan borrando los contenidos viejos (para evitar problemas)
        #despues del ; se insertan los valores en sus correspondientes filas
        self.nombre.delete(0, "end"); self.nombre.insert(0, vals[0])
        self.edad.delete(0, "end"); self.edad.insert(0, vals[1])
        self.user.delete(0, "end"); self.user.insert(0, vals[2])
        #este ultimo if es por si no existe un pass, se autorrellena como vacio
        #esto para poder manejar muy a futuro contraseñas sugeridas
        self.passw.delete(0, "end"); self.passw.insert(0, vals[3] if len(vals)>3 else "")
