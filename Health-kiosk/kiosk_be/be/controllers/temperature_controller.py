import board
import busio as io
import adafruit_mlx90614
import time

timeout = time.time() + 40 #40 secs
i2c = io.I2C(board.SCL, board.SDA, frequency=100000)
mlx = adafruit_mlx90614.MLX90614(i2c)

while True:
    roomTemp = "{:.2f}".format(mlx.ambient_temperature)
    bodyTemp = "{:.2f}".format(mlx.object_temperature)
    if time.time() > timeout:
        break
    time.sleep(1)

print("Room Temperature is: ",roomTemp,"°C")
print("Body Temperature is: ",bodyTemp,"°C")
