#ejecutar con python -m gui.main
#ejecutar tests con pytest -s -v

#Importamos tkinter para hacer la interfaz
import tkinter as tk
#aca importamos los metodos de tkinter
from tkinter import ttk
#sys para manejar rutas, para poder hacer un diseño por carpetas,
#como personas civilizadas
import sys


#la idea era poder usar esto para hacer que la ventana se viera como windows xp
def ensure_theme(root):
    #importamos style de tkinter
    style = ttk.Style(root)
    #con un try catch lo mandamos a ver si anda, pero con manejo de errores para que 
    #cargue igual, aunque no sea compatible
    try:
        #al final, no fue compatible
        style.theme_use('xpnative')
    except Exception:
        #si no existe, usar default para no romper nada
        pass

#aca se importan los cruds de las clases
from gui.ventanas_crud_alumnos import FrameAlumnos
from gui.ventanas_crud_docentes import FrameDocentes
from gui.ventanas_crud_problemas import FrameProblemas

#la clase App de tkinter, no la hicimos nosotros, es de tkinter misma
class App(tk.Tk):
    #se inicializa el constructor
    def __init__(self):
        #con super heredamos los metodos de la clase App de tkinter
        super().__init__()
        #este titulo es el que aparece arriba de la ventana centrado
        self.title("Sistema - GUI (Tkinter) - Capas")
        #esto es la resolución de la ventana
        self.geometry("900x600")
        #aca se llama a la función para intentar aplicar el estilo "windows xp"
        ensure_theme(self)

        #Menu, usando la clase de tkinter y se le pasa la ventana actual por parametro
        menubar = tk.Menu(self)
        #se asocia el menu guardadado en la variable de arriba para mostrarlo
        self.config(menu=menubar)
        #aca se esta diciendo si el menu puede aparecer como una ventana separada flotante
        #es decir, te permite arrastrarlo, pero en 0 esto esta desactivado
        archivo_menu = tk.Menu(menubar, tearoff=0)
        #aca se crea un boton "salir", que, efectivamente sirve para salir
        archivo_menu.add_command(label="Salir", command=self.quit)
        #aca es donde esta ubicado el comando "salir"
        #que a efectos prácticos, "salir" y cerrar la ventanana es lo mismo
        menubar.add_cascade(label="Archivo", menu=archivo_menu)

        #Botones
        #frame es el equivalente a un div, es un contenedor
        #padding le esta agregando un poco de "relleno" para que los botones no esten tan pegados
        toolbar = ttk.Frame(self, padding=6)
        #aca dice donde se va a mostrar la "barra" con los botones
        #fill x es que se alargue por toda la ventana
        toolbar.pack(side="top", fill="x")
        #Aca se accede a los cruds
        ttk.Button(toolbar, text="Alumnos", command=self.open_alumnos).pack(side="left", padx=4)
        ttk.Button(toolbar, text="Docentes", command=self.open_docentes).pack(side="left", padx=4)
        ttk.Button(toolbar, text="Problemas", command=self.open_problemas).pack(side="left", padx=4)

        #Aca se abren las "pestañas", eso es notebook
        self.notebook = ttk.Notebook(self)
        #pack es para controlar donde va el contenedor
        self.notebook.pack(fill="both", expand=True, padx=8, pady=8)

    #aca se abre la ventana con el crud de alumnos
    def open_alumnos(self):
        #esto sería para evitar duplicados, implementar a futuro
        for i in range(len(self.notebook.tabs())):
            pass
        #aca se esta creando un nuevo frame (una sección de la interfaz) para poner el
        #boton para ingresar al crud
        frame = FrameAlumnos(self.notebook)
        #aca se esta agregando la ventana de cruds a la ventana principal
        self.notebook.add(frame, text="Alumnos")
        #esto te redirige por defecto a la ventana creada (como abrir una nueva pestaña en un navegador)
        self.notebook.select(frame)

    #lo mismo que en alumnos
    def open_docentes(self):
        frame = FrameDocentes(self.notebook)
        self.notebook.add(frame, text="Docentes")
        self.notebook.select(frame)

    #lo mismo que en alumnos y docentes
    def open_problemas(self):
        frame = FrameProblemas(self.notebook)
        self.notebook.add(frame, text="Problemas")
        self.notebook.select(frame)

#aca es donde corre la app
if __name__ == "__main__":
    app = App()
    app.mainloop()
