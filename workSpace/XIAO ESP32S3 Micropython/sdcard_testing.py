import camera
import machine
import utime
from time import sleep
import os

class CameraBoard():
    def __init__(self, os):
        self.os = os
        self.microsd_config = {
            'miso':8,
            'mosi':9,
            'cs':21,
            'sck':7,
        }
        self.sd = machine.SDCard(slot=3, width=1,
                    sck=machine.Pin(self.microsd_config['sck']),
                    mosi=machine.Pin(self.microsd_config['mosi']),
                    miso=machine.Pin(self.microsd_config['miso']),
                    cs=machine.Pin(self.microsd_config['cs']))
        
        self.expansion_board_init()
        
    def expansion_board_init(self):
        #self.cam_init()
        print("mounting")
        print(self.sd.info())
        self.os.mount(self.sd, "/sd")
        print(self.os.listdir("/sd"))
        
    def get_time(self):
        current_time = utime.localtime()
        hour = current_time[3]
        minute = current_time[4]
        sec = current_time[5]
        return str(hour) + "_" + str(minute) + "_" + str(sec)
    
    def take_photo(self, file_name):
        p=camera.capture()
        now_file = "/sd/" + file_name + ".jpg"
        imgFile = open(now_file, "wb")
        imgFile.write(p)
        print(p)
        imgFile.close()
        self.close()
        return p

    def close(self):
        camera.deinit()
        
        
camera_board = CameraBoard(os)
camera_board.take_photo('this_photo')
