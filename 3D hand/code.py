import numpy as np
import pandas as pd
import csv
from random import randrange


# 0 for rest (open)
# 1 for hold (hold)
# 2 for close(close)

def close():
    print("Closed")


def open():
    print("Opened")


def hold():
    print("hold")


df = pd.read_csv("dataset.csv", usecols=["Signal", "Move"], )
for x in range(10):
    random = randrange(len(df.index))
    signal = int(df.values[random][0])
    move = int(df.values[random][1])
    print(signal)
    classes = ['Rest', 'hold', 'close']
    read = classes[move]
    if read == 'close':
        close()
    elif read == 'Rest':
        open()
    elif read == 'hold':
        hold()
