# -*- coding: utf8 -*-
__author__ = 'Lrony'
from weather import Weather
from config import _get_yaml
from pushbear import sendPushBear

import datetime
import time


conf = _get_yaml()
tips = conf['tips']
debug = conf['set']['debug']

weather = Weather()

while True:
	now = datetime.datetime.now()
	nowStr = str(now.hour) + ':' + str(now.minute)
	# print('debug >>> {}'.format(nowStr))
	index = 0

	for tip in tips:
		if tip['time'] == nowStr:

			message = ''
			# first send
			if index == 0:
				# print('debug >>> {}'.format('first'))
				message = '### 天气状况\n\n'
				message = (message + weather.getWeather() + '\n\n')

			message = (message + '### 喝水进度（' + str(index) + '/' + str(len(tips)) + '）\n\n')
			message = (message + tip['msg'] + '\n\n')

			if debug:
				print('debug >>> {}'.format(message))
			else:
				sendPushBear(message)
			# oneMinute >
			time.sleep(61)
			break

		index += 1


	# print('debug >>> {}'.format('sleep'))
	time.sleep(2)