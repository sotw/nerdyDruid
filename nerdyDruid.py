import os, sys
from os.path import expanduser
import argparse
import logging
import RPi.GPIO as GPIO
import time

global DB
global args
global ARGUDB

ARGUDB = []

def signupGPIO():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(31,GPIO.OUT)
    GPIO.setup(33,GPIO.OUT)
    GPIO.setup(35,GPIO.OUT)
    GPIO.setup(37,GPIO.OUT)
    GPIO.output(31,GPIO.HIGH)
    GPIO.output(33,GPIO.HIGH)
    GPIO.output(35,GPIO.HIGH)
    GPIO.output(37,GPIO.HIGH)
    print "Now doing some relay test..."
    print "relay 1 ON"
    GPIO.output(31,GPIO.LOW)
    time.sleep(1)
    GPIO.output(31,GPIO.HIGH)
    print "relay 2 ON"
    GPIO.output(33,GPIO.LOW)
    time.sleep(1)
    GPIO.output(33,GPIO.HIGH)
    print "relay 3 ON"
    GPIO.output(35,GPIO.LOW)
    time.sleep(1)
    GPIO.output(35,GPIO.HIGH)
    print "relay 4 ON"
    GPIO.output(37,GPIO.LOW)
    time.sleep(1)
    GPIO.output(37,GPIO.HIGH)
    print "now all ON"
    GPIO.output(31,GPIO.LOW)
    GPIO.output(33,GPIO.LOW)
    GPIO.output(35,GPIO.LOW)
    GPIO.output(37,GPIO.LOW)
    print "now all OFF"
    GPIO.output(31,GPIO.HIGH)
    GPIO.output(33,GPIO.HIGH)
    GPIO.output(35,GPIO.HIGH)
    GPIO.output(37,GPIO.HIGH)

def doStuff(tTarget):
    print "Hi"

def setup_logging(level):
	global DB
	DB = logging.getLogger('get_jpnews') #replace
	DB.setLevel(level)
	handler = logging.StreamHandler(sys.stdout)
	handler.setFormatter(logging.Formatter('%(module)s %(levelname)s %(funcName)s| %(message)s'))
	DB.addHandler(handler)

def verify():
	global tTarget
	global args
	parser = argparse.ArgumentParser(description='A nerdy druid plan')
	parser.add_argument('-v', '--verbose', dest='verbose', action = 'store_true', default=False, help='Verbose mode')
	parser.add_argument('query', nargs='*', default=None)
	parser.add_argument('-d', '--database', dest='database', action = 'store', default='/.nerdyDruid/nerdyDruid.db') #replace
	args = parser.parse_args()
	tTarget = ' '.join(args.query)
	log_level = logging.INFO
	if args.verbose:
		log_level = logging.DEBUG
	if not tTarget:
		parser.print_help()
		exit()
	setup_logging(log_level)

def loadDb():
	home = expanduser('~')
	if os.path.isfile(home+args.database) is True:
		f = open(home+args.database,'r')
		if f is not None:
			for line in f :
				if line != '\n' and line[0] != '#':
					line = line.rstrip('\n')
					global ARGUDB
					ARGUDB.append(line)
		f.close()
	else:
		DB.debug('override file is not exist')

def main():
    signupGPIO()
    doStuff(tTarget)



if __name__ == '__main__':
	verify()
	loadDb()
	main()
