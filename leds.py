from gpiozero import LED, Button
from signal import pause
from time import sleep


class Leds:
    def __init__(self):
        self.green = LED(21)
        self.blue = LED(20)
        self.red = LED(16)
        self.leds = [self.green, self.blue, self.red]
        self.flags = [False, False, False]
        self.nb_leds = len(self.leds)
        self.isOn = False
        # self.blink_time = 1
        # self.blink_time = 0.1 # Fast
        self.blink_time = 2  # Slow

    @property
    def green_toggle(self):
        self.green.toggle()

    @property
    def green_on(self):
        self.green.on()

    @property
    def green_off(self):
        self.green.off()

    @property
    def blue_toggle(self):
        self.blue.toggle()

    @property
    def blue_on(self):
        self.blue.on()

    @property
    def blue_off(self):
        self.blue.off()

    @property
    def red_toggle(self):
        self.red.toggle()

    @property
    def red_on(self):
        self.red.on()

    @property
    def red_off(self):
        self.red.off()

    @property
    def all_on(self):
        for led in self.leds:
            led.on()
        self.isOn = True

    @property
    def all_off(self):
        for led in self.leds:
            led.off()
        self.isOne = False

    @property
    def all_toggle(self):
        for led in self.leds:
            led.toggle()

    @property
    def green_only(self):
        self.all_off
        self.green.on()

    @property
    def blue_only(self):
        self.all_off
        self.blue.on()

    @property
    def red_only(self):
        self.all_off
        self.red.on()

    @property
    def blinks(self):
        self.all_off
        for led in self.leds:
            led.blink(
                self.blink_time / self.nb_leds,
                self.blink_time - self.blink_time / self.nb_leds,
            )
            sleep(self.blink_time / self.nb_leds)
