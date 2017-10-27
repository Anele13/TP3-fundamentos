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

# matriz

img=mpimg.imread('static/playa.jpg')
for i in range(img.shape[0]): #ensucia la imagen con puntos individuales aleatorios para poder limpiar despues
    for x in range(0,14):
        j =random.randint(0, 449)
        img[i,j]=0

mpimg.imsave("playa2.jpg", img,cmap="gray")
#plt.savefig("calvera2.jpg")
