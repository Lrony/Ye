# -*- coding: utf8 -*-
__author__ = 'Lrony'
from config import _get_yaml
import sys


reload(sys)
sys.setdefaultencoding('utf8')

conf = _get_yaml()
receive_name = conf['set']['receive_name'].strip()

templates = [
    '新的一天又来啦，给{}念早安早安早安，重要的事情说三遍，'.format(receive_name),
    '早安哦，{}快起床啦，'.format(receive_name),
    '坚持不懈的给{}奉上早安，我是不会忘记的，'.format(receive_name),
    '早晨，是一个美妙的开端，{}早安哦，'.format(receive_name),
    '{}，我有一千种给你说早安的方式，今天第一千种，'.format(receive_name),
    '每天都是改变命运的机会，{}，早安呐，'.format(receive_name),
    '早安，太阳，早安，地球，早安，中国，早安，亲爱的{}，快起来了，'.format(receive_name),
    '我想告诉全世界的人，你是最漂亮的，早安！{}，'.format(receive_name),
    '太阳冉冉升起，清风柔柔吹起,早安，',
    '让爱你的人放心，让恨你的人失落, 一碗鸡汤请{}喝，早安，'.format(receive_name),
    '我想你一定很忙，所以只看前三个字就好啦，早安呀！',
    '想不出来今天说啥了，嗯，早安，',
    '掀被而起，君临天下,haha，',
    '帅的人已醒 丑的人还在沉睡,丑的是指的我，早安，',
    'good   morning。。。。。',
    '晚安，哦，说错了，是早安，{}，'.format(receive_name)
]
