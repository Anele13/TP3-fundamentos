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
import easygui
# matriz

ruta= easygui.fileopenbox()
img = mpimg.imread(ruta)
for i in range(img.shape[0]): #ensucia la imagen con puntos individuales aleatorios para poder limpiar despues
    for x in range(0,14):
        j=random.choice(range(img.shape[1]))
        img[i,j]=0
ruta=ruta.split("/")
mpimg.imsave(ruta[len(ruta)-1].split(".")[0]+"-sucia.jpg", img,cmap="gray")
