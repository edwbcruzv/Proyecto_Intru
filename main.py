import time
import serial
##conexion con la interfaz grafica comando>   pyuic5 -x Interfaz_Instru.ui -o Interfaz_Instru.py 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
import threading
import os
from Interfaz_Intru.Interfaz_Instru import Ui_Form



class Ventana(QtWidgets.QWidget):
    

    def __init__(self,parent=None):
        super(Ventana,self).__init__(parent)
        self.ui=Ui_Form()
        self.ui.setupUi(self)

        self.litros=100
        self.ui.lcdNumber_Litros.display(str(self.litros))

    def llenadoTinaco(self,litros):
        if litros > 1100:
            #tinaco lleno
            return
        
        if litros<self.litros:#se esta vaciendo el tinaco
            self.ui.progressBar_TuboSalida.setValue(100)
            self.ui.progressBar_Llenado.setValue(0)

        elif litros>self.litros:#se esta llenando el tinaco
            self.ui.progressBar_Llenado.setValue(100)
            self.ui.progressBar_TuboSalida.setValue(0)
        else:#se detiene el llenado
            self.ui.progressBar_TuboSalida.setValue(0)
            self.ui.progressBar_Llenado.setValue(0)

        self.litros=litros# se actualizan los litros
        self.ui.lcdNumber_Litros.display(str(self.litros))
        # 1100 = 100%
        # litros= x

        self.ui.progressBar_Tinaco.setValue(int((litros*100)/1100))

class Puerto:

    def __init__(self) -> None:
        self.ser = serial.Serial('COM2',9600, timeout=1)
        time.sleep(2)

    def litros(self):
        distancia=float(self.ser.readline().decode('utf-8'))
        print(">",distancia)
        #mas distancia menos litros
        #menos distancia mas litros
        #la distancia maxima de 2 metros= 200 cm
        litros=int(1100-distancia*5.5)
        print(litros)

        return litros

##*****INICIO DE TODO EL PROGRAMA
if __name__=='__main__':
    puerto=Puerto()
    time.sleep(2)
    app=QtWidgets.QApplication(sys.argv)
    myapp=Ventana()
    myapp.show()
    litros=1

    while True:  
        
        try:
            print(litros)
            litros=puerto.litros()
        except:
            #al momento de recibir un dato puede haber un error y aqui se pasa por alto
            print("-----")
        
        myapp.llenadoTinaco(puerto.litros()) #se va a la interfaz

    sys.exit(app.exec_())


