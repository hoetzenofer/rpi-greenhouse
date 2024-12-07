# main.py

import RPi.GPIO as GPIO
import time as t

GPIO.setmode(GPIO.BCM)

def set_state(pin: int, state: bool):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH if state == True else GPIO.LOW)

set_state(17, True)
t.sleep(3)

GPIO.cleanup()

