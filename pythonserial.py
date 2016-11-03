import serial
import time

a=0
ser = serial.Serial()
ser.baudrate = 1200
ser.port = 'COM14'
ser.open()

while 'true':
    a=ser.readline();
    time.sleep(0.1)
    print(a)
    
    time.sleep(0.090)
    
