#This is a test script for lighting led from raspberry pi.

import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7,GPIO.OUT)

for x in range(0,5):

GPIO.output(7,True)

time.sleep(2)

GPIO.output(7,False)

time.sleep(2)

GPIO.cleanup() 