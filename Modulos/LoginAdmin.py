from tkinter import *
from PIL import *
import tkinter
from tkinter import ttk
from tkinter import messagebox
from Modulos.Conexion import *
from Modulos.Adminvent import *
from Modulos.Formulario import *
import mysql.connector


def Login(Inicio):
    def Cerrar():
        if messagebox.askyesno("Cerrar", "¿Desea Cerrar la Aplicacion?"):
            Inicio.deiconify()
            LoginAdminist.destroy()
    LoginAdminist = tkinter.Toplevel(Inicio)
    LoginAdminist.title("Inicio Administrador")
    LoginAdminist.geometry("219x210+440+170")
    LoginAdminist.resizable(0, 0)
    LoginAdminist.config(bg="#008f4c")
    LoginAdminist.iconbitmap("Imagenes/llave.ico")
    LoginAdminist.wm_attributes("-topmost", True)
    LoginAdminist.protocol("WM_DELETE_WINDOW", Cerrar)
    
    fondoimg = PhotoImage(file="./Imagenes/udecLog.png")
    fondoverd = Label(LoginAdminist, image=fondoimg,bg="#008f4c")
    fondoverd.place(relx=.35,rely=.20)
    Log = PhotoImage(file="./Imagenes/Keypy3.png")
    fondo = Label(LoginAdminist, image=Log, borderwidth=0,bg="#008f4c")
    fondo.pack()
    UsuarioText = Label(LoginAdminist, text="Usuario", anchor="center",bg="#008f4c")
    UsuarioText.place(x=18, y=95)
    global User
    User = StringVar()
    UsuarioTextEnt = Entry(LoginAdminist, textvariable=User)
    UsuarioTextEnt.place(x=70, y=96)

    ClaveText = Label(LoginAdminist, text="Clave", anchor="center",bg="#008f4c")
    LoginAdminist.attributes("-alpha", 0.97)
    ClaveText.place(x=18, y=125)
    global Clave
    LoginAdminist.focus_force()
    Clave = StringVar()
    ClaveTextEnt = Entry(LoginAdminist, textvariable=Clave)
    ClaveTextEnt.configure(show="*")
    ClaveTextEnt.place(x=70, y=126)

    def ingresar():
        dato = conexionBd('root', 'llave')
        conect = mysql.connector.connect(**dato)
        cursor = conect.cursor()
        cursor.execute('SELECT * FROM `usuarioadmin`')
        llavesR = cursor.fetchall()
        valor=0
        valor1=0
        for row in llavesR:
            if str(row[1]) == str(User.get()):
                clacenorm=str(Clave.get())
                n=hashlib.md5()
                n.update((clacenorm).encode('utf-8'))
                clave=n.hexdigest()
                if (str(row[5]) == clave):
                    valor=1
                    
        if (valor==1):
            if messagebox.askyesno("Ingresar", "¿Continuar?"):
                LoginAdminist.destroy()
                ventanaAdmin((str(row[2])), (str(row[3])),Inicio)
            else:
               Inicio.deiconify()
               LoginAdminist.destroy()
        else:
            messagebox.showerror("Error", "La contraseña /o el usuario es incorrecto")
            
        cursor.close()
        conect.close()
    Ingresar = ttk.Button(LoginAdminist, text="Ingresar", cursor="hand2", command=ingresar)
    Ingresar.place(relx=0.3, rely=0.8, anchor=CENTER)
    def registr():
        LoginAdminist.withdraw()
        Formreg(Inicio,LoginAdminist)
    reg = ttk.Button(LoginAdminist, text="Registrar", cursor="hand2", command=registr)
    reg.place(relx=0.65, rely=0.8, anchor=CENTER)

    LoginAdminist.mainloop()
