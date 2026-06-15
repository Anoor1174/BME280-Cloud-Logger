# BME280 Cloud Logger
BME280 Cloud Logger

Real-time environmental monitoring with a Raspberry Pi Pico W and BME280 sensor, logging temperature, humidity, and pressure data to Google Sheets via the Sheets API. Built with MicroPython.


## Overview

This project turns a Raspberry Pi Pico W into a wireless environmental sensor station. Every few seconds it reads temperature, humidity, and atmospheric pressure from a BME280 sensor and pushes the readings to a live Google Sheet — no additional server or cloud infrastructure required.


## Hardware Required

Component	Details
Raspberry Pi Pico W	RP2040 with onboard Wi-Fi (CYW43439)
BME280 Sensor	Temperature, humidity, pressure (I²C)
Breadboard + jumper wires	For prototyping
Micro-USB cable	Power and flashing


## Wiring (I²C)

BME280 Pin  	Pico W Pin
VCC	          3.3V (Pin 36)
GND	          GND (Pin 38)
SDA	          GP4 (Pin 6)
SCL	          GP5 (Pin 7)

## Software Setup

### 1. Flash MicroPython

Download the latest MicroPython .uf2 for Pico W from micropython.org and drag it onto the Pico W while holding BOOTSEL.

### 2. Install Dependencies

Copy the following to your Pico W using Thonny or mpremote:
```
bme280.py        # BME280 driver
urequests.py     # HTTP library for MicroPython
```
### 3. Google Sheets Setup


- Create a new Google Sheet and note the Spreadsheet ID from the URL
- Set up a Google Apps Script Web App to accept POST requests and append rows
- Deploy the script as a web app (access: anyone) and copy the deployment URL


4. Configure config.py
```
pythonWIFI_SSID     = "your_wifi_name"
WIFI_PASSWORD = "your_wifi_password"
SHEET_URL     = "https://script.google.com/macros/s/YOUR_DEPLOYMENT_ID/exec"
LOG_INTERVAL  = 10  # seconds between readings
```

## Usage
```
bash# Upload all files to Pico W, then run:
mpremote run main.py
```
Or set main.py as the boot script so it runs automatically on power-up.

The device will:


- Connect to Wi-Fi
- Initialise the BME280 sensor over I²C
- Read and log data to Google Sheets every LOG_INTERVAL seconds
- Print readings to the serial console for debugging



Sample Output
```
Connected to WiFi: MyNetwork
IP: 123.456.7.89
--- Reading 1 ---
Temperature: 21.4°C
Humidity: 58.2%
Pressure: 1013.2 hPa
Logged to Sheets ✓

```
Project Structure
```
├── main.py          # Main loop — reads sensor, logs to Sheets
├── config.py        # Wi-Fi credentials and Sheets URL
├── bme280.py        # BME280 MicroPython driver
└── urequests.py     # HTTP requests for MicroPython

```
Tech Stack


- Firmware: MicroPython
- Hardware: Raspberry Pi Pico W, BME280
- Cloud: Google Sheets via Apps Script Web App
- Protocol: I²C (sensor), HTTPS (logging)
