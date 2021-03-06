from machine import Pin, sleep, I2C
from acceleration import startScan
from speed import calcDeltaT, lastTime, currentTime, deltaT
# from mpu6050 import MPU
from SSD1306 import *

oled_width = 128
oled_height = 64

# interrupt pin und handler
interruptPin = Pin(25, Pin.IN, pull=Pin.PULL_UP)
interruptHandler = interruptPin.irq(handler=calcDeltaT,
                                    trigger=Pin.IRQ_FALLING)

# i2c bus 
i2c = I2C(1, scl=Pin(22), sda=Pin(21), freq=400000)

# acceleration sensor
# mpu = MPU(i2c = i2c)
oled = SSD1306_I2C(oled_width, oled_height, i2c, addr=60) 

def printText(oled, text, x=0, y=0, col=1):

    oled.text(text, 0, 0)
    oled.show()
# main logic to keep track 


