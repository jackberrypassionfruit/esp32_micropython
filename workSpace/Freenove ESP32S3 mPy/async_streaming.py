import sys, network, time
import asyncio
from microdot import Microdot
from camera import Camera, FrameSize, PixelFormat

# WLAN config
ssid = 'TP-Link_1936'
password = '97792710'

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)
while not station.isconnected():
    time.sleep(1)
print(f'Connected! IP: {station.ifconfig()[0]}. Open this IP in your browser')

app = Microdot()

cam = Camera(frame_size = FrameSize.SVGA, pixel_format=PixelFormat.JPEG, init=False)
cam.init()

@app.route('/')
async def index(request):
    return '''<!doctype html>
<html>
  <head>
    <title>Microdot Video Streaming</title>
    <meta charset="UTF-8">
  </head>
  <body>
    <h1>Microdot Video Streaming</h1>
    <img src="/video_feed">
  </body>
</html>''', 200, {'Content-Type': 'text/html'}


@app.route('/video_feed')
async def video_feed(request):
    print('Starting video stream.')

    # MicroPython can only use class-based async generators
    class stream():
        def __aiter__(self):
            return self

        async def __anext__(self):
            await asyncio.sleep(0.01)
            frame = cam.capture()
            return b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + \
                frame + b'\r\n'

        async def aclose(self):
            print('Stopping video stream.')

    return stream(), 200, {'Content-Type':
                           'multipart/x-mixed-replace; boundary=frame'}


if __name__ == '__main__':
    app.run(port=80, debug=True)

