#coding=gb2312
from win32api import GetSystemMetrics
import os
#�õ���Ļ��С
SCREENWIDTH = GetSystemMetrics (0)
SCREENHEIGHT = GetSystemMetrics (1)

class Settings():
	def __init__(self):
		#��Ļ���Ϊ400
		self.screen_width=500
		#��Ļ�߶�Ϊ600
		self.screen_height=600
		os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % ((SCREENWIDTH-self.screen_width)/2,(SCREENHEIGHT-self.screen_height)/2)
		self.bg_color=(255,255,255)
		#���ˮƽ�ƶ��ٶ�Ϊ8
		self.man_wid_speed_factor=8
		#����ڴ��ʹ��ϵ�ˮƽ�ٶ�
		self.man_wid_conveyer_factor=4
		
		  		
		
		
