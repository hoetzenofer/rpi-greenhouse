# main.py

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pin = 7
GPIO.setup(pin, GPIO.OUT)

try:
    while True:
        GPIO.output(pin, GPIO.HIGH)
        print("Pin eingeschaltet")
        time.sleep(5)
        
        GPIO.output(pin, GPIO.LOW)
        print("Pin ausgeschaltet")
        time.sleep(5)

except KeyboardInterrupt:
    print("Programm beendet")

finally:
    GPIO.cleanup()

