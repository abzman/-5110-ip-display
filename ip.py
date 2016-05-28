# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import time
 
import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI
import netifaces as ni
import Image
import ImageDraw
import ImageFont
import socket

# Raspberry Pi hardware SPI config:
# DC = 23
# RST = 24
# SPI_PORT = 0
# SPI_DEVICE = 0

# Raspberry Pi software SPI config:
SCLK = 17
DIN = 18
DC = 27
RST = 23
CS = 22

# Hardware SPI usage:
# disp = LCD.PCD8544(DC, RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=4000000))

# Software SPI usage (defaults to bit-bang SPI interface):
disp = LCD.PCD8544(DC, RST, SCLK, DIN, CS)

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))
 
# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)
 
# Draw a white filled box to clear the image. NEEDED TO SEE TEXT!!!
draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)
 
# Load default font.
font = ImageFont.load_default()
 
# Alternatively load a TTF font.
# Some nice fonts to try: http://www.dafont.com/bitmap.php
# font = ImageFont.truetype('Minecraftia.ttf', 8)
while True: 
	try:
		ip = ni.ifaddresses('eth0')[2][0]['addr']
	except:
		ip = ni.ifaddresses('lo')[2][0]['addr']
	try:
		netmask = ni.ifaddresses('eth0')[2][0]['netmask']
	except:
		netmask = ni.ifaddresses('lo')[2][0]['netmask']
	hostname = socket.gethostname()
	# Write some text.

	# Draw a white filled box to clear the image. NEEDED TO SEE TEXT!!!
	draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)
	disp.display()
	
	draw.text((0,0), hostname, font=font)
	draw.text((0,9), ip, font=font)
	draw.text((0,18), netmask, font=font)
	disp.image(image)
	disp.display()
	#print 'Press Ctrl-C to quit.'
	time.sleep(15.0)
