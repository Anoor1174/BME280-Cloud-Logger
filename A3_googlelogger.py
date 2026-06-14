from machine import Pin, I2C
import bme280
import network
import urequests
import json
import time
import gc

SSID = "iPhone"
PASSWORD = "Azhaar123"

SCRIPT_URL = "https://script.google.com/macros/s/AKfycbxD1eVe9aavv_z_qMbOKojaNzNNLcHGCBIZfJ5bjNQS-0anx_xgtAA-k3JWOzVlcByX/exec"
TIME_URL = "https://timeapi.io/api/Time/current/zone?timeZone=Europe/London"

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
bme = bme280.BME280(i2c=i2c)

def getTime(): 
    res = urequests.get(TIME_URL) # gets the time
    t = json.loads(res.text)["dateTime"]
    res.close()
    return t

def connectWiFi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        wlan.connect(SSID, PASSWORD)
        while not wlan.isconnected():
            print("Connecting...")
            time.sleep(1)
    print("Connected:", wlan.ifconfig())
    return wlan

def sendToSheet(timestamp, temp, press, hum): # here it creates the url
    url = (
        f"{SCRIPT_URL}"
        f"?time={timestamp}"
        f"&temp={temp}"
        f"&press={press}"
        f"&hum={hum}"
    )
    print("Sending:", url)
    res = urequests.get(url)
    res.close()
    gc.collect()

wlan = connectWiFi()

for i in range(20):
    try:
        ts = getTime()
        t, p, h = bme.values # makes sure the values have units
        t_clean = t.replace('C', '')
        p_clean = p.replace('hPa', '')
        h_clean = h.replace('%', '')
        print(f"{i+1}: {ts}  T={t_clean}  P={p_clean}  H={h_clean}")
        sendToSheet(ts, t_clean, p_clean, h_clean)
    except Exception as e:
        print("Error during loop:", e)
    time.sleep(5)
