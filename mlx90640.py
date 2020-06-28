import time
import board
import busio
import adafruit_mlx90640
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib
import numpy as np

PRINT_TEMPERATURES =  True
PRINT_ASCIIART = False

i2c = busio.I2C(board.SCL, board.SDA, frequency=800000)

mlx = adafruit_mlx90640.MLX90640(i2c)
print("MLX addr detected on I2C")
print([hex(i) for i in mlx.serial_number])

mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ

frame = [0] * 768

fig = plt.figure()
im = plt.imshow(np.reshape(frame, (24, 32)), cmap=matplotlib.cm.plasma, interpolation='bilinear')

while True:
    stamp = time.monotonic()
    try:
        mlx.getFrame(frame)
    except ValueError:
        # these happen, no biggie - retry
        continue
    print("Read 2 frames in %0.2f s" % (time.monotonic() - stamp))
    new_frame = np.reshape(frame, (24, 32))
    im.set_data(new_frame)
    plt.show()
