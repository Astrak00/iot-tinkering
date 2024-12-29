from gpiozero import Button
from luma.core.interface.serial import i2c
from luma.oled.device import sh1106
from PIL import Image, ImageDraw, ImageFont
from time import sleep
import sys
import time

"""
GPIO layout
VCC         - 1 - 3.3V
SDA         - GPIO2 
SCL         - GPIO3
GND         - 9
BTN-Signal  - GPIO22

"""

# Inicializa el botón conectado al pin GPIO 22
BtnPin = Button(22)

# Initialize the I2C interface
serial = i2c(port=1, address=0x3C)  # Adjust address if needed
device = sh1106(serial)

# Create a blank image
width = device.width
height = device.height

image = Image.new("1", (width, height))
# Create a drawing object
draw = ImageDraw.Draw(image)

def draw_text(acc: bool):
    # Draw something (e.g., a rectangle and text)
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    draw.text((10, 10), f"Llevas\n {acc} pulsaciones", fill=255)
    device.display(image)

def draw_image():
    image_path = "pano.jpg"  # Replace with your image file path
    image = Image.open(image_path)

    # Resize and convert the image to 1-bit monochrome
    image = image.resize((device.width, device.height)).convert("1")

    # Display the image
    device.display(image)

acc = 0
a = True

while 1:
    if BtnPin.value == 1:
        acc += 1
    draw_text(acc)
    time.sleep(0.1)




