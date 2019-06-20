# coding=gb2312
import pygame
from man import Man
from settings import Settings

ai_settings = Settings()


# �����ʼ�ϰ�
class Initial_Ordinary():
    def __init__(self, ai_settings, screen, man):
        self.screen = screen
        self.image = pygame.image.load('images/common.png')  # ����ͼ��
        self.rect = self.image.get_rect()  # ��ȡ����
        self.rect.centerx = man.rect.centerx  # ����Ϸ��ʼʱ���վ�ڳ�ʼ�ϰ�������
        self.rect.top = man.rect.bottom
        self.y = float(self.rect.y)

    def update_hei(self):
        self.y -= ai_settings.bar_hei_speed_factor  # ���ϰ�����������bar_hei_speed_factor���ٶ��˶�
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)
