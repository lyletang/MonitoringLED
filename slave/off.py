import RPi.GPIO as GPIO
import time
RED = 33
GREEN = 35
BLUE = 37


GPIO.setmode(GPIO.BOARD)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)
GPIO.output(BLUE,GPIO.HIGH)
GPIO.output(RED,GPIO.HIGH)

p = GPIO.PWM(GREEN,100)
p.start(100)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(BLUE, GPIO.OUT)


while True:
	GPIO.output(RED, GPIO.LOW)
	time.sleep(0.1)
	GPIO.output(RED, GPIO.HIGH)
	time.sleep(0.1)
