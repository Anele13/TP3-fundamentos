# coding: utf-8

from time import sleep
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib import animation
import matplotlib.image as mpimg
import os
import time
import random

def calcular(b):
    extra = b.copy() # Hacemos una copia de la matriz
    for i in range(b.shape[0]):
        for j in range(b.shape[1]):
            if b[i, j]== 255:
                extra[i, j] = 1
            else:
                extra[i,j]=0
    return extra


def vecindario(b):
    """Array de células vivas en el vecindario."""
    extra= calcular(b)
    vecindario = (
        np.roll(np.roll(extra, 1, 1), 1, 0) +  # Abajo-derecha
        np.roll(extra, 1, 0) +  # Abajo
        np.roll(np.roll(extra, -1, 1), 1, 0) +  # Abajo-izquierda
        np.roll(extra, -1, 1) +  # Izquierda
        np.roll(np.roll(extra, -1, 1), -1, 0) +  # Arriba-izquierda
        np.roll(extra, -1, 0) +  # Arriba
        np.roll(np.roll(extra, 1, 1), -1, 0) +  # Arriba-derecha
        np.roll(extra, 1, 1)  # Derecha
    )
    return vecindario



def convertirBinaria(img):
    buffer_b = img.copy() # Hacemos una copia de la matriz
    for i in range(buffer_b.shape[0]):
        for j in range(buffer_b.shape[1]):
            if buffer_b[i, j]== 255:
                buffer_b[i, j] = 0
            else:
                buffer_b[i,j]=255

    vecinos=vecindario(buffer_b)
    for i in range(buffer_b.shape[0]): #ensucia la imagen con puntos individuales aleatorios para poder limpiar despues
        for x in range(0,14):
            j =random.randint(0, 449)
            if vecinos[i,j]==0:
                buffer_b[i,j]=255
    return buffer_b


# matriz


# FIgura
fig = plt.figure() #crea una figura
ax = fig.add_subplot(111) #es en cuantas partes vas a dividir la cuadricula y el tercer arg es en cual de todas vas a dibujar
ax.axis('off') #desactiva los rotulos numeras al costado de cada eje



img=mpimg.imread('/home/anele/Descargas/calavera.jpg')
img=convertirBinaria(img)


#img = np.zeros((8, 8), dtype=int)

# Añadimos una nave
'''img[1, 2] = 255
img[2, 1] = 255
img[3, 2] = 255
img[7,7]=255'''


imagen = ax.imshow(img, interpolation="none", cmap=cm.gray_r)#interpolation es la nitidez de los cuadros negros y map es el color
j=0

def paso(img):
    #global j
    v = vecindario(img)
    buffer_b = img.copy() # Hacemos una copia de la matriz
    for i in range(buffer_b.shape[0]):
        for j in range(buffer_b.shape[1]):
            if v[i, j]<=4 and buffer_b[i,j]==255:
                buffer_b[i, j] = 0
    '''j=j+1
    if j == len(buffer_b):
        j=0'''
    return buffer_b


def animacion(nada):
    global img
    ''''if img[15,15]:
        print("si")
        img[15,15]=0
        img[16,15]=0
        img[16,15]=0
        img[18,15]=0
        img[19,15]=0
    else:
        print("No")
        img[15,15]=255
        img[16,15]=255
        img[16,15]=255
        img[18,15]=255
        img[19,15]=255
    imagen.set_data(img)'''
    img=paso(img)
    imagen.set_data(img)

ani = animation.FuncAnimation(fig, animacion)
plt.show()
