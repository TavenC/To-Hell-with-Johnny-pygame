#coding=gb2312
import pygame,random,time
from settings import Settings
ai_settings=Settings()
class Ordinary_3():
	def __init__(self,screen):
		self.screen=screen
		#�����һ����ͨ�ϰ���ͼ�񡢾���
		self.image=pygame.image.load('images/common.png')
		self.rect=self.image.get_rect()
		#������Ϊ��300��350���ڵ�һ�������
		self.rect.centerx=random.randrange(250,400)
		#������Ϊ��100��200����һ�������
		self.rect.centery=random.randrange(200,300)
		self.y=float(self.rect.y)
	
	#���������ͨ�ϰ�����ֵ���꺯��
	def update_hei(self,screen):
		#�����ͨ�ϰ�������Ļ���ˣ���ô��ͨ�ϰ���������ص���Ļ�׶ˣ�ˮƽ���������ȡ
		if self.rect.top<0:
			self.y=600
			self.rect.y=self.y
			self.rect.centerx=random.randrange(50,80)
		
		#�����ͨ�ϰ���û�е�����Ļ���ˣ���ô��ͨ�ϰ��ͻ���bar_hei_speed_factor���ٶ�������
		else:
			self.y-=ai_settings.bar_hei_speed_factor
			self.rect.y=self.y
		
			
			
		
	def blitme(self):
		self.screen.blit(self.image,self.rect)

