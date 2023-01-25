import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from random import choice

def mandelbrot(c):
    z = c
    n = 256
    for i in range(n):
        if abs(z) > 2:
            return i
        z = z*z + c
    return n

def create_fractal(xmin, xmax, ymin, ymax, xpoints, ypoints):
    x = np.linspace(xmin, xmax, xpoints)
    y = np.linspace(ymin, ymax, ypoints)
    c = x + y * 1j
    mandel = np.array([mandelbrot(c) for c in c.flat]).reshape(xpoints, ypoints)
    return mandel

def create_cocktail():
    fractal = create_fractal(-2, 2, -2, 2, 800, 800)
    plt.imshow(fractal, cmap=choice(cm.cmap_d), extent=(-2, 2, -2, 2))
    plt.show()

if __name__ == '__main__':
    create_cocktail()
