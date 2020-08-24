#!/bin/sh
#this is built by Alaskaradar with the help of many others that have come before
#Thank you for your trials and posts online to help me with my project.
import time
import sys
from time import sleep
from socket import *
from select import *
from Tkinter import *
import subprocess
import os
import RPi.GPIO as GPIO
import threading
from threading import Thread
import re
import flux_led

Relay1 = [11]
Relay2 = [8]
def setup():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(Relay1, GPIO.OUT, initial=GPIO.HIGH)
	GPIO.setup(Relay2, GPIO.OUT, initial=GPIO.HIGH)
	print "|=====================================================|"
	print "|             ***Victor Fire and EMS                  |"
	print "|-----------------------------------------------------|"
	print "|                                                     |"
	print "|                Station alert Script                 |"
	print "|                                                     |"
	print "|                 LED Light controller                |"
	print "|                                                     |"
	print "|                                                     |"
	print "|                                          Alaskaradar|"
	print "|_____________________________________________________|"
	print "|             System online and Standing by           |"
	print "|_____________________________________________________|"    

def main():
	while True:
            s = socket(AF_INET, SOCK_DGRAM)
	    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
            s.bind(('',50000))
            rx = s.recvfrom(2048)
	    print(rx[0]+'\r')

            for line in rx:
                if "2004099" in line:
                        print "Siren Triggered"
			os.system('python -m flux_led 10.13.38.4 -1')
			os.system('python -m flux_led 10.13.38.4 -C jump 100 "#FF0000 #0000FF" ')
		        timer()

	    for line in rx:
    		if "2004100" in line: 
			print "QRU Page Received"
			os.system('python -m flux_led 10.13.38.4 -1');
			os.system("python -m flux_led 10.13.38.4 -c blue")
		        timer()

   	    for line in rx:
                if "2007519" in line:
			print "Victor Ambulance Page received"
                        os.system('python -m flux_led 10.13.38.4 -1');
			os.system('python -m flux_led 10.13.38.4 -C jump 100 "#FF0000 #00FF00"');
			timer()


def timer():
	for remaining in xrange (120, 0, -1):
	    sys.stdout.write(str(remaining)+' Seconds Remaining.\r')
	    sys.stdout.flush()
	    time.sleep(1)

	os.system("python -m flux_led 10.13.38.4 -0");
	sys.stdout.write("\rSystem Standing By....\n")			
	main()

def destroy():
	GPIO.output(Relay1, GPIO.HIGH)
	GPIO.output(Relay2, GPIO.HIGH)
	GPIO.cleanup()

if __name__ == '__main__':
	setup()
	try:
		main()
	except KeyboardInterrupt:
		destroy()
