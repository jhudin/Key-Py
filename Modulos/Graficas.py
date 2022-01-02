import matplotlib.pyplot as plt
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
import tkinter as Tk
def graficas(tab,tip,Estadis):
    if(tab=="Salas"):
        dato = conexionBd('root', 'llave')
        conect = mysql.connector.connect(**dato)
        cursor = conect.cursor()
        cursor.execute('SELECT * FROM `llaves` ')
        llavesR = cursor.fetchall()
        SalasN = []
        SalUs=[]
        cant=[]
        global contador
        contador=0
        for row in llavesR:
            strsal = str(str(row[1]))
            SalasN.append(strsal)
        cursor.close()
        conect.close()
        dato = conexionBd('root', 'llave')
        conect = mysql.connector.connect(**dato)
        cursor = conect.cursor()
        cursor.execute('SELECT * FROM `prestamo`')
        llavesR1 = cursor.fetchall()
        j=0
        for row in llavesR1:
            strsal = str(str(row[7]))
            SalUs.append(strsal)
        cursor.close()
        conect.close()
        i=0
        contador=0
        explodes=[]
        for j in range(len(SalasN)):
            for i in range(len(SalUs)):
                if(SalasN[j]==SalUs[i]):
                    contador+=1
            cant.append(contador)
            contador=0
            explodes.append(0.1)

    sizes = [1, 2, 3,6,4,5]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
    if (tip=="Barras"):
        fi = Figure(figsize=(6,4.4), dpi=83)
        ax = fi.add_subplot(111)
        for j in range(len(cant)):
            ax.text(j, cant[j]+0.01, cant[j], fontsize=9)
        ind = numpy.arange(len(cant))  # the x locations for the groups
        width = .5
        ax.set_ylabel('Cantidad De Prestamos', fontsize=16)
        ax.set_xlabel('Salas', fontsize=16)
        ax.set_title("Uso de salas")
        rects1 = ax.bar(SalasN, cant, width)
        ax.set_xticklabels(SalasN,rotation=15)
        frame2 = tk.Frame(Estadis, width=70, height = 70, background="#008f4c")
        frame2.place(relx=.07, rely=.30)
        canvas = FigureCanvasTkAgg(fi, master=frame2)
        canvas.draw()
        canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=0)

        #-------------------------------------------------------------------------------
        
    else:
        f = Figure(figsize=(6,4.4), dpi=83)
        ax = f.add_subplot(1,1,1)
        f.add_subplot(animated=True)
        patches, texts = plt.pie(cant,colors=colors, explode=explodes , startangle=140)
        ind = numpy.arange(len(cant))  # the x locations for the groups
        width = .5
        ax.pie(cant,autopct='%1.1f%%', explode=explodes,colors=colors, shadow=True, startangle=140)
        ax.legend(patches, SalasN,loc='upper right', bbox_to_anchor=(0.5, 0.1, 0.1, 0.1),ncol=2)
        ax.set_facecolor("#008f4c")
        frame2 = tk.Frame(Estadis, width=70, height = 70, background="#008f4c")
        frame2.place(relx=.073, rely=.30)
        canvas = FigureCanvasTkAgg(f, master=frame2)
        canvas.draw()
       
        canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
