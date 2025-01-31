
from micropython import const

from time import sleep_ms
from machine import SDCard, Pin, SPI
import os, sys

# sd card
SD_SLOT            = const(2)
SD_SS           = const(38)
SD_MOSI         = const(39)
SD_SCK          = const(42)
SD_MISO         = const(41)
SD_IRQ          = const(40)
SD_DAT2         = const(37)



# create an SD card object
sd_card = SDCard(slot=SD_SLOT,sck=SD_SCK,miso=SD_MISO,mosi=SD_MOSI,cs=SD_SS)
# mount the sd card
# vfs = os.VfsFat(sd_card)
os.mount(sd_card,"/sd")

# open a text file for writing
filename = "/sd/helloWorld.txt"
f = open(filename,"r")
buf = f.read()
f.close()

print("{:d} characters read from {:s}".format(len(buf),filename))
print("The content is:")
print(buf)
