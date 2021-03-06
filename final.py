
import easygui
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib import animation
import matplotlib.image as mpimg
import os
from scipy.misc import toimage
import itertools
from matplotlib.widgets import Button

class Celula():
    def get_fila(self):
        return self.fila

    def get_columna(self):
        return self.columna

    def get_color(self):
        return self.color

    def get_buffer(self):
        return self.buff

    def cambiar_color(self, vecinos):
        lista_colores_vecinos=[]
        for x in itertools.product(range(-1,2), repeat=2):
        	fila_vecino = self.get_fila()+x[0]
        	columna_vecino = self.get_columna()+x[1]
        	lista_colores_vecinos.append(vecinos[fila_vecino, columna_vecino].get_color())
        self.buff=np.median(lista_colores_vecinos)

    def __init__(self,fila,columna,color):
        self.fila=0
        self.columna=0
        self.buff=0
        self.color=0
        self.colores_previos=[]
        self.fila=fila
        self.columna=columna
        self.color=color

    def get_color_anterior(self):
        try:
            return self.colores_previos.pop()
        except IndexError:
            return 0


class Evento (object):
    def avanzar(self, event):
        for x in itertools.product(range(matriz_celular.shape[0]-1),range(matriz_celular.shape[1]-1)):
            celula= matriz_celular[x]
            celula.cambiar_color(matriz_celular)

        for x in itertools.product(range(matriz_celular.shape[0]-1),range(matriz_celular.shape[1]-1)):
            celula=matriz_celular[x]
            matriz_colores[celula.get_fila(), celula.get_columna()]= celula.get_buffer()
            celula.color=celula.get_buffer()
        plt.imshow(matriz_colores, interpolation="none", cmap="gray")

    def retroceder(self, event):
        for x in itertools.product(range(matriz_celular.shape[0]-1),range(matriz_celular.shape[1]-1)):
            celula = matriz_celular[x]
            matriz_colores[celula.get_fila(), celula.get_columna()]=celula.get_color_anterior()
        plt.imshow(matriz_colores, interpolation = "none", cmap="gray")


def crear_celulas(img):
    matriz_celular=np.empty((img.shape[0],img.shape[1]), dtype=object)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            celula=Celula(fila=i,columna=j,color=img[i,j][0])
            celula.colores_previos.append(celula.get_color())
            matriz_celular[i,j]=celula
    return matriz_celular

if __name__ == '__main__':
    img = mpimg.imread(easygui.fileopenbox())
    matriz_celular=crear_celulas(img)
    matriz_colores=np.empty((matriz_celular.shape[0],matriz_celular.shape[1]),dtype=int)

    e = Evento()
    fig = plt.figure()

    a=fig.add_subplot(1,2,1)
    plt.imshow(img, interpolation="none", cmap="gray")
    a.set_title('Antes')

    a=fig.add_subplot(1,2,2)
    a.set_title('Despues')
    plt.imshow(matriz_colores, interpolation="none", cmap="gray")


    bnext = Button(plt.axes([0.81, 0.05, 0.1, 0.075]), 'Avanzar')
    bnext.on_clicked(e.avanzar)

    bprev = Button(plt.axes([0.1, 0.05, 0.15, 0.075]), 'Retroceder')
    bprev.on_clicked(e.retroceder)

    plt.axes(fig.get_axes()[1])

    plt.show()
