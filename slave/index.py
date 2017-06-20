#coding: utf-8
#Priject: Monitoring the RaspberryPi cluster with LED's.
#Node: The worker nodes
#Author: Jiahui Tang
#Date: 2017-06-19

import threading
import time
import os
import RPi.GPIO as GPIO

RED = 33
GREEN = 35
BLUE = 37

master_ip = '192.168.1.100'



def GPIO_init():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(RED, GPIO.OUT)
	GPIO.setup(BLUE, GPIO.OUT)
	GPIO.output(RED,GPIO.HIGH)
	GPIO.output(BLUE,GPIO.HIGH)
	GPIO.setup(GREEN, GPIO.OUT)
	p = GPIO.PWM(GREEN,100)
	p.start(100)


def gpio_init(func):
	def func():
		GPIO_init()
		GPIO.cleanup()
		GPIO_init()
		func()
	
	return func

#GPIO.cleanup()
@gpio_init
def GPIO_cleanup():
	GPIO.output(RED,GPIO.HIGH)
	GPIO.output(GREEN,GPIO.HIGH)
	GPIO.output(BLUE,GPIO.HIGH)


def on():
	cmd = 'python on.py &'
	os.system(cmd)

def run():
	cmd = 'python run.py &'
	os.system(cmd)

def off():
	cmd = 'python off.py &'
	os.system(cmd)

#the function of killing the process
def kill_process(process):
	ps_cmd = 'ps -ef | grep python | grep' + ' ' + process
	lists = os.popen(ps_cmd).readlines()
	for i in lists:
		print i
		tmp = i.split()
		if 'grep' not in tmp:
			pid = tmp[1]
			kill_cmd = 'kill -9' + ' ' + pid
			print kill_cmd
			os.system(kill_cmd)

def kill_other(process):
	if len(os.popen('ps -ef | grep python | grep {process}'.format(process = process)).readlines()) < 2:
		pass
					
	else:
		kill_process(process)
		GPIO_cleanup()

def main():
	try:
		while True:
			ping_cmd = 'ping -c 1 -W 1 -v {ip_address}'.format(ip_address = master_ip)

			#if success
			if not os.system(ping_cmd):
				
				#'free' status
				if len(os.popen('ps -ef | grep spark://Worker').readlines()) < 3:
					
					#test print, the node is free
					print 'free'
					
					#if have no process of 'on' status
					if len(os.popen('ps -ef | grep python | grep on.py').readlines()) < 2:
						
						#kill the process of 'run' status
						if len(os.popen('ps -ef | grep python | grep run.py').readlines()) < 2:
							pass
					
						else:
							kill_process('run.py')
							GPIO.cleanup()
							GPIO_init()
						
						#kill the process of 'off' status
						if len(os.popen('ps -ef | grep python | grep off.py').readlines()) < 2:
							pass
						
						else:
							kill_process('off.py')
							GPIO.cleanup()
							GPIO_init()
						on()

					else:
						pass

				#'run' status
				else:
					
					#test print, the node is run
					print 'run'
					
					#if have no process of 'run' status
					if len(os.popen('ps -ef | grep python | grep run.py').readlines()) < 2:
						
						#kill the process of 'on' status
						if len(os.popen('ps -ef | grep python | grep on.py').readlines()) < 2:
							pass

						else:
							print 'in'
							kill_process('on.py')
							GPIO.cleanup()
							GPIO_init()

						#kill the process of 'off' status
						if len(os.popen('ps -ef | grep python | grep off.py').readlines()) < 2:
							pass
						
						else:
							kill_process('off.py')
							GPIO.cleanup()
							GPIO_init()

						run()

					else:
						pass

			#'off' status
			else:
				
				#test print, the node can't connect to the cluster master
				print 'off'
				
				#if have no process of 'off' status
				if len(os.popen('ps -ef | grep python | grep off.py').readlines()) < 2:
					
					#kill the process of 'on' status
					if len(os.popen('ps -ef | grep pytho | grep on.py').readlines()) < 2:
						pass

					else:
						kill_process('on.py')
						GPIO.cleanup()
						GPIO_init()

					#kill the process of 'run' status
					if len(os.popen('ps -ef | grep pytho | grep run.py').readlines()) < 2:
						pass

					else:
						kill_process('run.py')
						GPIO.cleanup()
						GPIO_init()

					off()

				else:
					pass

	except Exception, e:
		with open('monitor.log', 'a') as log:
#			log.write(e)
			pass

if __name__ == '__main__':
	main()
