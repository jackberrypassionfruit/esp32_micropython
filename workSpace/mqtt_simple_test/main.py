# Complete project details at https://RandomNerdTutorials.com/micropython-programming-with-esp32-and-esp8266/

import time
from umqttsimple import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp
esp.osdebug(None)
import gc
gc.collect()

ssid = 'raspi-webgui'
password = 'ChangeMe'
mqtt_server = '192.168.0.211'

client_id = ubinascii.hexlify(machine.unique_id())
topic_pub = b'/testing/hello'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  time.sleep(0.1)

print('Connectioned to WLAN')

client = MQTTClient(client_id, mqtt_server)
client.connect()
print('Connected to MQTT Broker')

counter = 0

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(5)
  machine.reset()

while True:
  try:
    msg = b'Hello #%d' % counter
    client.publish(topic_pub, msg)
    counter += 1
    time.sleep(2)
  except OSError as e:
    restart_and_reconnect()



