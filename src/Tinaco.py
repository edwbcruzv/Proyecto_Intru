from tkinter import *
from tkinter import ttk

class Tinaco:

    def __init__(self) -> None:
        self.indicador_litros=0
        self.progress_llenado=0
        self.progress_entrada=0
        self.progress_salida=0
        self.litros=0

        self.root=Tk()
        self.root.title("Tinaco")
        self.root.geometry("1000x500")
        self.root.resizable(0,0)

        self.imagen_tinaco=PhotoImage(file="imagen2.png")
        self.label=Label(self.root,image=self.imagen_tinaco)
        self.label.place(x=0,y=0)

        self.progress_llenado = ttk.Progressbar(self.label, orient=VERTICAL, length=300, mode='determinate')
        self.progress_llenado.place(x=575,y=100)
        self.indicador_litros=ttk.Label(self.label,text=self.litros)
        self.indicador_litros.place(x=800,y=150)

        

        self.progress_entrada = ttk.Progressbar(self.label, orient=HORIZONTAL, length=250, mode='indeterminate')
        self.progress_entrada.place(x=270,y=100)

        self.progress_salida = ttk.Progressbar(self.label, orient=HORIZONTAL, length=200, mode='indeterminate')
        self.progress_salida.place(x=270,y=370)

        self.root.mainloop()

    def llenadoTinaco(self,litros):
        
        if litros<self.litros:#se esta vaciendo el tinaco
            self.progress_salida.start()
            self.progress_entrada.stop()

        elif litros>self.litros:#se esta llenando el tinaco
            self.progress_entrada.start()
            self.progress_salida.stop()
        else:#se detiene el llenado
            self.progress_entrada.stop()
            self.progress_salida.stop()

        self.litros=litros# se actualizan los litros
        self.progress_llenado.step(litros)