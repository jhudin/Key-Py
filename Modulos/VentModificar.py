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
def modifvent(tab,codi,Estadis):
    ventm=Toplevel(Estadis)
    ventm.config(background="#008f4c")
    def Cerrar():
        if messagebox.askyesno("Cerrar", "¿Desea Cerrar el modulo?"):
            Estadis.deiconify()
            ventm.destroy()
    ventm.protocol("WM_DELETE_WINDOW", Cerrar)
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
            cursor.execute("""UPDATE llaves SET  Nombre_llave='%s',N_Sala='%s',Bloque='%s' WHERE codigo_llave='%s' """ % (nombr.get().lower(),
                                                                                                                            nsal.get().lower(),
                                                                                                                            comb.get().lower(),codi.lower()))
            conect.commit()
            try:
                messagebox.showinfo("Completado", "Se ha Actualizado corectamente")
                ventm.destroy()
                Estadis.deiconify()
            except ImportError:
                messagebox.showerror("Error", "Error en la Actualizacion")
        elif(tab=="Docentes"):
            dato = conexionBd('root', 'llave')
            conect = mysql.connector.connect(**dato)
            cursor = conect.cursor()
            nombrecom=nombd.get()+" "+apelld.get()
            cursor.execute("""UPDATE docentes SET  programa='%s',Nombre_docente='%s'  WHERE Identificacion_docente='%s' """ %(comb1.get().lower(), nombrecom.lower(),codi.lower()))
            conect.commit()
            try:
                messagebox.showinfo("Completado", "Se ha Actualizado corectamente")
                ventm.destroy()
                Estadis.deiconify()
            except ImportError:
                messagebox.showerror("Error", "Error en la Actualizacion")
    if(tab=="Salas"):
        dato = conexionBd('root', 'llave')
        conect = mysql.connector.connect(**dato)
        cursor = conect.cursor()
        cursor.execute("""SELECT * FROM llaves WHERE  codigo_llave='%s'""" % (codi.lower()))
        llavesR = cursor.fetchall()
        combv=str
        for row in llavesR:
            nombr.set(str(row[1]))
            cod.set(str(row[0]))
            nsal.set(str(row[2]))
            combv=(str(row[3]))
            print(row[1])
        cursor.close()
        conect.close()
        frame2 = tk.Frame(ventm,background="#008f4c")
        frame2.pack()
        Label1=tk.Label(frame2,text="Nombre Sala",background="#008f4c")
        Label1.grid(row=0,column=0,sticky="w",pady=5,padx=5)
        Label1t=tk.Entry(frame2,text=nombr,textvariable=nombr)
        Label1t.grid(row=0,column=1,sticky="w",pady=5,padx=5)

        Label2=tk.Label(frame2,text="Codigo Sala",background="#008f4c")
        Label2.grid(row=0,column=3,sticky="w",pady=5,padx=5)
        Label2t=tk.Entry(frame2,text=cod,textvariable=cod)
        Label2t.grid(row=0,column=4,sticky="w",pady=5,padx=5)

        Label3=tk.Label(frame2,text="Numero de Sala",background="#008f4c")
        Label3.grid(row=1,column=0,sticky="w",pady=5,padx=5)
        Label3t=tk.Entry(frame2,text=nsal,textvariable=nsal)
        Label3t.grid(row=1,column=1,sticky="w",pady=5,padx=5)

        
        Tablas=["A","B","C","D","E","F"]
        i=0
        currentval=0
        print(combv)
        for i in range(len(Tablas)):
            if combv==Tablas[i].lower():
                currentval=i
        comb=ttk.Combobox(frame2,width=10)
        comb.grid(row=1,column=4,sticky="w",pady=5,padx=5)
        comb['values'] = Tablas
        comb.current(currentval)
        Label4t=tk.Label(frame2,text="Bloque",background="#008f4c")
        Label4t.grid(row=1,column=3,sticky="w",pady=5,padx=5)
        Enviar=ttk.Button(ventm,text="Enviar",command=agregarbd)
        Enviar.pack()
    elif(tab=="Docentes"):
        dato = conexionBd('root', 'llave')
        conect = mysql.connector.connect(**dato)
        cursor = conect.cursor()
        cursor.execute("""SELECT * FROM docentes WHERE  Identificacion_docente='%s'""" % (codi.lower()))
        llavesR = cursor.fetchall()
        nombc=str
        combval=str
        for row in llavesR:
            nombc=(str(row[1]))
            id.set(str(row[2]))
            combval=(str(row[0]))
        nombreapell = nombc.split()
        if(len(nombreapell)==4):
            nombd.set(nombreapell[0]+" "+nombreapell[1])
            apelld.set(nombreapell[2]+" "+nombreapell[3])
        elif(len(nombreapell)==3):
            nombd.set(nombreapell[0])
            apelld.set(nombreapell[1]+" "+nombreapell[2])
        else:
            nombd.set(nombreapell[0])
            apelld.set(nombreapell[1])
        cursor.close()
        conect.close()
        frame2 = tk.Frame(ventm,background="#008f4c")
        frame2.pack()
        Label1=tk.Label(frame2,text="Nombre",background="#008f4c")
        Label1.grid(row=0,column=0,sticky="w",pady=5,padx=5)
        Label1t=tk.Entry(frame2,text=nombd,textvariable=nombd)
        Label1t.grid(row=0,column=1,sticky="w",pady=5,padx=5)
        Label2=tk.Label(frame2,text="Apellido",background="#008f4c")
        Label2.grid(row=0,column=3,sticky="w",pady=5,padx=5)
        Label2t=tk.Entry(frame2,text=apelld,textvariable=apelld)
        Label2t.grid(row=0,column=4,sticky="w",pady=5,padx=5)

        Label3=tk.Label(frame2,text="ID",background="#008f4c")
        Label3.grid(row=1,column=0,sticky="w",pady=5,padx=5)
        Label3t=tk.Entry(frame2,text=id,textvariable=id)
        Label3t.grid(row=1,column=1,sticky="w",pady=5,padx=5)

        
        Tablas=["sistemas","zootecnia","contaduria","administración"]
        i=0
        currentval=0
        for i in range(len(Tablas)):
            if combval==Tablas[i].lower():
                currentval=i
        comb1=ttk.Combobox(frame2,width=10)
        comb1.grid(row=1,column=4,sticky="w",pady=5,padx=5)
        comb1['values'] = Tablas
        comb1.current(currentval)
        Label4t=tk.Label(frame2,text="Programa",background="#008f4c")
        Label4t.grid(row=1,column=3,sticky="w",pady=5,padx=5)
        Enviar=ttk.Button(ventm,text="Enviar",command=agregarbd)
        Enviar.pack()
    ventm.mainloop()