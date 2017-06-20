import RPi.GPIO as GPIO
import time

RED = 33
GREEN = 35
BLUE = 37

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)
GPIO.output(BLUE,GPIO.HIGH)
GPIO.output(RED,GPIO.HIGH)

p = GPIO.PWM(GREEN,100)
p.start(100)

a = range(0,101,4)
a += range(96,0,-4)
while True:
	for dc in a:
		p.ChangeDutyCycle(dc)
		time.sleep(0.05)




