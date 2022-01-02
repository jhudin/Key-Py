import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt
from Modulos.Conexion import *
import mysql.connector
import tkinter
from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import *
import matplotlib, numpy, sys
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as Tk
def graficas(tab,Estadis,top):
    #sala
    comb=ttk.Combobox()
    nombr=StringVar()
    cod=StringVar()
    nsal=StringVar()
    #docente
    comb1=ttk.Combobox()
    nombd=StringVar()
    apelld=StringVar()
    id=StringVar()
    def agregarbd():
        if(tab=="Salas"):
            dato = conexionBd('root', 'llave')
            conect = mysql.connector.connect(**dato)
            cursor = conect.cursor()
            
            valores = "INSERT INTO `llaves`(`codigo_llave`, `Nombre_llave`, `N_Sala`, `Bloque`) VALUES(%s,%s,%s,%s)"
            cursor.execute(valores, (cod.get().lower(),
                                     nombr.get().lower(),
                                     nsal.get().lower(),
                                     comb.get().lower()))
            conect.commit()
            try:
                messagebox.showinfo("Completado", "Se ha Almacenado corectamente")
                Estadis.destroy()
                top.deiconify()
            except ImportError:
                messagebox.showerror("Error", "Error en el almcenamiento")
        elif(tab=="Docentes"):
            dato = conexionBd('root', 'llave')
            conect = mysql.connector.connect(**dato)
            cursor = conect.cursor()
            nombrecom=nombd.get()+" "+apelld.get()
            valores = "INSERT INTO `docentes`(`programa`, `Nombre_docente`, `Identificacion_docente`) VALUES(%s,%s,%s)"
            cursor.execute(valores, (comb1.get().lower(),
                                     nombrecom.lower(),
                                     id.get().lower()))
            conect.commit()
            try:
                messagebox.showinfo("Completado", "Se ha Almacenado corectamente")
                Estadis.destroy()
                top.deiconify()
            except ImportError:
                messagebox.showerror("Error", "Error en el almcenamiento")
    if(tab=="Salas"):
        frame2 = tk.Frame(Estadis,background="#008f4c")
        frame2.place(relx=.073, rely=.5)
        Label1=tk.Label(frame2,text="Nombre Sala",background="#008f4c")
        Label1.grid(row=0,column=0,sticky="w",pady=5,padx=5)
        Label1t=tk.Entry(frame2,textvariable=nombr)
        Label1t.grid(row=0,column=1,sticky="w",pady=5,padx=5)

        Label2=tk.Label(frame2,text="Codigo Sala",background="#008f4c")
        Label2.grid(row=0,column=3,sticky="w",pady=5,padx=5)
        Label2t=tk.Entry(frame2,textvariable=cod)
        Label2t.grid(row=0,column=4,sticky="w",pady=5,padx=5)

        Label3=tk.Label(frame2,text="Numero de Sala",background="#008f4c")
        Label3.grid(row=1,column=0,sticky="w",pady=5,padx=5)
        Label3t=tk.Entry(frame2,textvariable=nsal)
        Label3t.grid(row=1,column=1,sticky="w",pady=5,padx=5)

        
        Tablas=["A","B","C","D","E","F"]
        comb=ttk.Combobox(frame2,width=10)
        comb.grid(row=1,column=4,sticky="w",pady=5,padx=5)
        comb['values'] = Tablas
        comb.current(1)
        Label4t=tk.Label(frame2,text="Bloque",background="#008f4c")
        Label4t.grid(row=1,column=3,sticky="w",pady=5,padx=5)

        Enviar=ttk.Button(Estadis,text="Enviar",command=agregarbd)
        Enviar.place(relx=.4,rely=.85)

    elif(tab=="Docentes"):
        frame2 = tk.Frame(Estadis,background="#008f4c")
        frame2.place(relx=.073, rely=.5)
        Label1=tk.Label(frame2,text="Nombre",background="#008f4c")
        Label1.grid(row=0,column=0,sticky="w",pady=5,padx=5)
        Label1t=tk.Entry(frame2,textvariable=nombd)
        Label1t.grid(row=0,column=1,sticky="w",pady=5,padx=5)

        Label2=tk.Label(frame2,text="Apellido",background="#008f4c")
        Label2.grid(row=0,column=3,sticky="w",pady=5,padx=5)
        Label2t=tk.Entry(frame2,textvariable=apelld)
        Label2t.grid(row=0,column=4,sticky="w",pady=5,padx=5)

        Label3=tk.Label(frame2,text="ID",background="#008f4c")
        Label3.grid(row=1,column=0,sticky="w",pady=5,padx=5)
        Label3t=tk.Entry(frame2,textvariable=id)
        Label3t.grid(row=1,column=1,sticky="w",pady=5,padx=5)

        
        Tablas=["sistemas","zootecnia","contaduria","administración"]
        comb1=ttk.Combobox(frame2,width=10)
        comb1.grid(row=1,column=4,sticky="w",pady=5,padx=5)
        comb1['values'] = Tablas
        comb1.current(1)
        Label4t=tk.Label(frame2,text="Programa",background="#008f4c")
        Label4t.grid(row=1,column=3,sticky="w",pady=5,padx=5)

        Enviar=ttk.Button(Estadis,text="Enviar",command=agregarbd)
        Enviar.place(relx=.4,rely=.85)
        



