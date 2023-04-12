import time
import board
import adafruit_ens160
import adafruit_bmp280

i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller

ens = adafruit_ens160.ENS160(i2c)

# Set the temperature compensation variable to the ambient temp
# for best sensor calibration
ens.temperature_compensation = 25
# Same for ambient relative humidity
ens.humidity_compensation = 50

bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)

# Set the sea level pressure value (in hPa)
bmp280.sea_level_pressure = 1013.25

while True:
    
    print("Temperature:", bmp280.temperature)
    print("Pressure:", bmp280.pressure)
    print("Altitude:", bmp280.altitude)
    print("AQI (1-5):", ens.AQI)
    print("TVOC (ppb):", ens.TVOC)
    print("eCO2 (ppm):", ens.eCO2)
    print()

    # new data shows up every second or so
    time.sleep(1)