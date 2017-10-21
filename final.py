# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib import animation
import matplotlib.image as mpimg
import os
from scipy.misc import toimage

class Celula():
    fila=0
    columna=0
    color=0

    def get_fila(self):
        return self.fila

    def get_columna(self):
        return self.columna

    def get_color(self):
        return self.color

    def __init__(self,fila,columna,color):
        self.fila=fila
        self.columna=columna
        self.color=color

    def cambiar_color(self, vecinos):
        print(self.fila, self.columna)
        lista_colores_vecinos=[]
        for i in range(-1,2):
            for j in range(-1,2):
                fila_vecino = self.get_fila()+i
                columna_vecino = self.get_columna()+j
                lista_colores_vecinos.append(vecinos[fila_vecino, columna_vecino].get_color())
        self.color=np.median(lista_colores_vecinos)


def crear_celulas():
    matriz_celular=np.empty((450,450), dtype=object)
    img=mpimg.imread('static/calavera.jpg')
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            matriz_celular[i,j]=Celula(fila=i,columna=j,color=img[i,j][0])
    return matriz_celular


matriz_celular=crear_celulas()
matriz_colores=np.empty((450,450), dtype=int)

for x in range(0,449):
    for z in range(0,449):
        celula= matriz_celular[x,z]
        celula.cambiar_color(matriz_celular)
        matriz_colores[celula.get_fila(), celula.get_columna()]= celula.get_color()
    print(x,z)


fig = plt.figure()
ax = fig.add_subplot(111)
imagen = ax.imshow(toimage(matriz_colores), interpolation="none", cmap="gray")
plt.show()
