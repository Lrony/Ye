# -*- coding: utf8 -*-
__author__ = 'Lrony'
from config import _get_yaml
import requests
import urllib


conf = _get_yaml()
pushbear_key = conf['pushbear']['key'].strip()
pushbear_title = conf['pushbear']['title'].strip()

def sendPushBear(msg):
	if pushbear_key == '':
		print('pushbear error >>> pushbear pushbear_key error')
		return

	try:
		data = {'sendkey': pushbear_key, 'text': pushbear_title, 'desp': msg}
		response = requests.get('https://pushbear.ftqq.com/sub', params=data)
		if response.status_code == 200:
			print('pushbear send success >>> {}'.format(msg))
		else:
			print('pushbear network error >>> {}'.format(response.status_code))
	except Exception as e:
		print('pushbear error >>> {}'.format(e))