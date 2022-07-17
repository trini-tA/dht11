from machine import Pin, I2C
import ssd1306
import dht
import utime as time
from screen import Screen

VERSION = "0.1"
NAME = "Temp"
DISPLAY_NAME = NAME + " " + VERSION
PIN_TEMP = 2                # on board -> D4
#screen
PIN_OLED_SCL = 5            # on board -> D1
PIN_OLED_SDA = 4            # on board -> D2

# using default address 0x3C
i2c = I2C(sda=Pin(PIN_OLED_SDA), scl=Pin(PIN_OLED_SCL))
display = ssd1306.SSD1306_I2C(64, 48, i2c)
Screen.start_screen( display, DISPLAY_NAME )
time.sleep(2)
Screen.clear_screen( display, DISPLAY_NAME )

# measure
d = dht.DHT11(Pin(PIN_TEMP, Pin.IN, Pin.PULL_UP))
count = 0
while True:
    display.text(DISPLAY_NAME, 0, 0, 1)

    try:
        d.measure()

        temp = d.temperature()
        hum = d.humidity()

        count = count + 1
        Screen.print_screen_dht11( display, temp, hum, count )

    except:
        output = 'ERR!!'
        display.text(output, 0, 40, 1)

    time.sleep(2)
    Screen.clear_screen( display, DISPLAY_NAME )