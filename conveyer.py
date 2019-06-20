# coding=gbk
import pygame, random, sys
from settings import Settings

ai_settings = Settings()


# ���崫�ʹ�
class Conveyers():
    def __init__(self, screen):
        # ���봫�ʹ���ͼ�񡢾���
        self.image = pygame.image.load('images/convey.png')
        self.rect = self.image.get_rect()
        self.screen = screen
        screen_rect = screen.get_rect()
        # �������ǣ�0��100���������
        self.rect.x = random.randrange(200, 400)
        # �������ǣ�0��100���������
        self.rect.y = random.randrange(0, 100)
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    # ���庯�����´��ʹ���������
    def update_hei(self, screen):
        # ������ʹ�������Ļ���ˣ���ô���ʹ�������Ļ�ײ���������������
        if self.rect.top < 0:
            self.y = 600
            self.rect.y = self.y
            self.x = random.randrange(350, 550)
            self.rect.x = self.x
        # ������ʹ�û�г�����Ļ���ˣ���ô���ʹ���bar_hei_speed_factor���ٶ�������
        else:
            self.y -= ai_settings.bar_hei_speed_factor
            self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)
