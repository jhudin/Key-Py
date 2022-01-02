import tkinter
from tkinter import *
from tkinter import ttk
from Modulos.Modificar_metod import *

def Modificarmetodo(top):
    def Cerrar():
        if messagebox.askyesno("Cerrar", "¿Desea Cerrar el modulo?"):
            top.deiconify()
            Modif.destroy()
    Modif=Toplevel(top)
    Modif.protocol("WM_DELETE_WINDOW", Cerrar)
    Modif.geometry("580x420")
    Modif.iconbitmap("Imagenes/llave.ico")
    Modif.title("Modificar")
    Modif.resizable(0,0)
    Modif.configure(bg="#008f4c")
    comb=ttk.Combobox(Modif)
    Tablas=["Docentes","Salas"]
    comb.place(x=70,y=40)
    comb['values'] = Tablas
    comb.current(1)
    def grF():
        modif(str(comb.get()),Modif,top)
    PastelSalas=ttk.Button(Modif,text="Añadir",command=grF).place(x=230, y=40)
    labelt=Label(Modif,text="_______________________________",font=("Impact",20),bg="#008f4c").place(relx=0.07,y=80)
    Modif.mainloop()