
# Complete project details at https://RandomNerdTutorials.com/micropython-programming-with-esp32-and-esp8266/

from machine import Pin
from time import sleep

led = Pin(21, Pin.OUT)

while True:
  led.value(not led.value())
  sleep(0.5)

