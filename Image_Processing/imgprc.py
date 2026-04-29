import cv2
import numpy as np
from pyfirmata2 import Arduino
from time import sleep

gray_matrix = cv2.imread('greytiger.jpg', cv2.IMREAD_GRAYSCALE)
binary = []

r, c = gray_matrix.shape

board = Arduino('COM6')   
led = board.get_pin('d:12:o')

while True:
    for i in range(r):
        for j in range(c):
         
            for k in format(gray_matrix[i][j], '08b'):
                if k == '1':   
                    led.write(1)
                    print(1)
                    sleep(0.2)
                else:
                    led.write(0)
                    print(0)
                    sleep(0.2)
            print('\n')
    exit(0)
