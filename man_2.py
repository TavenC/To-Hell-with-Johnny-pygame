#coding=gb2312
import pygame
from settings import Settings
ai_settings=Settings()
#�������2
class Man_2():
	def __init__(self,screen):
		self.screen=screen
		#�����˲���ȡͼ�񡢾��Σ�����ҵĳ�ʼλ��Ϊ��Ļ������·�
		self.image=pygame.image.load('images/man.bmp')
		self.rect=self.image.get_rect()
		self.screen_rect=screen.get_rect()
		self.rect.centerx=self.screen_rect.centerx
		self.rect.centery=550
		
		self.y=float(self.rect.y)
		self.x=float(self.rect.x)
		
		#��ҳ�ʼ״̬�Ǿ�ֹ��
		self.moving_right=False
		self.moving_left=False
		self.moving_up=False
		self.moving_down=False
	
	#���庯��������ҵĺ�����	
	def update_wid(self):
		#�������������ƶ�������û��Խ����Ļ���Ҷˣ�����Ҽ��������ƶ�
		if self.moving_right and self.rect.right<self.screen_rect.right:
			self.rect.centerx+=ai_settings.man_wid_speed_factor
		#�������������ƶ�������û��Խ����Ļ����ˣ�����Ҽ��������ƶ�
		elif self.moving_left and self.rect.left>0:
			self.rect.centerx-=ai_settings.man_wid_speed_factor
	
	#���庯������������ʼ�ϰ������λ��				
	def update_hei(self,initial_ordinary):
		#������λ���ڳ�ʼ�ϰ�֮�ڣ���ô��Һͳ�ʼ�ϰ�һ������������Ծ�ֹ��
		if initial_ordinary.rect.left<self.rect.right<initial_ordinary.rect.right:
			self.y-=ai_settings.man_hei_speed_factor_up
			self.rect.y=self.y
		#�����ҵ�λ���ڳ�ʼ�ϰ�֮�⣬��ô��Ҿͻ���man_hei_speed_factor_down���ٶ����µ���
		else:
			self.y+=ai_settings.man_hei_speed_factor_down
			self.rect.y=self.y
			
	
			
	#���庯������������������ϰ������λ��		
	def update_hei_1(self,initial_ordinary,ordinary_1,ordinary_2,ordinary_3,macadam_2,conveyer,monster_rect):
		#���ж�������ʼ�ϰ�֮���λ�ã������Ҵӳ�ʼ�ϰ�֮��
		if initial_ordinary.rect.bottom<self.rect.y:
			#���ж���������֮������λ�ã��������ڹ���λ��֮�ϻ���֮��
			if self.rect.bottom<monster_rect.top or self.rect.top>monster_rect.bottom:
				#Ȼ���ж���������������ϰ�֮������λ�ã�
				#�������ڵ�һ����ͨ�ϰ��ķ�Χ֮�ڣ���ô��ҿ���������ϰ��������ƶ�����Ҵ�ֱ�����ϰ�����ͬ�ٶ������˶���
				if ordinary_1.rect.top<self.rect.bottom<ordinary_1.rect.bottom and ordinary_1.rect.left<self.rect.right and self.rect.left<ordinary_1.rect.right:
					self.y-=Settings.man_hei_speed_factor_down+Settings.bar_hei_speed_factor
					self.rect.y=self.y
				#�������ڵڶ�����ͨ�ϰ��ķ�Χ֮�ڣ���ô��ҿ���������ϰ��������ƶ�����Ҵ�ֱ�����ϰ�����ͬ�ٶ������˶���
				elif ordinary_2.rect.top<self.rect.bottom<ordinary_2.rect.bottom and ordinary_2.rect.left<self.rect.right and self.rect.left<ordinary_2.rect.right:
					self.y-=Settings.man_hei_speed_factor_down+Settings.bar_hei_speed_factor
					self.rect.y=self.y
				#�������ڵ�������ͨ�ϰ��ķ�Χ֮�ڣ���ô��ҿ���������ϰ��������ƶ�����Ҵ�ֱ�����ϰ�����ͬ�ٶ������˶���
				elif ordinary_2.rect.top<self.rect.bottom<ordinary_2.rect.bottom and ordinary_2.rect.left<self.rect.right and self.rect.left<ordinary_2.rect.right:
					self.y-=Settings.man_hei_speed_factor_down+Settings.bar_hei_speed_factor
					self.rect.y=self.y
				#����������ʯ�ϰ���Χ֮�ڣ���ô��ҿ�������ϰ��������ƶ�����Ҵ�ֱ�����ϰ�����ͬ�ٶ������˶���
				elif macadam_2.rect.top<self.rect.bottom<macadam_2.rect.bottom and macadam_2.rect.left<self.rect.right<macadam_2.rect.right:
					self.y-=Settings.man_hei_speed_factor_down+Settings.bar_hei_speed_factor
					self.rect.y=self.y
				#�������ڴ��ʹ��ķ�Χ֮�ڣ�
				elif conveyer.rect.top<self.rect.bottom<conveyer.rect.bottom and conveyer.rect.left<self.rect.right and self.rect.left<conveyer.rect.right:
					#����ڴ�ֱ�������봫�ʹ�����ͬ���ٶ�������
					self.y-=Settings.man_hei_speed_factor_down+Settings.bar_hei_speed_factor
					self.rect.y=self.y
					#�����ˮƽ��������man_wid_conveyer_factor�����ƶ�
					self.x-=ai_settings.man_wid_conveyer_factor
					self.rect.x=self.x
				#�����Ҿ������κ�һ���ϰ��ķ�Χ֮�ڣ���ô��ҽ�����2*Settings.man_hei_speed_factor_down���ٶ�����
				else:
					self.y+=ai_settings.man_hei_speed_factor_down
					self.rect.y=self.y
			#�����ҵ�����������޵������귶Χ�н���
			else:
				#��������ˮƽ�����������û�н�����Ҳ�������û�д��������ޣ�
				if self.rect.right<monster_rect.left or monster_rect.right<self.rect.left:
					#��ô����������Ϸ�ʽһ���˶�
					if ordinary_1.rect.top<self.rect.bottom<ordinary_1.rect.bottom and ordinary_1.rect.left<self.rect.right<ordinary_1.rect.right:
						self.y-=Settings.man_hei_speed_factor_down+Settings.bar_hei_speed_factor
						self.rect.y=self.y
					elif ordinary_2.rect.top<self.rect.bottom<ordinary_2.rect.bottom and ordinary_2.rect.left<self.rect.right<ordinary_2.rect.right:
						self.y-=Settings.man_hei_speed_factor_down+Settings.bar_hei_speed_factor
						self.rect.y=self.y
					elif macadam_2.rect.top<self.rect.bottom<macadam_2.rect.bottom and macadam_2.rect.left<self.rect.right<macadam_2.rect.right:
						self.y-=Settings.man_hei_speed_factor_down+Settings.bar_hei_speed_factor
						self.rect.y=self.y
					elif conveyer.rect.top<self.rect.bottom<conveyer.rect.bottom and conveyer.rect.left<self.rect.right<conveyer.rect.right:
						self.y-=Settings.man_hei_speed_factor_down+Settings.bar_hei_speed_factor
						self.rect.y=self.y
						self.x-=ai_settings.man_wid_conveyer_factor
						self.rect.x=self.x
					else:
						self.y+=ai_settings.man_hei_speed_factor_down
						self.rect.y=self.y
				#����������޴�������ô��ҵ�������Ϊ650���������
				else:
					self.y=650
					self.rect.y=self.y
					
			
			
			
			
			
			
			
	def update_stick(self,stick):
		if self.rect.top<stick.rect.bottom:
			self.y=650
			self.rect.y=self.y	
			

		
		
	def blitme(self):
		self.screen.blit(self.image,self.rect)
		
	
