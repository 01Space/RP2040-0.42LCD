import board
import busio
import adafruit_ssd1306
import time
SDA = board.GP22
SCL = board.GP23
i2c = busio.I2C(SCL, SDA)
oled = adafruit_ssd1306.SSD1306_I2C(72, 40, i2c)
oled.fill(0)
time.sleep(0.1)
oled.text("HelloWorld!", 0, 0,1)
oled.show()