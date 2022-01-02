# -*- coding: utf-8 -*-
import sys
from tkinter import *
from PIL import *
import tkinter
from tkinter import ttk
from Modulos.Conexion import *
import mysql.connector
import tkinter as tk
import os.path
from Modulos.Eliminar import *
from Modulos.Modificar import *
from Modulos.Añadir import *
from Modulos.Estadisticas import *
from Modulos.Observaciones import *


def ventanaAdmin(nom_usu, apell_usu, Inicio):
    def vp_start_gui():
        global val, w, root
        global prog_location
        prog_call = sys.argv[0]
        prog_location = os.path.split(prog_call)[0]
        root = tk.Toplevel(Inicio)
        top = Toplevel1(root)
        root.mainloop()
    w = None

    def create_Toplevel1(root, *args, **kwargs):
        '''Starting point when module is imported by another program.'''
        global w, w_win, rt
        global prog_location
        prog_call = sys.argv[0]
        prog_location = os.path.split(prog_call)[0]
        rt = root
        w = tk.Toplevel(Inicio)
        top = Toplevel1(w)

        unknown_support.init(w, top, *args, **kwargs)
        return(w, top)

    def destroy_Toplevel1():
        global w
        w.destroy()
        w = None

    class Toplevel1:
        def __init__(self, top=None):
            top.geometry("800x500")
            top.title("Administrador")
            top.iconbitmap("Imagenes/llave.ico")
            
            def Cerrar():
                if messagebox.askyesno("Regresar", "¿Desea regresar al inicio?"):
                    Inicio.deiconify()
                    top.destroy()
            top.protocol("WM_DELETE_WINDOW", Cerrar)
            top.resizable(0, 0)
            top.configure(background="#008f4c")
            

            self.TablaPrest = ScrolledTreeView(top)
            self.TablaPrest.place(relx=0.04, rely=0.358,
                                  relheight=0.349,
                                  relwidth=0.439)
            self.TablaPrest.configure(columns="Col1 Col2")
            # build_treeview_support starting.
            self.TablaPrest.heading("#0", text="Docente")
            dato = conexionBd('root', 'llave')
            conect = mysql.connector.connect(**dato)
            cursor = conect.cursor()
            cursor.execute('SELECT * FROM `prestamo` ')
            llavesR = cursor.fetchall()
            global contador
            for row in llavesR:
                self.TablaPrest.insert("", 'end', text=(str(row[4])),
                                       values=(str(row[7]),str(row[1])))
            cursor.close()
            conect.close()

            self.TablaPrest.heading("#0", anchor="center")
            self.TablaPrest.column("#0", width="101", minwidth="101",
                                   stretch="1", anchor="center")
            self.TablaPrest.heading("Col1", text="Llave", anchor="center")
            self.TablaPrest.heading("Col1")
            self.TablaPrest.column("Col1", width="101", minwidth="101",
                                   stretch="1", anchor="center")
            self.TablaPrest.heading("Col2", text="Fecha Prestamo", anchor="center")
            self.TablaPrest.heading("Col2")
            self.TablaPrest.column("Col2", width="101", minwidth="101",
                                   stretch="1", anchor="center")


            self.Label1 = tk.Label(top)
            self.Label1.place(relx=0.07, rely=0.05, height=91, width=223)
            self.Label1.configure(background="#008f4c")
            self.Label1.configure(disabledforeground="#a3a3a3")
            self.Label1.configure(foreground="#000000")
            photo_location = os.path.join(prog_location, "keypy3.png")
            global _img0
            _img0 = tk.PhotoImage(file=photo_location)
            self.Label1.configure(image=_img0)
            self.Label1.configure(text='''Label''')

            self.Label212 = tk.Label(top)
            self.Label212.place(relx=0.5, rely=0.15)
            self.Label212.configure(background="#008f4c")
            self.Label212.configure(disabledforeground="#a3a3a3")
            self.Label212.configure(foreground="#000000")
            photo_location1 = os.path.join(prog_location, "udecLog.png")
            global _img1
            _img1 = tk.PhotoImage(file=photo_location1)
            self.Label212.configure(image=_img1)
            self.Label212.configure(text='''Label''')

            def eliminarmet():
                top.withdraw()
                Eliminarmetodo(root)

            def Agregarmet():
                top.withdraw()
                Agregarmetod(root)

            def Modificarmetod():
                top.withdraw()
                Modificarmetodo(root)

            def estadisticasmetod():
                top.withdraw()
                estadisticasmetodo(root)

            def Onservacionesmetod():
                top.withdraw()
                Onservacionesmetodo(root)

            self.AgregarButt = ttk.Button(top,command=Agregarmet)
            self.AgregarButt.place(relx=0.059, rely=0.782,
                                   height=24, width=77)
            self.AgregarButt.configure(text='''Agregar''')

            self.ModificarButt = ttk.Button(top,command=Modificarmetod)
            self.ModificarButt.place(relx=0.237, rely=0.782,
                                     height=24, width=77)
            self.ModificarButt.configure(text='''Modificar''')
            def eliminarmet():
                top.withdraw()
                Eliminarmetodo(root)

            def Agregarmet():
                top.withdraw()
                Agregarmetod(root)

            def Modificarmetod():
                top.withdraw()
                Modificarmetodo(root)

            def estadisticasmetod():
                top.withdraw()
                estadisticasmetodo(root)

            def Onservacionesmetod():
                top.withdraw()
                Onservacionesmetodo(root)

            self.elminarButt = ttk.Button(top,command=eliminarmet)
            self.elminarButt.place(relx=0.425, rely=0.782,
                                   height=24, width=77)
            self.elminarButt.configure(text='''Eliminar''')

            self.EstadistButt = ttk.Button(top,command=estadisticasmetod)
            self.EstadistButt.place(relx=0.611, rely=0.782,
                                    height=24, width=77)
            self.EstadistButt.configure(text='''Estadisticas''')

            self.ObservButt = ttk.Button(top,command=Onservacionesmetod)
            self.ObservButt.place(relx=0.791, rely=0.782,
                                  height=24, width=77)
            self.ObservButt.configure(text='''Observacioes''')

            self.NombreAdmin = tk.Label(top)
            self.NombreAdmin.place(relx=0.514, rely=0.098,
                                   height=21, width=315)
            self.NombreAdmin.configure(anchor='nw')
            self.NombreAdmin.configure(background="#008f4c",
                                       disabledforeground="#a3a3a3",
                                       foreground="#000000")
            nomb = nom_usu + " " + apell_usu
            self.NombreAdmin.configure(text=nomb.upper(),font=("Consolas",12))

            def Atras_Metod():
                root.destroy()
                Inicio.deiconify()

            self.AtrasButt = ttk.Button(top, command=Atras_Metod)
            self.AtrasButt.place(relx=0.059, rely=0.9,
                                 height=24, width=77)
            self.AtrasButt.configure(text='''Inicio''')

            self.TablaDev = ScrolledTreeView(top)
            self.TablaDev.place(relx=0.514, rely=0.358,
                                relheight=0.349, relwidth=0.439)
            self.TablaDev.configure(columns="Col1 Col2")
            # build_treeview_support starting.
            self.TablaDev.heading("#0", text="Docente")
            dato = conexionBd('root', 'llave')
            conect = mysql.connector.connect(**dato)
            cursor = conect.cursor()
            cursor.execute('SELECT * FROM `registro_prestamos` ')
            llavesR = cursor.fetchall()
            for row in llavesR:
                self.TablaDev.insert("", 'end', text=(str(row[5])),
                                     values=(str(row[3]),str(row[0])))
            cursor.close()
            conect.close()
            self.TablaDev.heading("#0", anchor="center")
            self.TablaDev.column("#0", width="101", minwidth="101",
                                 stretch="1", anchor="center")
            self.TablaDev.heading("Col1", text="Llave")
            self.TablaDev.heading("Col1", anchor="center")
            self.TablaDev.column("Col1", width="102", minwidth="101",
                                 stretch="1", anchor="center")
            self.TablaDev.heading("Col2", text="Fecha Devolucion")
            self.TablaDev.heading("Col2", anchor="center")
            self.TablaDev.column("Col2", width="102", minwidth="101",
                                 stretch="1", anchor="center")

            self.label2 = tk.Label(top)
            self.label2.place(relx=0.04, rely=0.314, height=21, width=124)
            self.label2.configure(activebackground="#f9f9f9",
                                  activeforeground="black",
                                  anchor='nw')
            self.label2.configure(background="white",
                                  disabledforeground="#a3a3a3",
                                  foreground="#000000",
                                  highlightbackground="#d9d9d9",
                                  highlightcolor="black",
                                  text='''Prestamos''')

            self.labe1 = tk.Label(top)
            self.labe1.place(relx=0.514, rely=0.314, height=21, width=124)
            self.labe1.configure(activebackground="#f9f9f9",
                                 activeforeground="black",
                                 anchor='nw')
            self.labe1.configure(background="white",
                                 disabledforeground="#a3a3a3",
                                 foreground="#000000",
                                 highlightbackground="#d9d9d9",
                                 highlightcolor="black",
                                 text='''Devoluciones''')

    class AutoScroll(object):
        '''Configure the scrollbars for a widget.'''

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

    vp_start_gui()
