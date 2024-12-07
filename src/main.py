# main.py

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

def set_state(pin: int, state: bool):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH if state == True else GPIO.LOW)

    GPIO.cleanup()

set_state(17, True)
