# -*- coding: utf8 -*-
__author__ = 'Lrony'
from weather import Weather
from config import _get_yaml
from pushbear import sendPushBear

import datetime
import time


conf = _get_yaml()
debug = conf['set']['debug']
sended = False

if __name__ == '__main__':
	print('start...')
	weather = Weather()
	hour = conf['set']['hour']
	while True:
		now = datetime.datetime.now()
		if sended == False and now.hour == hour:
			message = weather.getWeather()
			if message != None and debug == False:
				sendPushBear(message)
			else:
				print('debug >>> {}'.format(message))
			sended = True
		elif now.hour != hour:
			sended = False
		
		time.sleep(5)