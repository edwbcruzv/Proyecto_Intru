import serial
import time
##conexion con la interfaz grafica comando>   pyuic5 -x Interfaz_Instru.ui -o Interfaz_Instru.py 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
import os
from Interfaz_Intru.Interfaz_Instru import Ui_Form



class Ventana(QtWidgets.QWidget):
    

    def __init__(self,parent=None):
        super(Ventana,self).__init__(parent)
        self.ui=Ui_Form()
        self.ui.setupUi(self)

        self.litros=0
        self.ui.lcdNumber_Litros.display(str(self.litros))

    def llenadoTinaco(self,litros):
        if litros >= 1100:
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

    



##*****INICIO DE TODO EL PROGRAMA
if __name__=='__main__':
    app=QtWidgets.QApplication(sys.argv)
    myapp=Ventana()
    myapp.show()

    #pruebas
    while True:
            
        l=input("Litros:")
        myapp.llenadoTinaco(int(l))

    sys.exit(app.exec_())



exit()
ser = serial.Serial('COM2',9600, timeout=1)
time.sleep(2)
while True:

    print("----",ser.readline().decode('utf-8'))


