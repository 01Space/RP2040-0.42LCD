
# RP2040-0.42 OLED 


![image](https://github.com/01Space/RP2040-0.42LCD/blob/main/image/RP2040-0.42LCD.jpg)

![image](https://github.com/01Space/RP2040-0.42LCD/blob/main/image/CGg0wowU.jpg)

![image](https://github.com/01Space/RP2040-0.42LCD/blob/main/image/jka8Tb3U.jpg)


# General Flashing Instructions:

https://github.com/earlephilhower/arduino-pico This link has a very detailed description

Install Arduino IDE and install pico resources by adding line "https://github.com/earlephilhower/arduino-pico/releases/download/global/package_rp2040_index.json" to Additional Boards Manager URLs in Arduino IDE Files / Preferences.
Via Arduino IDE Tools/Board / Board Manager search for pico and choose Raspberry Pi Pico/RP2040 version 2.0.1 to install it.
# The following Arduino libraries need to be installed（via option tools / Manage Libraries in Arduino IDE）

Adafruit NeoPixel 

u8g2(Wire.cpp Need modification，Only the last two lines need to be modified.) 

Arduino15\packages\rp2040\hardware\rp2040\1.13.1\libraries\Wire\src This is under this directory
![image](https://github.com/01Space/RP2040-0.42LCD/blob/main/image/Arduino15.png)

//TwoWire Wire(i2c0, PIN_WIRE0_SDA, PIN_WIRE0_SCL);

//TwoWire Wire1(i2c1, PIN_WIRE1_SDA, PIN_WIRE1_SCL);

Modified into

TwoWire Wire(i2c1, PIN_WIRE1_SDA, PIN_WIRE1_SCL);

TwoWire Wire1(i2c0, PIN_WIRE0_SDA, PIN_WIRE0_SCL);




# Upload sketch from Arduino IDE:

Uploading Sketches
To upload your first sketch, you will need to hold the BOOTSEL button down while plugging in the Pico to your computer. Then hit the upload button and the sketch should be transferred and start to run.

After the first upload, this should not be necessary as the core has auto-reset support. Select the appropriate serial port shown in the Arduino Tools->Port->Serial Port menu once (this setting will stick and does not need to be touched for multiple uploads). This selection allows the auto-reset tool to identify the proper device to reset. Them hit the upload button and your sketch should upload and run.arduino-pico

In some cases the Pico will encounter a hard hang and its USB port will not respond to the auto-reset request. Should this happen, just follow the initial procedure of holding the BOOTSEL button down while plugging in the Pico to enter the ROM bootloader.


# Open Source / Contributors

Larry Bank (gif_01space，ArduinoCore-mbed)

Larry Bank (scd41_01space，ArduinoCore-mbed)

With ArduinoCore-mbed Release 2.0.0, Arduino now support Raspberry Pi Pico officially. To program Raspberry Pi Pico in Arduino framework, install Arduino Mbed OS RP2040 Boards in Arduino IDE's Library Manager.

![image](https://github.com/01Space/RP2040-0.42LCD/blob/main/image/Arduino%20Mbed%20OS%20RP2040%20Boards.jpg)

The following libraries need to be installed

OneBitDisplay

BitBang_I2C

SparkFun_SCD4x_Arduino_Library

AnimatedGIF

And many many others who haven't been mentioned....

# Resources required for programming in CircuitPython
In order to program your Raspberry Pi Pico with CircuitPython, you may have to flash it first. To do this, you need to download the *.uf2 file from https://circuitpython.org/board/raspberry_pi_pico/ and copy it to your Pi Pico.

Furthermore, the libraries are also required for the CircuitPython version used. In my case, I flashed the Pi Pico in version 7.11 and download the examples for version 7.x from https://circuitpython.org/libraries.

From this bundle of libraries we need the files / directory

adafruit_ssd1306.mpy
adafruit_framebuf.mpy
adafruit_display_text
These files/this directory will be/will be placed in the folder "CIRCUITPY (G:) lib".

As well as we also need a binary font file for the representation of text. We download this file from the GitHub repository adafruit / Adafruit_CircuitPython_framebuf from the examples and save it in the same path as the file "code.py" on the drive "CIRCUITPY".

# Contact 01Space
facebook:Jiale Xu

twitter:yongxiangxu251

E-mail：759315223@qq.com


