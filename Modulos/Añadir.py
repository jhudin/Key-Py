import tkinter
from tkinter import *
from tkinter import ttk
from Modulos.AñadirReg import *
from Modulos.GraficasEx import *
from Modulos.Reporte import *
def Agregarmetod(top):
    def Cerrar():
        if messagebox.askyesno("Cerrar", "¿Desea Cerrar el modulo?"):
            top.deiconify()
            Estadis.destroy()
    Estadis=Toplevel(top)
    Estadis.protocol("WM_DELETE_WINDOW", Cerrar)
    Estadis.geometry("560x230")
    Estadis.resizable(0,0)
    Estadis.iconbitmap("Imagenes/llave.ico")
    Estadis.title("Añadir")
    Estadis.configure(bg="#008f4c")
    labelt=Label(Estadis,text="Añadir",font=("Impact",20),bg="#008f4c").place(relx=0.07, rely=0.03)

    comb=ttk.Combobox(Estadis,width=10)
    Tablas=["Docentes","Salas"]
    comb.place(x=120,rely=0.2)
    comb['values'] = Tablas
    comb.current(1)
    labelt1=Label(Estadis,text="Añadir",bg="#008f4c").place(relx=0.07, rely=0.2)
    def grF():
        graficas(str(comb.get()),Estadis,top)
    PastelSalas=ttk.Button(Estadis,text="Añadir",command=grF).place(x=230, rely=0.2)
    
    labelt=Label(Estadis,text="_______________________________",font=("Impact",20),bg="#008f4c").place(relx=0.07, rely=0.35)

    Estadis.mainloop()