from machine import Pin, sleep

# micropython.alloc_emergency_exception_buf(100)

counter = 0
interruptPin = Pin(25, Pin.IN, pull=Pin.PULL_UP)

def count(Pin):
    global counter
    counter += 1

interruptHandler = interruptPin.irq(handler=count, trigger=Pin.IRQ_FALLING)

while True:
    print (counter/5)
    sleep(1)
