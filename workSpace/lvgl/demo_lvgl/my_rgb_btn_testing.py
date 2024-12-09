'''Custom Driver xpt2046_cyd and MPY-LVGL build from
https://stefan.box2code.de/2023/11/18/esp32-grafik-mit-lvgl-und-micropython/

Running on cheap yellow display with TWO USB Ports
--> https://github.com/witnessmenow/ESP32-Cheap-Yellow-Display/blob/main/cyd.md
'''
import lvgl as lv
import time
import display_driver
from machine import Pin, ADC

num = 0 # Used for callback
rgb_val = 'green'

r_led, g_led, b_led = Pin(4, Pin.OUT), Pin(16, Pin.OUT), Pin(17, Pin.OUT)
ldr_pin = ADC(Pin(34, Pin.IN))

def enable(el):
    if el.has_state(lv.STATE.DISABLED):
        el.clear_state(lv.STATE.DISABLED)

def disable(el):
    if not el.has_state(lv.STATE.DISABLED):
        el.add_state(lv.STATE.DISABLED)

def largeFont(el):
    el.set_style_text_font(lv.font_montserrat_16, 0)

def callback(s):
    global num
    if s == 'Prev':
        num -= 1
    elif s == 'Next':
        num += 1
    valueLbl.set_text('Count: ' + str(num))
    
    '''
    num_mod = num % 3
    if num_mod == 0:
        r_led.value(False)
        g_led.value(True)
        b_led.value(True)
    elif num_mod == 1:
        r_led.value(True)
        g_led.value(False)
        b_led.value(True)
    elif num_mod == 2:
        r_led.value(True)
        g_led.value(True)
        b_led.value(False)
    '''
    # print('button clicked')

def rgb_callback(s):
    global rgb_val
    rgb_val = s
    LEDvalueLbl.set_text('RGB Color: ' + str(rgb_val))
    if s == 'red':
        r_led.value(False)
        g_led.value(True)
        b_led.value(True)
    if s == 'green':
        r_led.value(True)
        g_led.value(False)
        b_led.value(True)
    if s == 'blue':
        r_led.value(True)
        g_led.value(True)
        b_led.value(False)


''' Get reference to active screen for drawing '''
scr = lv.scr_act()
scr.set_style_bg_color(lv.color_white(), lv.PART.MAIN)


''' Create label and center it on screen '''
valueLbl = lv.label(scr)
largeFont(valueLbl)
valueLbl.set_text('Count: ' + str(num))
valueLbl.center()


''' Create Button with icon and text and add callback '''
prevBtn = lv.btn(scr)
prevBtn.set_size(80, 40)
prevBtn.align_to(valueLbl, lv.ALIGN.OUT_LEFT_MID, -20, 0)
prevBtn.add_event_cb(lambda e: callback('Prev'), lv.EVENT.CLICKED, None)
''' Assign label to button '''
prevBtnLbl = lv.label(prevBtn)
prevBtnLbl.set_text(lv.SYMBOL.PREV + ' Prev')
prevBtnLbl.center()


nextBtn = lv.btn(scr)
nextBtn.set_size(80, 40)
nextBtn.align_to(valueLbl, lv.ALIGN.OUT_RIGHT_MID, 20, 0)
nextBtn.add_event_cb(lambda e: callback('Next'), lv.EVENT.CLICKED, None)

nextBtnLbl = lv.label(nextBtn)
nextBtnLbl.set_text('Next ' + lv.SYMBOL.NEXT)
nextBtnLbl.center()


''' Create myOwn Button for changing RGB color to red '''
RgbBtn = lv.btn(scr)
RgbBtn.set_size(80, 40)
RgbBtn.align_to(valueLbl, lv.ALIGN.OUT_TOP_MID, 0, -50)
RgbBtn.add_event_cb(lambda e: rgb_callback('red'), lv.EVENT.CLICKED, None)

RgbBtnLbl = lv.label(RgbBtn)
RgbBtnLbl.set_text('Red ' + lv.SYMBOL.EYE_OPEN)
RgbBtnLbl.center()

''' Create myOwn Button for changing RGB color to green '''
rGbBtn = lv.btn(scr)
rGbBtn.set_size(80, 40)
rGbBtn.align_to(valueLbl, lv.ALIGN.OUT_TOP_LEFT, -100, -50)
rGbBtn.add_event_cb(lambda e: rgb_callback('green'), lv.EVENT.CLICKED, None)

rGbBtnLbl = lv.label(rGbBtn)
rGbBtnLbl.set_text('Green ' + lv.SYMBOL.EYE_OPEN)
rGbBtnLbl.center()

''' Create myOwn Button for changing RGB color to blue '''
rgBBtn = lv.btn(scr)
rgBBtn.set_size(80, 40)
rgBBtn.align_to(valueLbl, lv.ALIGN.OUT_TOP_RIGHT, 0100, -50)
rgBBtn.add_event_cb(lambda e: rgb_callback('blue'), lv.EVENT.CLICKED, None)

rgBBtnLbl = lv.label(rgBBtn)
rgBBtnLbl.set_text('Blue ' + lv.SYMBOL.EYE_OPEN)
rgBBtnLbl.center()



'''Create label showing current RGB color value '''
LEDvalueLbl = lv.label(scr)
LEDvalueLbl.align_to(valueLbl, lv.ALIGN.OUT_BOTTOM_LEFT, 0, 50)
largeFont(LEDvalueLbl)
LEDvalueLbl.set_text('RGB Color: ' + str(rgb_val))



