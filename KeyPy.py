# -*- coding: utf-8 -*-
from tkinter import *
from PIL import *
from tkinter import ttk
from tkinter import messagebox
from Modulos.PrestamoGUI import *
from Modulos.LoginAdmin import *
import mysql.connector
from Modulos.comboboxauto import *
from Modulos.Tabla import *
from Modulos.devolucion import *
import matplotlib.pyplot as plt
import tkinter.font as tkFont
import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt
from Modulos.Conexion import *
import mysql.connector
from matplotlib.backends.backend_tkagg import *
import matplotlib, numpy, sys
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import mysql.connector
from tkinter import messagebox
from arrow import utcnow, get
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, mm
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib.colors import black, deepskyblue, white
from reportlab.pdfgen import canvas
from tkinter import filedialog
import textwrap
import hashlib

def VentanaPrin():
    def Cerrar():
        if messagebox.askyesno("Cerrar", "¿Desea Cerrar la Aplicacion?"):
            Inicio.destroy()
    Inicio = Tk()
    Inicio.title("KeyPy")
    Inicio.geometry("580x400+440+170")
    Inicio.resizable(0, 0)
    Inicio.protocol("WM_DELETE_WINDOW", Cerrar)
    Inicio.attributes("-alpha", 0.99)
    Inicio.config(bg="#008f4c")
    Inicio.iconbitmap("Imagenes/llave.ico")
    log = PhotoImage(file="./Imagenes/logo.png")
    fondo = Label(Inicio, image=log)
    fondo.pack()
    Inicio.wm_attributes("-topmost", True)
    logo = Frame(Inicio)
    fondoimg = PhotoImage(file="./Imagenes/udecLog.png")
    fondoverd = Label(Inicio, image=fondoimg,bg="#008f4c")
    fondoverd.place(relx=.35,rely=.20)

    def actualizar():
        Inicio.destroy()
        VentanaPrin()
    logo.pack(padx=0, pady=0)
    dato = conexionBd('root', 'llave')
    conect = mysql.connector.connect(**dato)
    cursor = conect.cursor()
    cursor.execute('SELECT * FROM `llaves` ')
    llavesR = cursor.fetchall()
    SalasN = []
    global contador
    for row in llavesR:
        strsal = str(str(row[1]))
        SalasN.append(strsal)
    cursor.close()
    conect.close()
    '''''+++++++++++++++++++++++++++++COMBOBOX+++++++++++++++++++++++++++++'''
    combo = Combobox()
    ComboboxMostPrin(SalasN, Inicio, 340, 216, 447, 215, "Buscar", 11, combo)
    '''''++++++++++++++++++++++++++++++TABLA++++++++++++++++++++++++++++++'''
    TablaRep(Inicio)

    def PrestamoM():
        Inicio.withdraw()
        Prestamometod(Inicio)
    def devolucionM():
        Inicio.withdraw()
        devolucionmetod(Inicio)
    PrestaImage = PhotoImage(file="./Imagenes/Prestamo.png")
    Prestamo = ttk.Button(Inicio, text="Préstamo", command=PrestamoM)
    Prestamo.configure(compound="top")
    Prestamo.configure(image=PrestaImage)
    Prestamo.place(x=120, y=120)
    DeboImage = PhotoImage(file="./Imagenes/Debolucion.png")
    Devolucion = ttk.Button(Inicio, text="Devolución", command=devolucionM)
    Devolucion.configure(compound="top")
    Devolucion.configure(image=DeboImage)
    Devolucion.place(x=360, y=120)

    def Admin():
        Inicio.withdraw()
        Login(Inicio)
    menu_bar=Menu(Inicio)
    menuarchivo = Menu(menu_bar, tearoff=0)
    menuarchivo.add_command(label="Inicio de Sesión", command=Admin)
    menuarchivo.add_separator()
    menuarchivo.add_command(label="Salir", command=Cerrar)
    menu_bar.add_cascade(label="Administrador", menu=menuarchivo)
    Inicio.config(menu=menu_bar)
    Actua = ttk.Button(Inicio, text="Actualizar", command=actualizar)
    Actua.place(x=23, y=215)
    Inicio.mainloop()


VentanaPrin()

