import serial
import time
import thingspeak
channel_id = 178079
write_key = 'U8HQCBU3XPCDJ00I'
a=0
ser = serial.Serial()
ser.baudrate = 1200
ser.port = 'COM14'
ser.open()
channel=thingspeak.Channel(id=channel_id,write_key=write_key)
while 'true':
    a=ser.readline();
    time.sleep(0.1)
    print(a)
    response = channel.update({1:a})
    time.sleep(0.090)
    
