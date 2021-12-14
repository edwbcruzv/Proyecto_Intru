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
        self.ser = serial.Serial('COM2',9600, timeout=1)
        time.sleep(1)

        self.litros=1
        self.ui.lcdNumber_Litros.display(str(self.litros))

        #self.ui.pushButton_IniciarLlenado.clicked.connect(self.corre)
        
        hilo=threading.Thread(target=self.puerto)
        hilo.start()
    
    def puerto(self):

        while True:  
            
            try:
                distancia=float(self.ser.readline().decode('utf-8'))
                print(">",distancia)
                #mas distancia menos litros
                #menos distancia mas litros
                #la distancia maxima de 2 metros= 200 cm
                self.litros=int(1100-distancia*5.5)
                print(self.litros)
                self.litros=self.puerto.litros()
            except:
                #al momento de recibir un dato puede haber un error y aqui se pasa por alto
                print("-----")
            try:
                self.ui.lcdNumber_Litros.display(str(self.litros))
                self.llenadoTinaco(self.litros) #se va a la interfaz
            except:
                print("paralelo")
    

    def llenadoTinaco(self,litros):
        if litros > 1100:
            #tinaco lleno
            print("lleno")
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
        # litros= x %

        self.ui.progressBar_Tinaco.setValue(int((litros*100)/1100))



##*****INICIO DE TODO EL PROGRAMA
if __name__=='__main__':
    
    app=QtWidgets.QApplication(sys.argv)
    myapp=Ventana()
    myapp.show()
    sys.exit(app.exec_())
    



