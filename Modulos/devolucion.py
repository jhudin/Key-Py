from tkinter import *
from PIL import *
import tkinter
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from Modulos.Conexion import *
import mysql.connector
from Modulos.comboboxauto import *
import sys


def devolucionmetod(Inicio):
    def Cerrar():
        if messagebox.askyesno("Cerrar", "¿Desea Cerrar elmodulo?"):
            PrestamoS.destroy()
            Inicio.update()
            Inicio.deiconify()
            

    PrestamoS = tk.Toplevel(Inicio)
    PrestamoS.title("Devoluciones")
    PrestamoS.geometry("580x400+440+170")
    PrestamoS.resizable(0, 0)
    PrestamoS.iconbitmap("Imagenes/llave.ico")
    PrestamoS.wm_attributes("-topmost", True)
    PrestamoS.config(bg="#008f4c")
    PrestamoS.protocol("WM_DELETE_WINDOW", Cerrar)
    PrestamoS.attributes("-alpha", 0.97)

    def docenteinfo():
        if(CodigoText.get() != ""):
            dato = conexionBd('root', 'llave')
            conect = mysql.connector.connect(**dato)
            cursor = conect.cursor()
            cursor.execute('SELECT * FROM `docentes` ')
            llavesR = cursor.fetchall()
            Programa = str
            Nombre = str
            comp = False
            global contador
            for row in llavesR:
                if(int(row[2]) == int(CodigoText.get())):
                    comp = True
                    Programa = str(str(row[0]))
                    Nombre = str(str(row[1]))
            cursor.close()
            conect.close()
            if(comp):
                nombrecomp.set(str.lower(Nombre))
                nombreapell = Nombre.split()
                nombrecomp.set(Nombre)
                nombreapell = Nombre.split()
                if(len(nombreapell)==4):
                    NombreVar.set(nombreapell[0]+" "+nombreapell[1])
                    ApellidoVar.set(nombreapell[2]+" "+nombreapell[3])
                elif(len(nombreapell)==3):
                    NombreVar.set(nombreapell[0])
                    ApellidoVar.set(nombreapell[1]+" "+nombreapell[2])
                else:
                    NombreVar.set(nombreapell[0])
                    ApellidoVar.set(nombreapell[1])
                CodigoVar.set(str(CodigoText.get()))
                ProgramaVar.set(Programa)
                PrestamoS.update()
                comp = False
        salasDoc = []
        dato = conexionBd('root', 'llave')
        conect = mysql.connector.connect(**dato)
        cursor = conect.cursor()
        valores = "SELECT * FROM `prestamo`"
        cursor.execute(valores)
        llavesP = cursor.fetchall()
        guardian = str
        verdfal = False
        for row in llavesP:
            if(str(str(row[4])) == str(nombrecomp.get())):
                if(guardian != str(row[7])):
                    verdfal = True
                    guardian = str(row[7])
                    salasDoc.append(str(row[7]))
        cursor.close()
        conect.close()
        if not verdfal:
            messagebox.showinfo("Docente", "El docente no cuenta con llaves registradas")
            Inicio.deiconify()
            PrestamoS.destroy()
        if verdfal:
            ComboboxMost(salasDoc, PrestamoS, 310, 280, 140, 279, "Prestar", 11)
        PrestamoS.update()
    CodigoText = StringVar()
    CodigoText.set("")
    NombreVar = StringVar()
    nombrecomp = StringVar()
    nombrecomp.set("")
    NombreVar.set("")
    ApellidoVar = StringVar()
    CodigoVar = StringVar()
    ProgramaVar = StringVar()
    log = PhotoImage(file="./Imagenes/logo.png")
    fondo = Label(PrestamoS, image=log)
    fondo.pack()
    fondoimg = PhotoImage(file="./Imagenes/udecLog.png")
    fondoverd = Label(PrestamoS, image=fondoimg,bg="#008f4c")
    fondoverd.place(relx=.35,rely=.20)
    text = Label(PrestamoS, text="ESCANEAR EL CARNET INSTITUCIONAL", font=("Impact", 20), borderwidth=0, fg="yellow", relief="flat", bg="#008f4c")
    text.place(x=24, y=80)
    CodigoText1 = Label(PrestamoS, text="Codigo", font=("Arial", 10), borderwidth=0, relief="flat", bg="#008f4c")
    CodigoText1.place(x=30, y=121)
    Codigo = Entry(PrestamoS, font=("Helvetica", 11), width=15, textvariable=CodigoText, relief="solid")
    Codigo.focus()
    Codigo.place(x=106, y=121)

    style = ttk.Style()
    style.map("C.TButton", foreground=[('pressed', 'red'), ('active', 'green')], background=[('pressed', '!disabled', 'black'), ('active', 'deepskyblue')])

    EnviarCod = ttk.Button(PrestamoS, text="Enviar", command=docenteinfo, style="C.TButton")
    EnviarCod.place(x=260, y=119)

    infodocente = Frame(PrestamoS)
    infodocente.place(x=30, y=200)

    Nombret = Label(PrestamoS, text="Nombre", font=("Helvetica", 10), bg="#008f4c")
    Nombret.place(x=30, y=200)
    Nombre = Entry(PrestamoS, font=("Helvetica", 11), width=15, textvariable=NombreVar, state=tk.DISABLED, relief="solid")
    Nombre.place(x=106, y=200)

    Apellidot = Label(PrestamoS, text="Apellido", font=("Helvetica", 10), bg="#008f4c")
    Apellidot.place(x=260, y=200)
    Apellido = Entry(PrestamoS, font=("Helvetica", 11), width=15, textvariable=ApellidoVar, state=tk.DISABLED, relief="solid")
    Apellido.place(x=340, y=200)

    Codigot = Label(PrestamoS, text="Codigo", font=("Helvetica", 10), bg="#008f4c")
    Codigot.place(x=30, y=240)
    Codigo = Entry(PrestamoS, font=("Helvetica", 11), width=15, textvariable=CodigoVar, state=tk.DISABLED, relief="solid")
    Codigo.place(x=106, y=240)

    Programat = Label(PrestamoS, text="Programa", font=("Helvetica", 10), bg="#008f4c")
    Programat.place(x=260, y=240)
    Programa = Entry(PrestamoS, font=("Helvetica", 11), width=15, textvariable=ProgramaVar, state=tk.DISABLED, relief="solid", bg="gray")
    Programa.place(x=340, y=240)

    noved = Label(PrestamoS, text="Novedades", font=("Helvetica", 10), bg="#008f4c")
    noved.place(x=30, y=310)

    frames = Frame(PrestamoS, width=192, height=82, bg="black")
    frames.place(x=105, y=279)

    class TextScrollCombo(ttk.Frame):
        def __init__(self, *args, **kwargs):

            super().__init__(*args, **kwargs)
        # ensure a consistent GUI size
            self.grid_propagate(False)
        # implement stretchability
            self.grid_rowconfigure(0, weight=1)
            self.grid_columnconfigure(0, weight=1)
        # create a Text widget
            self.txt = tkinter.Text(self)
            self.txt.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
        # create a Scrollbar and associate it with txt
            scrollb = ttk.Scrollbar(self, command=self.txt.yview)
            scrollb.grid(row=0, column=1, sticky='nsew')
            self.txt['yscrollcommand'] = scrollb.set

    combot = TextScrollCombo(PrestamoS)
    combot.config(width=190, height=80)
    combot.txt.config(font=("consolas", 12), undo=True, wrap='word')
    combot.txt.config(borderwidth=0, relief="solid")
    combot.place(x=106, y=280)
    '''''+++++++++++++++++++++++++++++COMBOBOX+++++++++++++++++++++++++++++'''

    def prestamo():
        llaVe = combosal()
        combotext = combot.txt.get(1.0, END)
        devolver(llaVe, combotext, Inicio, PrestamoS)
    Busquedasal = ttk.Button(PrestamoS, text='Devolver', command=prestamo, style="C.TButton")
    Busquedasal.place(x=430, y=279)

    def atras():
        PrestamoS.destroy()
        Inicio.update_idletasks
        Inicio.deiconify()
        Inicio.update()

    AtrasButton = ttk.Button(PrestamoS, text='Atras', command=atras, style="C.TButton")
    AtrasButton.place(x=20, y=370)

    PrestamoS.mainloop()
