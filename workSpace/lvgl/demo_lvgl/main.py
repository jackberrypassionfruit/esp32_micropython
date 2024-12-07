import lvgl as lv
import display_driver
import gc

class ScreenWithButtonOnly:
    def __init__(self, text, nextScreenNum):
        self.text = text
        self.nextScreen = nextScreenNum

    def load(self):
        self.screen = lv.obj()
        self.btn = lv.btn(self.screen)
        self.btn.add_event_cb(self.eventhandler, lv.EVENT.ALL, None)
        self.btn.align(lv.ALIGN.CENTER, 0, 0)
        self.btn.set_size(200,100)
        self.label = lv.label(self.btn)
        self.label.set_text(self.text)
        
    def eventhandler(self, e):
       if e.code == lv.EVENT.CLICKED:
          changeScreen(self.nextScreen)
    
class ScreenWithChartAndButton:
    def __init__(self, text, nextScreenNum):
        self.text = text
        self.nextScreen = nextScreenNum

    def load(self):
        self.screen = lv.obj()
        self.chart = lv.chart(self.screen)
        self.chart.set_size(200, 150)
        self.chart.align(lv.ALIGN.TOP_MID, 0, 10)
        self.chart.set_type(lv.chart.TYPE.LINE)

        self.ser1 = self.chart.add_series(lv.palette_main(lv.PALETTE.RED), lv.chart.AXIS.PRIMARY_Y)
        self.ser1.y_points = [0, 20, 40, 60, 80, 100, 80, 60, 40, 20, 0]
        self.chart.refresh()      
        
        self.btn = lv.btn(self.screen)
        self.btn.add_event_cb(self.eventhandler, lv.EVENT.ALL, None)
        self.btn.align(lv.ALIGN.BOTTOM_MID, 0, -10)
        self.btn.set_size(300,50)
        self.label = lv.label(self.btn)
        self.label.set_text(self.text)
        
    def eventhandler(self, e):
       if e.code == lv.EVENT.CLICKED:
          changeScreen(self.nextScreen)
    
class ScreenWithCalendarAndButton:
    def __init__(self, text, nextScreenNum):
        self.text = text
        self.nextScreen = nextScreenNum

    def load(self):
        self.screen = lv.obj()
        self.calendar = lv.calendar(self.screen)
        self.calendar.set_size(200, 160)
        self.calendar.align(lv.ALIGN.TOP_MID, 0, 10)
        self.btn = lv.btn(self.screen)
        self.btn.add_event_cb(self.eventhandler, lv.EVENT.ALL, None)
        self.btn.align(lv.ALIGN.BOTTOM_MID, 0, -10)
        self.btn.set_size(300,50)
        self.label = lv.label(self.btn)
        self.label.set_text(self.text)
        
    def eventhandler(self, e):
       if e.code == lv.EVENT.CLICKED:
          changeScreen(self.nextScreen)
        
def changeScreen(screenNum):
    screens[screenNum].load() # build the new screen
    
    # load the new screen (animated) and delete the old one
    lv.scr_load_anim(screens[screenNum].screen, lv.SCR_LOAD_ANIM.FADE_ON, 100, 0, True)
    
    gc.collect() # call the garbage collector
    print("MEM free: " + str(gc.mem_free())) # show free memory
    
screens = []

for i in range(0, 100):
    if i % 2 == 0:
        screens.append(ScreenWithChartAndButton("Screen " + str(i), i + 1))
    elif i % 3 == 0:
        screens.append(ScreenWithCalendarAndButton("Screen " + str(i), i + 1))  
    else:
        screens.append(ScreenWithButtonOnly("Screen " + str(i), i + 1))
        
screens.append(ScreenWithButtonOnly("Back to begin", 0))

        
changeScreen(0) # load initial screen