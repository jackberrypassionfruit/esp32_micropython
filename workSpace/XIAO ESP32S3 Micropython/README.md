
One firmware and flasher script
1) firmware.bin
2) esp32s3_flash

This firmware was compiled with esp-idf4.4.5, with MicroPython v1.20.0-197.

You need to flash this firmware to your XIAO.

```
./esp32s3_flash /dev/ttyACM0
```

Three example scripts
1) Wifi.py
2) streamin_server.py
3) steaming_client.py

Upload 1) and 2) to XIAO ESP32S3 Sense.
To start the server just import the streaming server script

```
MicroPython v1.20.0-197-gb3cd41dd4-kaki5 on 2023-06-18; ESP32S3-XIAO OV2640 (KAKI5) with ESP32-S3
>>> 
>>> import streamin_server
Camera ready?:  True
Waiting ...
Waiting ...
Connected to dlink-3530
network config: ('192.168.4.70', '255.255.252.0', '192.168.4.1', '192.168.4.1')
Request from: ('192.168.4.27', 39094)

```

To stream mjpeg just connect to server from a web browser

http://192.168.4.70/xiao/Hi-Xiao-Ling

To use opencv on a PC that installed opencv-python just run the client script
on that PC.

```
python3 steaming_client.py
```

Of course, to test, you need to change the IP address your XIAO in the URL and steaming_client.py

@shariltumin.gamil.com

