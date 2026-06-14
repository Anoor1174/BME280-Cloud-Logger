from machine import Pin, I2C
import bme280
import network
from time import sleep

SSID = "iPhone"
PASSWORD = "Azhaar123"

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
bme = bme280.BME280(i2c=i2c)

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        wlan.connect(SSID, PASSWORD)
        while not wlan.isconnected():
            print("Connecting...")
            sleep(1)
    ip = wlan.ifconfig()[0]
    print("Connected on", ip)
    return ip


def run():
    while True: # loop
        t, p, h = bme.values
        print("Temperature:", t, "Pressure:", p, "Humidity:", h)
        sleep(2)

ip = connect_wifi()
run() 
