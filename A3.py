from machine import Pin, I2C
import bme280
import time

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
bme = bme280.BME280(i2c=i2c)

for i in range(10):
    t, p, h = bme.values
    timestamp = time.time() 
    print(f"{i+1}: ts={timestamp}  T={t}  P={p}  H={h}")
    time.sleep(2)