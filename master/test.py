#!coding:utf-8
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(37,GPIO.OUT)
GPIO.output(33,GPIO.HIGH)
GPIO.output(35,GPIO.HIGH)
GPIO.output(37,GPIO.HIGH)
GPIO.cleanup()

