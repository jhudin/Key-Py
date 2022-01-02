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

def Elimi(tab,Modif,top):
    def modifcicarme():
        if(tab=="Docentes"):
            curItem = TablaDev.item(TablaDev.focus())
            codig = curItem['text']
            if messagebox.askyesno("Eliminar","Desea eliminar el registro con el correspondiente a el codigo "+codig):
                conect = mysql.connector.connect(**dato)
                cursor = conect.cursor()
                cursor.execute("""DELETE FROM docentes  WHERE  Identificacion_docente='%s'""" % (codig.lower()))
                conect.commit()
                try:
                    messagebox.showinfo("Completado",
                                        "Se ha eliminado el registro ")
                except ImportError:
                    messagebox.showerror("Error",
                                         "No se eliminado el registro")
                cursor.close()
                conect.close()
        elif(tab=="Salas"):
            curItem = TablaDev.item(TablaDev.focus())
            codig = curItem['text']
            if messagebox.askyesno("Eliminar","Desea eliminar el registro con el correspondiente a el codigo "+codig):
                conect = mysql.connector.connect(**dato)
                cursor = conect.cursor()
                cursor.execute("""DELETE FROM llaves  WHERE  codigo_llave='%s'""" % (codig.lower()))
                conect.commit()
                try:
                    messagebox.showinfo("Completado",
                                        "Se ha eliminado el registro ")
                except ImportError:
                    messagebox.showerror("Error",
                                         "No se eliminado el registro")
                cursor.close()
                conect.close()

    valor=False
    Modificb=Button(Modif,text="Eliminar",command=modifcicarme).place(relx=.4,rely=.93)
    if(tab=="Docentes"):
        if(valor):
            TablaDev.destroy()
            valor=False
        print("tab =="+tab)
        TablaDev = ScrolledTreeView(Modif)
        TablaDev.place(relx=0.07, rely=0.358,
                            relheight=0.5, relwidth=0.9)
        TablaDev.configure(columns="Col1 Col2")
        # build_treeview_support starting.
        TablaDev.heading("#0", text="    ID")
        dato = conexionBd('root', 'llave')
        conect = mysql.connector.connect(**dato)
        cursor = conect.cursor()
        cursor.execute('SELECT * FROM `docentes` ')
        llavesR = cursor.fetchall()
        for row in llavesR:
            TablaDev.insert("", 'end', text=(str(row[2])),
                                    values=(str(row[1]),str(row[0])))
        cursor.close()
        conect.close()
        TablaDev.heading("#0", anchor="w")
        TablaDev.column("#0", width="70", minwidth="80",
                                stretch="1", anchor="w")
        TablaDev.heading("Col1", text="Nombre")
        TablaDev.heading("Col1", anchor="w")
        TablaDev.column("Col1", width="120", minwidth="116",
                                stretch="1", anchor="w")
        TablaDev.heading("Col2", text="Programa")
        TablaDev.heading("Col2", anchor="w")
        TablaDev.column("Col2", width="102", minwidth="101",
                                stretch="1", anchor="w")
        valor=True
    elif(tab=="Salas"):
        if(valor):
            TablaDev.destroy()
            valor=False
        print("tab =="+tab)
        TablaDev = ScrolledTreeView(Modif)
        TablaDev.place(relx=0.07, rely=0.358,
                            relheight=0.5, relwidth=0.9)
        TablaDev.configure(columns="Col1 Col2 Col3")
        # build_treeview_support starting.
        TablaDev.heading("#0", text="Codigo")
        dato = conexionBd('root', 'llave')
        conect = mysql.connector.connect(**dato)
        cursor = conect.cursor()
        cursor.execute('SELECT * FROM `llaves` ')
        llavesR = cursor.fetchall()
        for row in llavesR:
            TablaDev.insert("", 'end', text=(str(row[0])),
                                    values=(str(row[1]),str(row[2]),str(row[3])))
        cursor.close()
        conect.close()
        TablaDev.heading("#0", anchor="w")
        TablaDev.column("#0", width="70", minwidth="80",
                                stretch="1", anchor="w")
        TablaDev.heading("Col1", text="Nombre")
        TablaDev.heading("Col1", anchor="w")
        TablaDev.column("Col1", width="102", minwidth="101",
                                stretch="1", anchor="w")
        TablaDev.heading("Col2", text="N Sala")
        TablaDev.heading("Col2", anchor="w")
        TablaDev.column("Col2", width="102", minwidth="101",
                                stretch="1", anchor="w")
        TablaDev.heading("Col3", text="Bloque")
        TablaDev.heading("Col3", anchor="w")
        TablaDev.column("Col3", width="102", minwidth="101",
                                stretch="1", anchor="w")
        valor=True
class AutoScroll(object):
    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master,
                                orient='vertical',
                                command=self.yview)
        except ImportError:
            pass
        hsb = ttk.Scrollbar(master,
                            orient='horizontal',
                            command=self.xview)

        # self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except ImportError:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except ImportError:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master (taken from ScrolledText.py)
        methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
            | tk.Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>',
                        lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>',
                        lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledTreeView(AutoScroll, ttk.Treeview):
    '''A standard ttk Treeview widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        ttk.Treeview.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

import platform

def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>',
                        lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>',
                        lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>',
                        lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>',
                        lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>',
                        lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>',
                        lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1 * int(event.delta / 120), 'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1 * int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1 * int(event.delta / 120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1 * int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')