import RPi.GPIO as GPIO
import time
import subprocess

GPIO.setmode(GPIO.BCM)
PIR = 7
GPIO.setup(PIR, GPIO.IN)

try:
    print("PIR Module Test")
    print(" (CTRL+C to exit)")
    time.sleep(2)
    print "Ready"
    while True:
        if GPIO.input(PIR):
            print("Motion detected! ")
            subprocess.call(["aplay", "1728.wav"], shell = False)
        print ("detection")
        time.sleep(3)
except KeyboardInterrupt:
    print("Quitting")
    GPIO.cleanup()
