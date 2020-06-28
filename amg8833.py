import time
import busio
import board
import adafruit_amg88xx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib
import numpy as np

i2c = busio.I2C(board.SCL, board.SDA)
amg = adafruit_amg88xx.AMG88XX(i2c)

fig = plt.figure()
ax = plt.imshow(amg.pixels, cmap=matplotlib.cm.plasma, interpolation=None)

def init():
    ax.set_data(amg.pixels)

def update(k):

    for text in fig.texts:
        text.set_visible(False)
    ax.set_data(amg.pixels)
    for (j, i), label in np.ndenumerate(amg.pixels):
        plt.text(i,j,label,ha='center',va='center')
    plt.pause(0.5)

    return ax
update(0)
anim = animation.FuncAnimation(fig, update, init_func=init, interval=10000)
plt.show()
