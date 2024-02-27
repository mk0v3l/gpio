#!/usr/bin/python3 
from time import sleep
from water_pump import Water_pump
water_pump = Water_pump(21)
print('hello')
while True:
    water_pump.fload()
    sleep(0.3)
    water_pump.stop()
    sleep(1)


