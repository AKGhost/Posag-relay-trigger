#!/bin/sh
#this is built by Alaskaradar with the help of many others that have come before
#Thank you for your trials and posts online to help me with my project.
import time
import sys
from time import sleep
from socket import *
from select import *
from tkinter import *
import subprocess
import os
import RPi.GPIO as GPIO
import threading
from threading import Thread
import re

Relay1 = [11]
Relay2 = [8]
def setup():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(Relay1, GPIO.OUT, initial=GPIO.HIGH)
	GPIO.setup(Relay2, GPIO.OUT, initial=GPIO.HIGH)
	print "|=====================================================|"
	print "|             ***Station Name or title                |"
	print "|-----------------------------------------------------|"
	print "|                                                     |"
	print "|                Station alert Script                 |"
	print "|                                                     |"
	print "|                    Pin 11 = Relay 1 VQRU            |"
	print "|                    Pin 8 = Relay 1 VFD              |"
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
                if "CHANGEME" in line:
                        print " Siren Triggered"
		        GPIO.output(Relay1, GPIO.LOW);
		        GPIO.output(Relay2, GPIO.LOW);
		        timer()

	    for line in rx:
    		if "CHANGEME" in line: 
			print "Page Received"
			GPIO.output(Relay1, GPIO.LOW);
		        timer()

   	    for line in rx:
                if "CHANGEME" in line:
			print "Victor QRU Page received"
                        GPIO.output(Relay2, GPIO.LOW);
			timer()

	    for line in rx:
               if "CHANGEME" in line:
			print "Relay test"
			GPIO.output(Relay1, GPIO.LOW);
                        GPIO.output(Relay2, GPIO.LOW);
			print "on"
                        sleep(1.0);
                        GPIO.output(Relay1, GPIO.HIGH);
                        GPIO.output(Relay2, GPIO.HIGH);
			print "off"
			sleep(1.0);
			GPIO.output(Relay1, GPIO.LOW);
                        GPIO.output(Relay2, GPIO.LOW);
                        print "on"
			sleep(1.0);
                        GPIO.output(Relay1, GPIO.HIGH);
                        GPIO.output(Relay2, GPIO.HIGH);
			print "off"
                        print " "
                        print "System Standing By....."			
                        main()

def timer():
	for remaining in xrange (120, 0, -1):
	    sys.stdout.write(str(remaining)+' Seconds Remaining.\r')
	    sys.stdout.flush()
	    time.sleep(1)

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
