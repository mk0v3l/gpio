#!/usr/bin/env python3

from urllib import request
from gpiozero import PingServer
from rgb import RGB
from signal import pause
from time import sleep

rgb = RGB()


def wifi_led_on():
    rgb.all_off
    rgb.green_on


def wifi_led_off():
    rgb.all_off
    rgb.red_on


def internet_on():
    try:
        request.urlopen("http://www.google.com", timeout=1)
        return True
    except:
        return False


while True:
    network = internet_on()
    if network:
        wifi_led_on()
    else:
        wifi_led_off()
    sleep(1)
