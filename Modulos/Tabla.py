import tkinter
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from Modulos.Conexion import *
import mysql.connector


class Table(tk.Frame):
    def __init__(self, parent=None, headers=[], height=4, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self._title = tk.Label(self,
                               text="REGISTRO DE LLAVES EN USO",
                               font="Impact")
        self._headers = headers
        self._tree = ttk.Treeview(self,
                                  height=height,
                                  columns=self._headers,
                                  show="headings")
        self._title.pack(side=tk.TOP, fill="x")
        vsb = ttk.Scrollbar(self, orient="vertical",
                            command=self._tree.yview)
        vsb.pack(side='right', fill='y')
        hsb = ttk.Scrollbar(self, orient="horizontal",
                            command=self._tree.xview)
        hsb.pack(side='bottom', fill='x')

        self._tree.configure(xscrollcommand=hsb.set,
                             yscrollcommand=vsb.set)
        self._tree.pack(side="left")

        for header in self._headers:
            self._tree.heading(header, text=header.title())
            self._tree.column(header, stretch=True,
                              width=100,minwidth="100",anchor="center")

    def add_row(self, row):
        self._tree.insert('', 'end', values=row)
        for i, item in enumerate(row):
            col_width = tkFont.Font().measure(item)
            self._tree.column(self._headers[i], width=100,minwidth="100",anchor="center")


def TablaRep(Inicio, parent=None):
    Inicio.focus_set()
    Inicio.grab_set()
    clientes_headers = (u"Fecha",
                        u"Nombre Docente",
                        u"Programa ",
                        u"Hora prestamo",
                        u"Llave prestada"
                        )
    clientes_tab = Table(Inicio, headers=clientes_headers)
    clientes_tab.pack()

    clientes_tab.place(x=24, y=240)

    dato = conexionBd('root', 'llave')
    conect = mysql.connector.connect(**dato)
    cursor = conect.cursor()
    cursor.execute("SELECT `Dia`, `Nombre_docente`, `Programa`,`hora`, `NombSal`  FROM prestamo")
    for row in cursor:
        clientes_tab.add_row(row)
