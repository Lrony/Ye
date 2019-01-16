# -*- coding: utf8 -*-
__author__ = 'Lrony'
from config import _get_yaml
import requests


conf = _get_yaml()
pushbear_api = conf['pushbear']['api'].strip()
pushbear_key = conf['pushbear']['key'].strip()
pushbear_title = conf['pushbear']['title'].strip()

def sendPushBear(msg):
	if pushbear_key == '':
		print('pushbear error >>> pushbear pushbear_key error')
		return

	url = '{}?sendkey={}&text={}&desp={}'.format(pushbear_api, pushbear_key, pushbear_title, msg)
	try:
		response = requests.get(url)
		if response.status_code == 200:
			print('pushbear send success >>> {}'.format(msg))
		else:
			print('pushbear network error >>> {}'.format(response.status_code))
	except Exception as e:
		print('pushbear error >>> {}'.format(e))