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
img2 = img.copy()
for i in range(img2.shape[0]): #ensucia la imagen con puntos individuales aleatorios para poder limpiar despues
    for x in range(0,14):
        j=random.choice(range(img2.shape[1]))
        img2[i,j]=0
ruta=ruta.split("/")
mpimg.imsave(ruta[len(ruta)-1].split(".")[0]+"-sucia.jpg", img2,cmap="gray")
