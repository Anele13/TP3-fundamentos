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
    '''for i in range(buffer_b.shape[0]):
        for j in range(buffer_b.shape[1]):
            if buffer_b[i, j]== 255:
                buffer_b[i, j] = 0
            else:
                buffer_b[i,j]=255
    '''
    vecinos=vecindario(buffer_b)
    for i in range(buffer_b.shape[0]): #ensucia la imagen con puntos individuales aleatorios para poder limpiar despues
        for x in range(0,14):
            j =random.randint(0, 449)
            buffer_b[i,j]=0
    return buffer_b


# matriz


# FIgura
fig = plt.figure() #crea una figura
ax = fig.add_subplot(111) #es en cuantas partes vas a dividir la cuadricula y el tercer arg es en cual de todas vas a dibujar
ax.axis('off') #desactiva los rotulos numeras al costado de cada eje



img=mpimg.imread('static/calavera.jpg')
#img=convertirBinaria(img)
img=convertirBinaria(img)
imagen = ax.imshow(img, interpolation="none", cmap="gray")#interpolation es la nitidez de los cuadros negros y map es el color
j=0


#img = np.zeros((8, 8), dtype=int)

# Añadimos una nave
def paso(img):
    global j
    v = vecindario(img)
    buffer_b = img.copy() # Hacemos una copia de la matriz
    for i in range(buffer_b.shape[0]):
        if i==0:
            buffer_b[i,j]= np.median([buffer_b[i,j],  buffer_b[i+1,j], buffer_b[i+2,j] ])
            print("sali")
        else:
            if i==449:
                buffer_b[i,j]= np.median([  buffer_b[i,j],  buffer_b[i-1,j],  buffer_b[i-2,j]  ])
            else:
                buffer_b[i,j]= np.median([  buffer_b[i,j],   buffer_b[i+1,j],  buffer_b[i-1,j]  ])
    j=j+1
    if j==450:
        j=0
    return buffer_b


def animacion(nada):
    global img
    img=paso(img)
    imagen.set_data(img)

ani = animation.FuncAnimation(fig, animacion)
plt.show()
