from tkinter import ttk
from tkinter import *
import tkinter
import mysql.connector
from Modulos.Conexion import *
import time


class Combobox(ttk.Combobox):
    def set_completion_list(self, completion_list):
        self._completion_list = sorted(completion_list, key=str.lower)
        self._hits = []
        self._hit_index = 0
        self.position = 0
        self.bind('<KeyRelease>', self.handle_keyrelease)
        self['values'] = self._completion_list

    def autocomplete(self, delta=0):
        if delta:
            self.delete(self.position, tkinter.END)
        else:
            self.position = len(self.get())
        _hits = []
        for element in self._completion_list:
                if element.lower().startswith(self.get().lower()):
                        _hits.append(element)
        if _hits != self._hits:
                self._hit_index = 0
                self._hits = _hits
        if _hits == self._hits and self._hits:
                self._hit_index = (self._hit_index + delta) % len(self._hits)
        if self._hits:
                self.delete(0, tkinter.END)
                self.insert(0, self._hits[self._hit_index])
                self.select_range(self.position, tkinter.END)

    def handle_keyrelease(self, event):
        if event.keysym == "BackSpace":
                self.delete(self.index(tkinter.INSERT), tkinter.END)
                self.position = self.index(tkinter.END)
        if event.keysym == "Left":
                if self.position < self.index(tkinter.END):
                        self.delete(self.position, tkinter.END)
                else:
                        self.position = self.position - 1
                        self.delete(self.position, tkinter.END)
        if event.keysym == "Right":
                self.position = self.index(tkinter.END)
        if len(event.keysym) == 1:
                self.autocomplete()


def Prestar(dia, hora, docente, nomdoce, asignatura, llave,nombllav, Inicio, prestamo):
    if(llave != ""):
        dato = conexionBd('root', 'llave')
        conect = mysql.connector.connect(**dato)
        cursor = conect.cursor()
        valores = "INSERT INTO prestamo(`Dia`, `hora`, `Identificacion_docente`, `Nombre_docente`, `Programa`, `codigo_llave`, `NombSal`) VALUES(%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(valores, (dia.lower(), hora.lower(),
                                 docente.lower(),nomdoce.lower(),
                                 asignatura.lower(),
                                 llave.lower(),nombllav.lower()))
        conect.commit()
        try:
            messagebox.showinfo("Completado", "Se ha realizado el prestamo")
            prestamo.destroy()
            Inicio.deiconify()
        except ImportError:
            messagebox.showerror("Error", "Fallo en elprestamo")


def devolver(llave, combot, Inicio, prestamo):
    if(llave != ""):
        dato = conexionBd('root', 'llave')
        conect = mysql.connector.connect(**dato)
        cursor = conect.cursor()
        valores = "SELECT * FROM `prestamo`"
        cursor.execute(valores)
        llavesP = cursor.fetchall()
        dia = str
        hora = str
        Programa = str
        Cod_Docent =str
        Cod_llav= str
        Nombrellave = str
        
        for row in llavesP:
            if((str(row[7])) == (str(llave))):
                dia = str(row[1])
                hora = str(row[2])
                Cod_Docent= str(row[3])
                docente = str(row[4])
                Programa = str(row[5])
                Cod_llav= str(row[6])
                Nombrellave = str(row[7])
        cursor.close()
        conect.close()
        print(Nombrellave)
        hora = hora + "-" + str(time.strftime("%H:%M"))
        conect = mysql.connector.connect(**dato)
        cursor = conect.cursor()
        valores = "INSERT INTO registro_prestamos(`Dia`, `hora`, `codigo_llave`, `Nombre_llave`, `Identificacion_docente`, `Nombre_docent`, `Programa`, `Novedades`) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(valores, (dia.lower(), hora.lower(),Cod_llav.lower(),Nombrellave.lower(),
                                 Cod_Docent.lower(),docente.lower(), Programa.lower(), combot.lower()))
        conect.commit()
        cursor.close()
        conect.close()
        conect = mysql.connector.connect(**dato)
        cursor = conect.cursor()
        cursor.execute("""DELETE FROM prestamo  WHERE  NombSal='%s'""" % (Nombrellave.lower()))
        conect.commit()
        try:
            messagebox.showinfo("Completado",
                                "Se ha realizado la devolucion ")
            prestamo.destroy()
            Inicio.deiconify()
        except ImportError:
            messagebox.showerror("Error",
                                 "No se ha realizado la devolucion")
        cursor.close()
        conect.close()


def ComboboxMost(test_list, Inicio, x1, y1, x2, y2, bs, tamaño):
        FrameComboBox = Frame(Inicio)
        FrameComboBox.place(x=x1, y=y1)
        global combo
        combo = Combobox(FrameComboBox, width=tamaño)
        combo.set_completion_list(test_list)
        combo.pack()
        combo.focus_set()


def combosal():
    return combo.get()


def ComboboxMostPrin(test_list, Inicio, x1, y1, x2, y2, bs, tamaño, combo):
        FrameComboBox = Frame(Inicio)
        FrameComboBox.place(x=x1, y=y1)
        combo = Combobox(FrameComboBox, width=tamaño)
        combo.set_completion_list(test_list)
        combo.pack()
        combo.focus_set()

        def Buscar():
            dato = conexionBd('root', 'llave')
            conect = mysql.connector.connect(**dato)
            cursor = conect.cursor()
            cursor.execute('SELECT * FROM `prestamo` ')
            llavesR = cursor.fetchall()
            docente = str
            docente = ""
            hora = str
            hora = ""
            comprob = False
            global contador
            for row in llavesR:
                if(str(str(row[7])) == str(combo.get())):
                    cursor1 = conect.cursor()
                    cursor1.execute('SELECT * FROM docentes')
                    llavesU = cursor1.fetchall()
                    Nombdocente=str
                    docente = str(str(row[3]))
                    for rowu in llavesU:
                        if(docente== str(rowu[2])):
                            Nombdocente = str(rowu[1])
                    
                    hora = str(str(row[2]))
                    comprob = True
            cursor.close()
            conect.close()
            if comprob:
                text1 = "La llave de la sala "
                text2 = " fue solicitada por "
                sal = (str(combo.get()))
                docentetext = text1 + sal + text2 + Nombdocente + " a las " + hora
                comprob = False
            else:
                docentetext = "La llave se encuentra disponible"
            messagebox.showinfo("Docente", docentetext)
        if bs == "Buscar":
            Busquedasal = ttk.Button(Inicio, text=bs, command=Buscar)
            Busquedasal.place(x=x2, y=y2)
