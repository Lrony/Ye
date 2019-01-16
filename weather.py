# -*- coding: utf8 -*-
__author__ = 'Lrony'
from pushbear import sendPushBear
from template import templates
from config import _get_yaml

import requests
import random
import json
import sys


class Weather(object):
	
	def __init__(self):
		reload(sys)
		sys.setdefaultencoding('utf8')
		conf = _get_yaml()

		self.city_code = conf['city']['code'].strip()
		self.city_name = conf['city']['name'].strip()
		self.send_name = conf['set']['send_name'].strip()
		self.receive_name = conf['set']['receive_name'].strip()

	def getWeather(self):
		url = 'http://t.weather.sojson.com/api/weather/city/{}'.format(self.city_code)
		response = requests.get(url)
		if response.status_code == 200:
			result = json.loads(response.text)
			weatherType = result.get('data').get('forecast')[0].get('type')
			ymd = result.get('data').get('forecast')[0].get('ymd')
			template = templates[random.randint(0,len(templates) - 1)]

			if weatherType == '晴' or weatherType == '晴转多云' or weatherType == '多云':
				message = '{}今天是{} 天气是{} ，天气真好，就好像我对{}一样！记得带伞，别晒黑了哦'.format(template, ymd, weatherType, self.receive_name)
			elif weatherType == '阴':
				message = '{}今天是{} 天气是{}，天气一般，{}呆在家里好好追剧最好'.format(template, ymd, weatherType, self.receive_name)
			elif weatherType == '雾':
				message = '{}今天是{} 天气是{}，出门眼睛要擦亮哦，提醒{}要看好{}！'.format(template, ymd, weatherType, self.receive_name, self.send_name)
			elif weatherType == '雨夹雪':
				message = '{}今天是{} 天气是{}，把伞带好，{}还是别出门啦，如果硬要出，把家里的皮大衣拿来'.format(template, ymd, weatherType, self.receive_name)
			elif weatherType == '暴雨':
				message = '{}今天是{} 天气是{}，今天不要出去了，太可怕了！'.format(template, ymd, weatherType)
			elif weatherType == '雨' or weatherType == '小雨':
				message = '{}今天是{} 天气是{}，把伞伞伞带好，重要的事情说三遍，雨天路滑，回宿舍当心，路上别看手机'.format(template, ymd, weatherType)
			elif weatherType == '大雪':
				message = '{}今天是{} 天气是{}，呆在家里多暖和，起什么床呀！来呀，快活啊，反正有大把时光！'.format(template, ymd, weatherType)
			elif weatherType == '冰雹':
				message = '{}今天是{} 天气是{}，安全第一，在家里好好呆着，{}冒死也会给{}弄吃的'.format(template, ymd, weatherType, self.send_name, self.receive_name)
			else:
				message = '{}今天是{} 天气是{}，这是一个未收录的天气状况，快提醒{}改代码！'.format(template, ymd, weatherType, self.send_name)

			return message
		else:
			print('weather network error >>> {}'.format(response.status_code))
			return None