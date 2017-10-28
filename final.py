
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib import animation
import matplotlib.image as mpimg
import os
from scipy.misc import toimage
import itertools
from matplotlib.widgets import Button
def funcion_next():
    for x in itertools.product(range(matriz_celular.shape[1]-1), repeat=2):
            celula= matriz_celular[x]
            celula.cambiar_color(matriz_celular)

    for x in itertools.product(range(matriz_celular.shape[1]-1), repeat=2):
            celula=matriz_celular[x]
            matriz_colores[celula.get_fila(), celula.get_columna()]= celula.get_buffer()
            celula.color=celula.get_buffer()

    plt.imshow(toimage(matriz_colores), interpolation="none", cmap="gray")
class Index(object):
    ind = 0

    def next(self, event):
        funcion_next()
        

    def prev(self, event):
        a = 0
class Celula():
    fila=0
    columna=0
    buff=0
    color=0

    def get_fila(self):
        return self.fila

    def get_columna(self):
        return self.columna

    def get_color(self):
        return self.color

    def get_buffer(self):
        return self.buff

    def __init__(self,fila,columna,color):
        self.fila=fila
        self.columna=columna
        self.color=color

    def cambiar_color(self, vecinos):
        lista_colores_vecinos=[]
        for x in itertools.product(range(-1,2), repeat=2):
                fila_vecino = self.get_fila()+x[0]
                columna_vecino = self.get_columna()+x[1]
                lista_colores_vecinos.append(vecinos[fila_vecino, columna_vecino].get_color())
        self.buff=np.median(lista_colores_vecinos)


def crear_celulas(img):
    matriz_celular=np.empty((img.shape[0],img.shape[1]), dtype=object)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            matriz_celular[i,j]=Celula(fila=i,columna=j,color=img[i,j][0])
    return matriz_celular


def animacion(fig):
    for x in itertools.product(range(matriz_celular.shape[1]-1), repeat=2):
            celula= matriz_celular[x]
            celula.cambiar_color(matriz_celular)

    for x in itertools.product(range(matriz_celular.shape[1]-1), repeat=2):
            celula=matriz_celular[x]
            matriz_colores[celula.get_fila(), celula.get_columna()]= celula.get_buffer()
            celula.color=celula.get_buffer()

    plt.imshow(toimage(matriz_colores), interpolation="none", cmap="gray")
'''
def funcion(img):
    print("entre a la funcion")
    matriz_celular=crear_celulas(img)
    matriz_colores=np.empty((matriz_celular.shape[0],matriz_celular.shape[1]), dtype=int)

    callback = Index()
    axprev = plt.axes([0.1, 0.05, 0.1, 0.075])
    axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
    bnext = Button(axnext, 'Siguiente')
    bnext.on_clicked(callback.next)
    bprev = Button(axprev, 'Anterior')
    bprev.on_clicked(callback.prev)
    print("llame a la funcion")
    plt.show()
    print("llamo a la funcion")
'''


if __name__ == '__main__':
    os.walk('/')
    img=mpimg.imread('static/calavera.jpg')
    matriz_celular=crear_celulas(img)
    matriz_colores=np.empty((matriz_celular.shape[0],matriz_celular.shape[1]), dtype=int)
    

    callback = Index()
    
    fig = plt.figure()
    a=fig.add_subplot(1,2,1)
    img = mpimg.imread('static/calavera.jpg')
    lum_img = img[:,:,0]
    imagen = plt.imshow(lum_img, interpolation="none", cmap="gray")
    a.set_title('Antes')
    a=fig.add_subplot(1,2,2)
    a.set_title('Despues')
    plt.imshow(toimage(matriz_colores), interpolation="none", cmap="gray")
    #ani = animation.FuncAnimation(fig, animacion)
    #plt.show()

    
    axprev = plt.axes([0.1, 0.05, 0.1, 0.075])
    axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
    bnext = Button(axnext, 'Siguiente')
    bnext.on_clicked(callback.next)
    bprev = Button(axprev, 'Anterior')
    bprev.on_clicked(callback.prev)
    plt.show()

    #funcion(img)

