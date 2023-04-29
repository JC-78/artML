import time
import board
import csv
import adafruit_ens160
import adafruit_bmp280

i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller

ens160 = adafruit_ens160.ENS160(i2c)

# Set the temperature compensation variable to the ambient temp
# for best sensor calibration
ens160.temperature_compensation = 25
# Same for ambient relative humidity
ens160.humidity_compensation = 50

bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)

# Set the sea level pressure value (in hPa)
bmp280.sea_level_pressure = 1013.25

# Create a CSV file and write header
with open('sensor_data1.csv', 'w', newline='') as csvfile:
    fieldnames = ['AQI', 'TVOC', 'eCO2', 'Temperature', 'Pressure', 'Altitude', 'Label']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    while True:
        aqi = ens160.AQI
        tvoc = ens160.TVOC
        eCO2 = ens160.eCO2
        temperature = bmp280.temperature
        pressure = bmp280.pressure
        altitude = bmp280.altitude
        label = "ambient"
        
        # Write sensor readings to CSV file
        writer.writerow({'AQI': aqi, 'TVOC': tvoc, 'eCO2': eCO2, 'Temperature': temperature, 'Pressure': pressure, 'Altitude': altitude, 'Label': label})

        print("Temperature:", temperature)
        print("Pressure:", pressure)
        print("Altitude:", altitude)
        print("AQI (1-5):", aqi)
        print("TVOC (ppb):", tvoc)
        print("eCO2 (ppm):", eCO2)
        print("Label:", label)
        print()

        # sampling at 5Hz
        time.sleep(0.20)