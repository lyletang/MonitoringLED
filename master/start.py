#!coding:utf-8
import threading
import os


def func1():
	cmd = 'rsh -l pi 192.168.1.108 "cd ~/MonitoringLED/slave && nohup python index.py &"'
	os.system(cmd)
def func2():
	cmd = 'rsh -l pi 192.168.1.109 "cd ~/MonitoringLED/slave && nohup python index.py &"'
	os.system(cmd)
def func3():
	cmd = 'rsh -l pi 192.168.1.102 "cd ~/MonitoringLED/slave && nohup python index.py &"'
	os.system(cmd)
def func4():
	cmd = 'rsh -l pi 192.168.1.103 "cd ~/MonitoringLED/slave && nohup python index.py &"'
	os.system(cmd)
def func5():
	cmd = 'python index.py'
	os.system(cmd)
	
t1 = threading.Thread(target = func1, args=())
t2 = threading.Thread(target = func2, args=())
t3 = threading.Thread(target = func3, args=())
t4 = threading.Thread(target = func4, args=())
t5 = threading.Thread(target = func5, args=())

threads = []
threads.append(t1)
threads.append(t2)
threads.append(t3)
threads.append(t4)
threads.append(t5)

for thread in threads:
	thread.start()

while True:
	 pass
