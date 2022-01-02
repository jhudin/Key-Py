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
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk
def graficasEx(tab,tip):
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
        print(SalasN)
        dato = conexionBd('root', 'llave')
        conect = mysql.connector.connect(**dato)
        cursor = conect.cursor()
        cursor.execute('SELECT * FROM `registro_prestamos` ')
        llavesR1 = cursor.fetchall()
        j=0
        for row in llavesR1:
            strsal = str(str(row[3]))
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
    print(SalUs)
    print(cant)

    sizes = [1, 2, 3,6,4,5]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
    if (tip=="Barras"):
        y_pos = np.arange(len(SalasN))
        # Create bars
        plt.bar(y_pos, cant)
        plt.title("Concurrencia de las salas")
        # Create names on the x-axis
        plt.xticks(y_pos, SalasN, color='deepskyblue',rotation=45)
        plt.yticks(color='deepskyblue')
        for j in range(len(cant)):
            plt.text(j, cant[j]+0.01, cant[j], fontsize=10)
        # Show graphic
        plt.show()
        #-------------------------------------------------------------------------------
        
    else:
        
        patches, texts = plt.pie(cant,colors=colors, explode=explodes , startangle=140)
        plt.pie(cant,autopct='%1.1f%%', explode=explodes,colors=colors, shadow=True, startangle=140)
        plt.legend(patches, SalasN, loc="best",ncol=2)
        plt.axis('equal')
        plt.title("Concurrencia de las salas")
        plt.tight_layout()
        plt.show()



