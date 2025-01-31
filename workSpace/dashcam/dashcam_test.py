import sys, os, network, time, machine
import uasyncio as asyncio
from microdot import Microdot
import camera

import zipfile

# # WLAN config
# # ssid, password = 'iPhone 13', 'myNewPassword69420'
# ssid, password = 'TP-Link_1936', '97792710'

# station = network.WLAN(network.STA_IF)
# station.active(True)
# station.connect(ssid, password)
# while not station.isconnected():
#     time.sleep(1)
# print(f'Connected! IP: {station.ifconfig()[0]}. Open this IP in your browser')

duration = 6
fps = 10

frames_qty = duration * fps
frame_length = 1 / fps

print(f'{frames_qty=}')
print(f'{frame_length=}')

sd_dict = {
    'miso': 8,
    'mosi': 9,
    'cs':   21,
    'sck':  7,
}

sd_pins = { key: machine.Pin(val) for key, val in sd_dict.items() }

sd = machine.SDCard(
    slot =  3,
    width = 1,
    sck =   sd_pins['sck'],
    mosi =  sd_pins['mosi'],
    miso =  sd_pins['miso'],
    cs =    sd_pins['cs']
)

os.mount(sd, "/sd")

try:
    cam = camera.init() # Camera
    print("Camera ready?: ", cam)

    while not cam:
        time.sleep(1)
        camera.init()
    # set preferred camera setting
    camera.framesize(10)    # frame size 800X600 (1.33 espect ratio)
    camera.contrast(2)      # increase contrast
    # camera.speffect(2)    # jpeg grayscale
    camera.flip(1)          # verticle flip 

    # for i in range(frames_qty):
    #     time.sleep(frame_length)
    #     pic = camera.capture()
    #     now_file = f"/sd/to_zip/new_photo_{i}.jpg"
    #     with open(now_file, "wb") as imgFile:
    #         imgFile.write(pic)

    in_file_buffer = [
        open(f"/sd/to_zip/new_photo_{i}.jpg", 'wb') 
        for i in range(frames_qty) 
    ]
    
    for in_file in in_file_buffer:
        time.sleep(frame_length)
        pic = camera.capture()
        in_file.write(pic)
        in_file.close()
        
    camera.deinit()
    
except Exception as e:
    camera.deinit()

with zipfile.ZipFile('/sd/archive.zip', mode='w') as zipfp:
    for i in range(frames_qty):
        now_file = f"/sd/to_zip/new_photo_{i}.jpg"
        with zipfp.open(f"new_photo_{i}.jpg", 'w') as arc_f:
            with open(now_file, 'rb') as in_f:
                arc_f.write(in_f.read())

