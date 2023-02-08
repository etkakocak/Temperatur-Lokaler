from machine import Pin
from time import sleep

err_ledr = Pin(5, Pin.OUT)
tem_ledb = Pin(4,Pin.OUT)
hum_ledw = Pin(3, Pin.OUT)

def err():
    while True:
        err_ledr.value(1)
        sleep(0.5)
        err_ledr.value(0)
        sleep(0.5)

def ltem():
    while True:
        tem_ledb.value(1)
        sleep(0.5)
        tem_ledb.value(0)
        sleep(0.5)

def hhum():
    while True:
        hum_ledw.value(1)
        sleep(0.5)
        hum_ledw.value(0)
        sleep(0.5)
