#coding=gb2312
import pygame
#�����
class Stick():
	def __init__(self,screen):
		self.screen=screen
		#����̵�ͼ�񡢾���
		self.image=pygame.image.load('images/stick_2.png')
		self.rect=self.image.get_rect()
		#����̵�λ��
		self.rect.centerx=300
		self.rect.top=0
		
	def blitme(self):
		self.screen.blit(self.image,self.rect)
