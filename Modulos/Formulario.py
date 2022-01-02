from tkinter import ttk
from tkinter import *
import tkinter
import mysql.connector
from Modulos.Conexion import *
from tkinter import messagebox
import time
import hashlib

def Formreg(Inicio,LoginAdminist):
    def Cerrar():
        if messagebox.askyesno("Cerrar", "¿Desea Cerrar el modulo?"):
            Formulario.destroy()
            LoginAdminist.deiconify()
    Formulario=Toplevel(Inicio)
    Formulario.title('Formulario')
    Formulario.configure(bg="#008f4c")
    Formulario.geometry('310x340+200+200')
    Formulario.resizable(0,0)
    Formulario.protocol("WM_DELETE_WINDOW", Cerrar)
    Formulario.iconbitmap("Imagenes/llave.ico")
    miFrame=Frame(Formulario,width=1200,height=600,bg="#008f4c")
    miFrame.pack()
    miFrame.place(x=10,y=40)
    idregistro=StringVar();
    idregistro.set("")
    Apellidoregistro=StringVar();
    Apellidoregistro.set("")
    Nombreregistro=StringVar();
    Nombreregistro.set("")
    usuarioregistro=StringVar();
    usuarioregistro.set("")
    claveregistro=StringVar();
    claveregistro.set("")
    claveregistroconfirm=StringVar()
    claveregistroconfirm.set("")
    claveregistroAdmin=StringVar()
    claveregistroAdmin.set("")
    cantusutk=StringVar()
    cantusutk.set("")
    TipoUsuario=StringVar()
    TipoUsuario.set("Administrador")
    cuadroNombre=Entry(miFrame,textvariable=Nombreregistro)
    cuadroNombre.grid(row=0,column=1)
    cuadroNombre.config(justify="center")
    cuadroApellido=Entry(miFrame,textvariable=Apellidoregistro)
    cuadroApellido.grid(row=1,column=1)
    cuadroApellido.config(justify="center")
    cuadroCorreo=Entry(miFrame,textvariable=idregistro)
    cuadroCorreo.grid(row=2,column=1)
    cuadroCorreo.config(justify="center")
    cuadroUsuario=Entry(miFrame,textvariable=usuarioregistro)
    cuadroUsuario.grid(row=4,column=1)
    cuadroUsuario.config(justify="center")
    cuadroContraseña=Entry(miFrame,textvariable=claveregistro)
    cuadroContraseña.grid(row=5,column=1)
    cuadroContraseña.config(justify="center",show="*")
    nombrelabel=Label(miFrame,text="Nombre ",bg="#008f4c",fg="Black",font=("Helvetica", 11))
    nombrelabel.grid(row=0,column=0,sticky="w",pady=5)
    aperllidolabel=Label(miFrame,text="Apellido ",bg="#008f4c",fg="Black",font=("Helvetica", 11))
    aperllidolabel.grid(row=1,column=0,sticky="w",pady=5)
    correolabel=Label(miFrame,text="ID ",bg="#008f4c",fg="Black",font=("Helvetica", 11))
    correolabel.grid(row=2,column=0,sticky="w",pady=5)
    Usuariolabel=Label(miFrame,text="Usuario ",bg="#008f4c",fg="Black",font=("Helvetica", 11))
    Usuariolabel.grid(row=4,column=0,sticky="w",pady=5)

    cl=Label(miFrame,text="Clave ",bg="#008f4c",fg="Black",font=("Helvetica", 11))
    cl.grid(row=5,column=0,sticky="w",pady=5)
    cl2=Label(miFrame,text="Confirmar Clave ",bg="#008f4c",fg="Black",font=("Helvetica", 11))
    cl2.grid(row=6,column=0,sticky="w",pady=5)

    cuadroContraseña=Entry(miFrame,textvariable=claveregistroconfirm)
    cuadroContraseña.grid(row=6,column=1)
    cuadroContraseña.config(justify="center",show="*")

    cla=Label(miFrame,text="Clave Admin",bg="#008f4c",fg="Black",font=("Helvetica", 11))
    cla.grid(row=7,column=0,sticky="w",pady=5)
    cuadroContraseñaAd=Entry(miFrame,textvariable=claveregistroAdmin)
    cuadroContraseñaAd.grid(row=7,column=1)
    cuadroContraseñaAd.config(justify="center",show="*")
    def registr(id,usu,nom,ape,usut,cl):
        print("hola")
        n=hashlib.md5()
        n.update((cl).encode('utf-8'))
        clave=n.hexdigest()
        dato = conexionBd('root', 'llave')
        conect = mysql.connector.connect(**dato)
        cursor = conect.cursor()
        valores = "INSERT INTO usuarioadmin(`Identificacionusu`, `usuario_adm`, `Nombre_usu`, `Apellido_usu`, `Tipo_usu`, `Contraseña_usu`) VALUES(%s,%s,%s,%s,%s,%s)"
        cursor.execute(valores, (id.lower(), usu.lower(),
                                   nom.lower(),
                                    ape.lower(),
                                    usut.lower(),
                                    clave.lower()))
        conect.commit()
        try:
            messagebox.showinfo("Completado", "Se ha realizado el registro")
            Formulario.destroy()
            LoginAdminist.deiconify()
        except ImportError:
            messagebox.showerror("Error", "Fallo en registro")
    def Enviarinf():
        dato = conexionBd('root', 'llave')
        conect = mysql.connector.connect(**dato)
        cursor = conect.cursor()
        cursor.execute('SELECT * FROM `usuarioadmin`')
        llavesR = cursor.fetchall()
        global valor
        valor=0
        for row in llavesR:
            if (str(row[5]) == str(claveregistroAdmin.get())):
                valor=1
        cursor.close()
        conect.close()
        print(valor)
        if valor==1:
            registr(idregistro.get(),usuarioregistro.get(),
                     Nombreregistro.get(),
                     Apellidoregistro.get(),
                     TipoUsuario.get(),
                     claveregistro.get()
                    )
        else: messagebox.showerror("Error","Contraseñade administrador icorrecta")
    
    
    envi=Button(Formulario,text="Registrar",font=("Consolas",14),command=Enviarinf).place(relx=.3,rely=0.9)

    Formulario.mainloop()



