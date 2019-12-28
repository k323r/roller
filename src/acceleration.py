from machine import Pin, I2C

def startScan(i2c):
    res = i2c.scan()
    for r in res:
        print(r)


