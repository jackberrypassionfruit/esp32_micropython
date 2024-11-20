import os
from neopixel import NeoPixel
from machine import Pin, ADC
from time import sleep

light_sensor = ADC(Pin(4))
pin = Pin(48, Pin.OUT)   # set GPIO48  to output to drive NeoPixel
neo = NeoPixel(pin, 1)   # create NeoPixel driver on GPIO48 for 1 pixel

row_num = 0
while True:
    brightness = light_sensor.read()
    if  brightness < 3000:
        neo[0] = (128, 10, 50)
        print("it's red now")
    else:
        neo[0] = (20, 128, 200)
        print("it's blue now")
    neo.write()
    print(f'{'{:04d}'.format(row_num)} --- ', end='')
    print(f'{brightness=}')

    row_num += 1
    sleep(0.5)

