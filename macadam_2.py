#coding=gb2312
import pygame,random,time
from settings import Settings
ai_settings=Settings()
#������ʯ
class Macadam_2s():
	def __init__(self,screen):
		self.image=pygame.image.load('images/gravel.png') #��ȡ��ʯͼ��
		self.rect=self.image.get_rect() #��ȡ��ʯ����
		self.screen=screen
		screen_rect=screen.get_rect()
		self.rect.x=random.randrange(350,400) #���������ʯ��ʼ�����꣬��ΧΪ350-400
		self.rect.y=300
		self.y=float(self.rect.y)
		self.x=float(self.rect.x)
		
	def update_hei(self,screen):
		#�����ʯ������Ļ�Ķ���
		if self.rect.top<0:
			#��ô��ʯ��������600������������趨������������������
			self.y=600
			self.rect.y=self.y
			self.x=random.randrange(50,550)
			self.rect.x=self.x
		#�����ʯû�е�����Ļ���ˣ���ô��ʯ�ϰ���������������
		else:
			self.y-=ai_settings.bar_hei_speed_factor
			self.rect.y=self.y
	
	#���庯���ж���ʯ�Ƿ���ʧ		
	def check_collide(self,screen,man,man_2):
		#������1����ʯ�ϣ�
		if self.rect.top<man.rect.bottom<self.rect.bottom and self.rect.left<man.rect.right<self.rect.right:
			#�������м����������ʯ��ĳ����Χ֮�ڣ�centerx-10,centerx+10)
			if self.rect.centerx-10<man.rect.centerx<self.rect.centerx+10:
				#��ô��ʯ�����������̱��600���������������
				self.y=600
				self.rect.y=self.y
				self.rect.x=random.randrange(200,350)
		#������2����ʯ�ϣ�		
		elif self.rect.top<man_2.rect.bottom<self.rect.bottom and self.rect.left<man_2.rect.right<self.rect.right:
			#����������м����������ʯ��ĳ����Χ֮�ڣ�centerx-10,centerx+10)
			if self.rect.centerx-10<man_2.rect.centerx<self.rect.centerx+10:
				#��ô��ʯ�����������̱��600���������������
				self.y=600
				self.rect.y=self.y
				self.rect.x=random.randrange(200,350)
					

			
	def blitme(self):
		self.screen.blit(self.image,self.rect)
		
		
