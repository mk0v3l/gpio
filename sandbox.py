#!/usr/bin/env python3

from leds import Leds
from sensor_temp import Sensor_temp
from water_pump import Water_pump
from time import sleep

# leds = Leds()
# sensor = Sensor_temp()
water_pump = Water_pump(21)
while True:
    water_pump.fload()
    sleep(1)
    water_pump.stop()
    sleep(1)
# leds.all_on()


def test_temp():
    while True:
        temp = sensor.get_temp
        # temp = get_temp(chan.voltage)  #
        if 20 < temp < 25:
            leds.green_only
        elif temp < 20:
            leds.blue_only
        else:
            leds.red_only


def test_rgb():
    while True:
        # inpt = input("On [o]\nOff [f]\nBlink [B]\nQuit [q]\n")
        inpt = input(
            "On [o]\nOff [f]\n---\nGreen [g]\nBlue [b]\nRed [r]\n---\nBlink [B]\nQuit [q]\n"
        )
        match inpt:
            case "o":
                leds.all_on
            case "f":
                leds.all_off
            case "g":
                leds.green_toggle
            case "b":
                leds.blue_toggle
            case "r":
                leds.red_toggle
            case "B":
                leds.blinks
            case "q":
                exit()
            case _:
                print("Invalid input")


# test_temp()
