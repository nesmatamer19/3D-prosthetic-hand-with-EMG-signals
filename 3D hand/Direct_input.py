import numpy as np
import serial
from time import sleep


ser = serial.Serial(port="COM3", baudrate=9600, timeout=1)
sleep(2)

while True:

    pred = float(input('Enter the prediction: '))

    print("The prediction is: ",pred)

    if pred == 0:
        print('The movement is: Close')
        ser.write(b'C')
        print(ser.readline().decode().strip())
    elif pred == 1:
        print('The movement is: Open')
        ser.write(b'O')
        print(ser.readline().decode().strip())
    elif pred == 2:
        print('The movement is: Hold')
        ser.write(b'H')
        print(ser.readline().decode().strip())
    elif pred == 3:
        print('The movement is: Point')
        ser.write(b'P')
        print(ser.readline().decode().strip())