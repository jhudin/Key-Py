from tkinter import *
from PIL import *
import tkinter
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from Modulos.Conexion import *
import mysql.connector
from Modulos.comboboxauto import *
import time
from Modulos.Tabla import *
import sys


def Prestamometod(Inicio):

    def Cerrar():
        if messagebox.askyesno("Cerrar", "¿Desea Cerrar el modulo?"):
            PrestamoS.destroy()
            Inicio.deiconify()

    PrestamoS = tk.Toplevel(Inicio)
    PrestamoS.title("Prestamo")
    PrestamoS.resizable(0, 0)
    PrestamoS.geometry("580x400+440+170")
    PrestamoS.wm_attributes("-topmost", True)
    PrestamoS.config(bg="#008f4c")
    PrestamoS.protocol("WM_DELETE_WINDOW", Cerrar)
    PrestamoS.attributes("-alpha", 0.97)
    PrestamoS.iconbitmap("Imagenes/llave.ico")

    def docenteinfo():
        dato = conexionBd('root', 'llave')
        conect = mysql.connector.connect(**dato)
        cursor = conect.cursor()
        cursor.execute('SELECT * FROM `prestamo` ')
        llavesR = cursor.fetchall()
        docentellav=False
        global contador
        for row in llavesR:
            if(CódigoText.get()==str(rowu[3])):
                docentellav = True
        cursor.close()
        conect.close()

        if(CódigoText.get() != "" and docentellav==False):
            dato = conexionBd('root', 'llave')
            conect = mysql.connector.connect(**dato)
            cursor = conect.cursor()
            cursor.execute('SELECT * FROM `docentes` ')
            llavesR = cursor.fetchall()
            Programa = str
            Nombre = str
            comp = False
            for row in llavesR:
                if(int(row[2]) == int(CódigoText.get())):
                    comp = True
                    Programa = str(str(row[0]))
                    Nombre = str(str(row[1]))
            cursor.close()
            conect.close()
            if(comp):
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
                CódigoVar.set(str(CódigoText.get()))
                ProgramaVar.set(Programa)
                PrestamoS.update()
                comp = False
        else:
            messagebox.showerror("Error","El docente ya se encuentra con una llave prestada")
    CódigoText = StringVar()
    nombrecomp = StringVar()
    nombrecomp.set("")
    CódigoText.set("")
    NombreVar = StringVar()
    NombreVar.set("")
    ApellidoVar = StringVar()
    CódigoVar = StringVar()
    ProgramaVar = StringVar()
    log = PhotoImage(file="./Imagenes/logo.png")
    fondo = Label(PrestamoS, image=log)
    fondo.pack()
    fondoimg = PhotoImage(file="./Imagenes/udecLog.png")
    fondoverd = Label(PrestamoS, image=fondoimg,bg="#008f4c")
    fondoverd.place(relx=.35,rely=.20)
    textq = Label(PrestamoS,
                  text="ESCANEAR EL CARNET INSTITUCIONAL",
                  font=("Impact", 20), borderwidth=0,
                  fg="yellow", relief="flat",
                  bg="#008f4c")
    textq.place(x=24, y=80)
    CódigoText1 = Label(PrestamoS, text="Código",
                        font=("Arial", 10),
                        borderwidth=0,
                        relief="flat",
                        bg="#008f4c")
    CódigoText1.place(x=30, y=121)
    Código = Entry(PrestamoS, font=("Helvetica", 11),
                   width=15, textvariable=CódigoText,
                   relief="solid")
    Código.place(x=95, y=121)

    style = ttk.Style()
    style.map("C.TButton",
              foreground=[('pressed', 'red'),
                          ('active', 'green')],
              background=[('pressed', '!disabled', 'black'),
                          ('active', 'deepskyblue')])

    EnviarCod = ttk.Button(PrestamoS, text="Enviar",
                           command=docenteinfo, style="C.TButton")
    EnviarCod.place(x=260, y=119)
    infodocente = Frame(PrestamoS)
    infodocente.place(x=30, y=200)

    Nombret = Label(PrestamoS, text="Nombre",
                    font=("Helvetica", 10), bg="#008f4c")
    Nombret.place(x=30, y=200)
    Nombre = Entry(PrestamoS, font=("Helvetica", 11),
                   width=15, textvariable=NombreVar,
                   state=tk.DISABLED, relief="solid")
    Nombre.place(x=95, y=200)

    Apellidot = Label(PrestamoS, text="Apellido",
                      font=("Helvetica", 10),
                      bg="#008f4c")
    Apellidot.place(x=260, y=200)
    Apellido = Entry(PrestamoS, font=("Helvetica", 11),
                     width=15, textvariable=ApellidoVar,
                     state=tk.DISABLED, relief="solid")
    Apellido.place(x=340, y=200)

    Códigot = Label(PrestamoS, text="Código",
                    font=("Helvetica", 10),
                    bg="#008f4c")
    Códigot.place(x=30, y=240)
    Código = Entry(PrestamoS, font=("Helvetica", 11),
                   width=15, textvariable=CódigoVar,
                   state=tk.DISABLED, relief="solid")
    Código.place(x=95, y=240)

    Programat = Label(PrestamoS, text="Programa",
                      font=("Helvetica", 10), bg="#008f4c")
    Programat.place(x=260, y=240)
    Programa = Entry(PrestamoS, font=("Helvetica", 11),
                     width=15, textvariable=ProgramaVar,
                     state=tk.DISABLED, relief="solid")
    Programa.place(x=340, y=240)

    dato = conexionBd('root', 'llave')
    conect = mysql.connector.connect(**dato)
    cursor = conect.cursor()
    cursor.execute('SELECT * FROM `llaves` ')
    llavesR = cursor.fetchall()
    SalasN = []
    valor = bool
    valor = False
    global contador
    for row in llavesR:
        cursor1 = conect.cursor()
        cursor1.execute('SELECT * FROM `prestamo` ')
        llavesU = cursor1.fetchall()
        for rowu in llavesU:
            if(str(row[0]) == str(rowu[6])):
                valor = True
        if not(valor):
            strsal = str(str(row[1]))
            SalasN.append(strsal)
        valor = False
    cursor.close()
    conect.close()
    '''''+++++++++++++++++++++++++++++COMBOBOX+++++++++++++++++++++++++++++'''
    ComboboxMost(SalasN, PrestamoS, 260, 280, 140, 279, "Prestar", 11)
    hoy = str(time.strftime("%d/%m/%Y"))
    horaact = str(time.strftime("%H:%M"))

    def prestamo():
        llaVe = combosal()
        print(llaVe)
        dato = conexionBd('root', 'llave')
        conect = mysql.connector.connect(**dato)
        cursor = conect.cursor()
        cursor.execute('SELECT * FROM `llaves` ')
        llavesR = cursor.fetchall()
        SalasN = []
        valor = bool
        valor = False
        global contador
        for row in llavesR:
            cursor1 = conect.cursor()
            cursor1.execute('SELECT * FROM llaves')
            llavesU = cursor1.fetchall()
            codllav=str
            for rowu in llavesU:
                if(llaVe== str(rowu[1])):
                    codllav = str(rowu[0])
        cursor.close()
        conect.close()
        if(str(nombrecomp.get()) != ""):
            Prestar(hoy, horaact, CódigoText.get(),nombrecomp.get(),
                    ProgramaVar.get(), codllav,llaVe, Inicio, PrestamoS)
    Busquedasal = ttk.Button(PrestamoS, text='Prestar',
                             command=prestamo, style="C.TButton")
    Busquedasal.place(x=390, y=279)

    def atras():
        PrestamoS.destroy()
        Inicio.deiconify()
        Inicio.update()

    AtrasButton = ttk.Button(PrestamoS, text='Atras',
                             command=atras, style="C.TButton")
    AtrasButton.place(x=30, y=350)

    PrestamoS.mainloop()
