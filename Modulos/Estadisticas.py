import tkinter
from tkinter import *
from tkinter import ttk
from Modulos.Graficas import *
from Modulos.GraficasEx import *
from Modulos.Reporte import *
def estadisticasmetodo(top):
    def Cerrar():
        if messagebox.askyesno("Cerrar", "¿Desea Cerrar el modulo?"):
            top.deiconify()
            Estadis.destroy()
    Estadis=Toplevel(top)
    Estadis.protocol("WM_DELETE_WINDOW", Cerrar)
    Estadis.geometry("560x530")
    Estadis.resizable(0,0)
    Estadis.iconbitmap("Imagenes/llave.ico")
    Estadis.title("Estadisinar")
    Estadis.configure(bg="#008f4c")
    labelt=Label(Estadis,text="Reportes",font=("Impact",20),bg="#008f4c").place(relx=0.07, rely=0.03)

    comb=ttk.Combobox(Estadis,width=10)
    Tablas=["Docentes","Salas"]
    comb.place(relx=0.07,rely=0.15)
    comb['values'] = Tablas
    comb.current(1)
    labelt1=Label(Estadis,text="tipo de grafica",bg="#008f4c").place(x=128, rely=0.15)
    combo=ttk.Combobox(Estadis,width=10)
    Tablas=["Docentes","Salas"]
    combo.place(x=220,rely=0.15)
    combo['values'] = ["Barras","Pastel"]
    combo.current(1)
    def grF():
        graficas(str(comb.get()),str(combo.get()),Estadis)
    PastelSalas=ttk.Button(Estadis,text="Graficar",command=grF).place(x=330, rely=0.15)
    def grFi():
        graficasEx(str(comb.get()),str(combo.get()))
    def Pdfrep():
        reportepdfs(str(combopd.get()))
    PastelSalas=ttk.Button(Estadis,text="Grafica externa",command=grFi).place(x=410, rely=0.15)
    

    labelt=Label(Estadis,text="_______________________________",font=("Impact",20),bg="#008f4c").place(relx=0.07, rely=0.22)
    text2=Label(Estadis,text="Pdf",bg="#008f4c").place(relx=0.07, rely=0.21)
    combopd=ttk.Combobox(Estadis,width=10)
    Tablas=["Salas"]
    combopd.place(relx=0.11,rely=0.21)
    combopd['values'] = ["Docentes","Prestamos"]
    combopd.current(1)
    ReporteGen=ttk.Button(Estadis,text="Generar PDF",command=Pdfrep).place(relx=0.29, rely=0.21)

    Estadis.mainloop()