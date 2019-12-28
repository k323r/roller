import time

# counter function to keep track of the rotations via induction sensor

lastTime = 0
currentTime = 0
deltaT = 0 # used to the time difference between two consecutive signals

def calcDeltaT(Pin):
    global lastTime
    global currentTime
    global deltaT

    currentTime = time.ticks_ms()
    deltaT = (currentTime - lastTime)/1000 # to seconds 
    print(0.2/deltaT)
    lastTime = currentTime


