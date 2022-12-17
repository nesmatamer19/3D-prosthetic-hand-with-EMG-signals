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
