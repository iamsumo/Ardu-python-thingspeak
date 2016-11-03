# Ardu-python-thingspeak
This repository has codes to send data to thingspeak channel from arduino through a python script running in the laptop.
Upload the program into arduino and ceheck whether it's sending data through serial bus using serial monitor.

steps for python:
1.downlod python
2.download pyserial package and thingspeak python package, unzip the file, go to to the folder which has setup.py through command prompt, 
then run the following command
setup.py install
3. open python-serial.py program change the comport name to the comport your arduino is connecte to.
4.Run the program and check whether the program is receiving data from arduino.
5. Open pythonserial-thingspeak.py, change the values of 'channel_id' and and 'write_key' to your respective id and key.
6. Run the code, open your thingspeak dash board and check whether the data is being plotted.

I have not written code for acknowledging the reception and detecting loss of data while transmission. try to write codes for that. 
