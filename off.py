import RPi.GPIO as GPIO
import time
RED = 33
GREEN = 35
BLUE = 37



GPIO.setmode(GPIO.BOARD)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)


while True:
	GPIO.output(RED, GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(RED, GPIO.LOW)
	time.sleep(0.5)
