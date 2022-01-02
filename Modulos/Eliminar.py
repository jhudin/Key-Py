import tkinter
from tkinter import *
from tkinter import ttk
from Modulos.Eliminar_metod import *

def Eliminarmetodo(top):
    def Cerrar():
        if messagebox.askyesno("Cerrar", "¿Desea Cerrar el modulo?"):
            top.deiconify()
            Elim.destroy()
    Elim=Toplevel(top)
    Elim.protocol("WM_DELETE_WINDOW", Cerrar)
    Elim.geometry("580x420")
    Elim.resizable(0,0)
    Elim.iconbitmap("Imagenes/llave.ico")
    Elim.title("Eliminar")
    Elim.configure(bg="#008f4c")
    comb=ttk.Combobox(Elim)
    Tablas=["Docentes","Salas"]
    comb.place(x=70,y=40)
    comb['values'] = Tablas
    comb.current(1)
    def grF():
        Elimi(str(comb.get()),Elim,top)
    PastelSalas=ttk.Button(Elim,text="Aceptar",command=grF).place(x=230, y=40)
    labelt=Label(Elim,text="_______________________________",font=("Impact",20),bg="#008f4c").place(relx=0.07,y=80)
    Elim.mainloop()