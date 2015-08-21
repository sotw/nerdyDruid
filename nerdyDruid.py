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

#[]== repeat_to_length
def r2len(string_to_expand, length):
	return (string_to_expand * ((length/len(string_to_expand))+1))[:length]

chan_list = [31,33,36,37]

def selftesting(chans):
	DB.info('doing seltesting...')
	for chan in chans:
		DB.info('test ping %d' %(chan))
		GPIO.output(chan, GPIO.LOW)
		time.sleep(3)
		GPIO.output(chan, GPIO.HIGH)

#doing initialize in old fashion
def regOneGPIOoutLowAct(num):
	#DB.info('%s' %(r2len('-',40)))
	DB.info('reg GPIO pin %d' %(num))
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(num,GPIO.OUT) #you know, you can directly setup a matrix
	GPIO.output(num,GPIO.HIGH)
	DB.debug('self testing...')
	DB.debug('output low')
	GPIO.output(num,GPIO.LOW)
	time.sleep(3)
	DB.debug('output high')
	GPIO.output(num,GPIO.HIGH)

#[]== should use matrix to define and initialize all items
def signupGPIO():
	#regOneGPIOoutLowAct(31)
	os.system('clear')
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(chan_list,GPIO.OUT)
	selftesting(chan_list)
	os.system('clear')

def doStuff(tTarget):
	DB.info('Let\'s start a wonderful nerdyDruid day and try to survive in post-apocalypse')

def setup_logging(level):
	global DB
	DB = logging.getLogger('nerdyDruid') #replace
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
