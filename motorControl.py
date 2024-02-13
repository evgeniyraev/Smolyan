from time import sleep
import RPi.GPIO as GPIO

DIR = 16   # Direction GPIO Pin - Blue 
STEP = 21  # Step GPIO Pin - Green
ENABLE = 20  # Step GPIO Pin - Yellow

CW = 1     # Clockwise Rotation - the moon rotation
CCW = 0    # Counterclockwise Rotation
SPR = 15_000   # Steps per Revolution (360 / 7.5)

#delay = .0208
delay = .010


def rotate():
    print( "starting rotation")
    
    step_count = SPR
    

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DIR, GPIO.OUT)
    GPIO.setup(STEP, GPIO.OUT)
    GPIO.setup(ENABLE, GPIO.OUT)

    GPIO.output(DIR, CW)
    #GPIO.output(DIR, CCW)

    GPIO.output(ENABLE, GPIO.HIGH)

    for x in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)

    GPIO.cleanup()


#GPIO.output(DIR, CCW)
#for x in range(step_count):
#    GPIO.output(STEP, GPIO.HIGH)
#    sleep(delay)
#    GPIO.output(STEP, GPIO.LOW)
#    sleep(delay)
