import serial
import time

class Puerto:

    def __init__(self) -> None:
        self.ser = serial.Serial('COM2',9600, timeout=1)
        time.sleep(2)

    def litros(self):
        distancia=float(self.ser.readline().decode('utf-8'))
        print(">",distancia)
        litros=int(1100-distancia*5.5)
        print(litros)

        return litros
