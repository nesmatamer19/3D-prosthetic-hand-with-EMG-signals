import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
import serial
from time import sleep

model = load_model('C:/Users/Nesma Tamer/Downloads/Conv1D.h5')
ser = serial.Serial(port="COM3", baudrate=9600, timeout=1)
sleep(2)

while True:

    max = float(input('Enter the maximum: '))
    min = float(input('Enter the minimum: '))
    mean = float(input('Enter the mean: '))
    var = float(input('Enter the variance: '))
    gender = float(input('Enter the gender (0 for Female and 1 for Male): '))

    sample = [max	,min	,mean	,var	,gender]
    pred = np.argmax(model.predict([[max	,min	,mean	,var	,gender]]))
    print("The prediction is: ",pred)

    if pred == 0:
        print('The movement is: Close')
        ser.write(b'C')
        # print(ser.readline().decode().strip())
    elif pred == 1:
        print('The movement is: Open')
        ser.write(b'O')
        # print(ser.readline().decode().strip())
    elif pred == 2:
        print('The movement is: Hold')
        ser.write(b'H')
        # print(ser.readline().decode().strip())
    elif pred == 3:
        print('The movement is: Point')
        ser.write(b'P')
        # print(ser.readline().decode().strip())