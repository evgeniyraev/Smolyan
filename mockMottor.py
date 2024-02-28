from time import sleep
import threading
import RPi.GPIO as GPIO

DIR = 16   # Direction GPIO Pin - Blue 
STEP = 21  # Step GPIO Pin - Green
ENABLE = 20  # Step GPIO Pin - Yellow
LED = 17 # Controll led stip 

CW = 1     # Clockwise Rotation - the moon rotation
CCW = 0    # Counterclockwise Rotation

delay = .003

global shouldRotate, direction
shouldRotate = False
direction = CW

global position, stepsPerRevolution, earhPosition
position = -1
stepsPerRevolution = -1
earhPosition = -1

def cw():
    print( "starting cw")
    global direction, shouldRotate
    
    GPIO.output(DIR, CW)
    GPIO.output(ENABLE, GPIO.HIGH)
    GPIO.output(LED, GPIO.LOW)
    shouldRotate = True

def ccw():
    print( "starting ccw")
    global direction, shouldRotate
    
    GPIO.output(DIR, CCW)
    GPIO.output(ENABLE, GPIO.HIGH)
    GPIO.output(LED, GPIO.LOW)
    shouldRotate = True

def stop_rotation():
    print("stopping rotation")
    global shouldRotate
    GPIO.output(LED, GPIO.HIGH)
    shouldRotate = False

def isRotating():
    global shouldRotate
    return shouldRotate

def step():
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DIR, GPIO.OUT)
    GPIO.setup(STEP, GPIO.OUT)
    GPIO.setup(ENABLE, GPIO.OUT)
    GPIO.setup(LED, GPIO.OUT)
    GPIO.output(LED, GPIO.HIGH)

    while True:
        if shouldRotate:
            global position
            if direction == CW:
                position += 1
            elif direction == CCW:
                position -= 1

            GPIO.output(STEP, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STEP, GPIO.LOW)
            sleep(delay)

        elif GPIO.input(ENABLE):
            GPIO.output(ENABLE, GPIO.LOW)
            GPIO.output(LED, GPIO.HIGH)
            sleep(delay*2)

def step_tread():
    thread = threading.Thread(target=step)
    thread.deamon = True
    thread.start()

def listen():
    print("starting tread")
    step_tread()

    
def main():
    listen()
            
if __name__ == "__main__":
    main()

