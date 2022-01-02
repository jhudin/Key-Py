import tkinter
from tkinter import *
from tkinter import ttk
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
import textwrap

def Onservacionesmetodo(top):
    def wrap(string, lenght=25):
        return '\n'.join(textwrap.wrap(string, lenght))

    def Cerrar():
        if messagebox.askyesno("Cerrar", "¿Desea Cerrar el modulo?"):
            top.deiconify()
            Observ.destroy()
    Observ=Toplevel(top)
    Observ.protocol("WM_DELETE_WINDOW", Cerrar)
    Observ.resizable(0, 0)
    Observ.iconbitmap("Imagenes/llave.ico")
    Observ.title("Observaciones")
    Observ.configure(bg="#008f4c")
    comb=ttk.Combobox(Observ)
    Tablas=["Docentes","Salas"]
    comb.place(x=70,y=40)
    comb['values'] = Tablas
    

    s = ttk.Style()
    s.configure("mystyle.Treeview", rowheight=40) # Modify the font of the body
    TablaDev = ScrolledTreeView(Observ,style="mystyle.Treeview")
    TablaDev.pack()
    TablaDev.configure(columns="Col1 Col2 Col3")
    # build_treeview_support starting.
    TablaDev.heading("#0", text="    Fecha")
    dato = conexionBd('root', 'llave')
    conect = mysql.connector.connect(**dato)
    cursor = conect.cursor()
    cursor.execute('SELECT * FROM `registro_prestamos` ')
    llavesR = cursor.fetchall()
    for row in llavesR:
        TablaDev.insert("", 'end', text=(str(row[0])),
                                values=(str(row[1]),str(row[5]),wrap(str(row[7]))))
    cursor.close()
    conect.close()
    TablaDev.heading("#0", anchor="w")
    TablaDev.column("#0", width="70", minwidth="80",
                            stretch="1", anchor="w")
    TablaDev.heading("Col1", text="Hora")
    TablaDev.heading("Col1", anchor="w")
    TablaDev.column("Col1", width="120", minwidth="116",
                            stretch="1", anchor="w")
    TablaDev.heading("Col2", text="Docente")
    TablaDev.heading("Col2", anchor="w")
    TablaDev.column("Col2", width="102", minwidth="101",
                            stretch="1", anchor="w")
    TablaDev.heading("Col3", text="Novedades")
    TablaDev.heading("Col3", anchor="w")
    TablaDev.column("Col3",stretch=True, anchor="w", )
    Observ.mainloop()
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