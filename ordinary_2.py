#coding=gb2312
import pygame,random,time
from settings import Settings
ai_settings=Settings()
#����ڶ�����ͨ�ϰ�
class Ordinary_2():
	def __init__(self,screen):
		self.screen=screen
		#�����һ����ͨ�ϰ���ͼ�񡢾���
		self.image=pygame.image.load('images/common.png')
		self.rect=self.image.get_rect()
		#�������ڣ�50��100���������
		self.rect.centerx=random.randrange(400,500)
		#������Ϊ��400��500���������
		self.rect.centery=random.randrange(400,500)
		self.y=float(self.rect.y)
	
	#���������ͨ�ϰ�����ֵ���꺯��	
	def update_hei(self,screen):
		#�����ͨ�ϰ�������Ļ���ˣ���ô��ͨ�ϰ���������ص���Ļ�׶ˣ�ˮƽ���������ȡ
		if self.rect.top<0:
			self.y=600
			self.rect.y=self.y
			self.rect.centerx=random.randrange(200,400)
		
		#�����ͨ�ϰ���û�е�����Ļ���ˣ���ô��ͨ�ϰ��ͻ���bar_hei_speed_factor���ٶ�������	
		else:
			self.y-=ai_settings.bar_hei_speed_factor
			self.rect.y=self.y
			
	
			
	def blitme(self):
		self.screen.blit(self.image,self.rect)
		
