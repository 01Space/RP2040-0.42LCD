from machine import Pin, I2C
import time
from ssd1306 import SSD1306_I2C

# Init Display
# scl and sda can be any pin on i2c bus 1
i2c  = I2C(1, scl=Pin(23), sda=Pin(22), freq=40000)
oled = SSD1306_I2C(72, 40, i2c)
# Title Screen
oled.fill(0)

oled.text('"01SPACE"', 0, 0, 1)
oled.show()
time.sleep(5)