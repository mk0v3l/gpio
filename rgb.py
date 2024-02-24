from leds import Leds
from gpiozero import LED, Button


class RGB(Leds):
    def __init__(self):
        self.green = LED(19)
        self.orange = LED(26)
        self.red = LED(13)
        self.leds = [self.green, self.orange, self.red]
        self.flags = [False, False, False]
        self.nb_leds = len(self.leds)
        self.isOn = False
        # self.blink_time = 1
        # self.blink_time = 0.1 # Fast
        self.blink_time = 2  # Slow
