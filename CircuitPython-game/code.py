#
# Released under MIT License
#
# Copyright (C) 2022 by Ciro Cattuto <ciro.cattuto@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom
# the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT
# OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import board
import busio
import adafruit_ssd1306
import neopixel
import digitalio
from random import randint
import time

# Neopixel
pixels = neopixel.NeoPixel(board.GP12, 1)
pixels[0] = (0, 0, 0)

# button
button = digitalio.DigitalInOut(board.GP21)

# I2C bus to OLED display
SDA = board.GP22
SCL = board.GP23
i2c = busio.I2C(SCL, SDA)

# OLED 72x40 display
oled = adafruit_ssd1306.SSD1306_I2C(72, 40, i2c)

oled.fill(0)
oled.show()

# DINO sprinte
dino1 = bytes([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 252, 254, 250, 254, 254, 190, 190, 190, 62, 60, 0])
dino2 = bytes([0, 63, 124, 248, 240, 240, 248, 252, 252, 254, 255, 255, 255, 255, 63, 4, 12, 0, 0, 0, 0, 0])
dino3 = bytes([0, 0, 0, 0, 1, 3, 63, 47, 7, 3, 7, 63, 33, 0, 0, 0, 0, 0, 0, 0, 0, 0])

def place_dino(x,n):
    i = 72*n + x
    oled.buf[i:i+22] = dino1
    oled.buf[i+72:i+72+22] = dino2
    oled.buf[i+144:i+144+22] = dino3

# CACTUS sprite
cactus1 = bytes([240, 0, 255, 255, 128, 128, 252])
cactus2 = bytes([3, 2, 255, 255, 1, 0, 0])

def place_cactus(x):
    i = 72*3 + x
    oled.buf[i:i+7] = cactus1
    oled.buf[i+72:i+72+7] = cactus2


def game():
    dino_vpos = 2
    cactus_delay = 25
    cactus_show = False
    points = 0
    lives = 3

    while True:
        oled.fill(0)

        # dino
        if button.value:
            dino_vpos = (dino_vpos+1) if (dino_vpos<2) else 2
        else:
            dino_vpos = (dino_vpos-1) if (dino_vpos>0) else 0
        place_dino(5, dino_vpos)

        # cactus
        if cactus_show:
            place_cactus(cactus_x)
            cactus_x -= cactus_vx
            if (cactus_x < 0):
                cactus_show = False
                cactus_delay = randint(5,25)
                points += 1
                if points == 25: # win
                    break
        else:
            cactus_delay -= 1
            if cactus_delay == 0:
                cactus_show = True
                cactus_x = 65
                cactus_vx = randint(1,3)

        # collision
        if cactus_show and cactus_x < 25 and dino_vpos > 0:
            pixels[0] = (32, 0, 32)
            for n in range(9):
                oled.invert(n % 2)
                time.sleep(0.1)
            pixels[0] = (0, 0, 0)
            cactus_show = False
            cactus_delay = 25
            lives -= 1
            if lives == 0:
                break

        # score
        oled.text("%02d" % points, 60, 0, 1)

        # frame
        oled.show()
        time.sleep(0.01)

    oled.fill(0)
    if lives == 0:
        pixels[0] = (64, 0, 0)
        oled.text("GAME OVER", 10, 20, 1)
    else:
        pixels[0] = (0, 64, 0)
        oled.text("YOU WIN !", 10, 20, 1)
    oled.show()

    time.sleep(0.5)
    while button.value:
        pass
    pixels[0] = (0, 0, 0)
    while not button.value:
        pass
    oled.fill(0)


# FOREVER PLAY
while True:
    game()


# The sprites "DINO" and "CACTUS" containted in the bitmaps dino1/2/3 and cactus 1/2
# are derived from the Chromium assets of the "neterror" game (chrome://dino/),
# which are distributed according to the license reported below:

#
# Copyright 2015 The Chromium Authors. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#    * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above
# copyright notice, this list of conditions and the following disclaimer
# in the documentation and/or other materials provided with the
# distribution.
#    * Neither the name of Google Inc. nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
