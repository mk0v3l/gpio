#!/usr/bin/env python3
import time, board, busio, math
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn


class Sensor_temp:
    def __init__(self):
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.ads = ADS.ADS1115(self.i2c)
        self.chan = AnalogIn(self.ads, ADS.P0)
        self.R1, self.Vcc, self.Bc, self.Tnom, self.Rntc = 10040, 3.34, 3950, 23, 9500

    def _compute_temp(self):
        Vr2 = self.chan.voltage

        steinhart = (
            (math.log((Vr2 * self.R1 / (self.Vcc - Vr2)) / self.Rntc)) / self.Bc
        ) + (1 / (self.Tnom + 273.15))

        temp_K = 1 / steinhart
        temp_C = temp_K - 273.15
        return temp_C, temp_K

    @property
    def get_temp(self):
        return self._compute_temp()[0]

    @property
    def get_temp_K(self):
        return self._compute_temp()[1]


# from leds import Leds

# led = Leds()
# sensor = Sensor_temp()

# while True:
#     # print("{:>5}\t{:>5.3f}".format(chan.value, chan.voltage)) #
#     temp = sensor.get_temp
#     # temp = get_temp(chan.voltage)  #
#     if 20 < temp < 25:
#         led.green_only
#     elif temp < 20:
#         led.blue_only
#     else:
#         led.red_only
#     # Vr2 = chan.voltage
#     # R2=Vr2*R1/(Vcc-Vr2)
#     # steinhart = R2 / Rntc
#     # steinhart = math.log(steinhart)
#     # steinhart /= Bc
#     # steinhart += 1 / (Tnom + 273.15)
#     # steinhart = 1 / steinhart
#     # steinhart -= 273.15
#     # temp = steinhart

#     print("{0:.2f}".format(temp))
#     time.sleep(0.5)
