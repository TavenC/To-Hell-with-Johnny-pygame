# coding=gb2312
import csv
import os
import pygame
import sys
import time

from win32api import GetSystemMetrics

import game_function as gf
from conveyer import Conveyers
from initial_ordinary import Initial_Ordinary
from macadam_2 import Macadam_2s
from man import Man
from man_2 import Man_2
from ordinary_1 import Ordinary_1
from ordinary_2 import Ordinary_2
from ordinary_3 import Ordinary_3
from settings import Settings
from stick import Stick

# ���û����С���ֱ��ʡ���ɫ��
FPS = 300
WINWIDTH = 800
WINHEIGHT = 600
HALF_WINWIDTH = int(WINWIDTH / 2)
HALF_WINHEIGHT = int(WINHEIGHT / 2)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BGCOLOR = WHITE  # ������ɫΪ��ɫ
TEXTCOLOR = BLACK  # ������ɫΪ��ɫ

# �õ���Ļ��С
SCREENWIDTH = GetSystemMetrics(0)
SCREENHEIGHT = GetSystemMetrics(1)

font = pygame.font.SysFont(None, 48)
gameOverSound = pygame.mixer.Sound('gameover.wav')
pygame.mixer.music.load('background.mid')


def main():
    # global��ʾ��Щ�����Ǻ����ⶨ���ȫ�ֱ���
    global FPSCLOCK, IMAGESDICT, BASICFONT, DISPLAYSURF, PARAMETER

    pygame.init()  # ��ʼ��
    # �̶���Ļλ��
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % ((SCREENWIDTH - WINWIDTH) / 2, (SCREENHEIGHT - WINHEIGHT) / 2)
    DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
    # ��ʼ��������ʾ�Ĵ��ڲ����ô��ڳߴ�,��Ϊ800����Ϊ600��������Ϊ��λ
    FPSCLOCK = pygame.time.Clock()  # ���ô���ʱ�Ӷ���(���Կ�����Ϸѭ��Ƶ��)
    pygame.display.set_caption("Lingnan Jump")  # ���ó��򴰿ڵı���
    pygame.font.init()
    BASICFONT = pygame.font.Font('Comici.ttf', 18)  # ����ΪComici���ֺ�Ϊ18��
    pygame.display.flip()

    # IMAGEDICT�����ó�������Ҫ������ͼƬ����
    # IMAGEDICT�����ó�������Ҫ������ͼƬ����
    IMAGESDICT = {'title': pygame.image.load('gametitle.png'),
                  'ordinary': pygame.image.load('images/common.png'),
                  'macadam': pygame.image.load('gravel.png'),
                  'conveyor': pygame.image.load('images/convey.png'),
                  'explanation': pygame.image.load('explain.png'),
                  'smallhelp': pygame.image.load('help.png'),
                  'monster_im': pygame.image.load('images/monster_1.png')}

    PARAMETER = {'coefficient': 1}

    startScreen()


# while True:
# run the game

def startScreen():
    """��ʾ��ʼ����"""

    titleRect = IMAGESDICT['title'].get_rect()  # ���ñ���ͼ��
    topCoord_1 = 35  # topCoord���ڶ�λ�ı�������λ��
    titleRect.top = topCoord_1
    titleRect.centerx = HALF_WINWIDTH
    topCoord_1 += titleRect.height

    SRLRect = IMAGESDICT['explanation'].get_rect()  # ����explanationͼ��
    topCoord_2 = 380
    SRLRect.top = topCoord_2
    SRLRect.centerx = HALF_WINWIDTH
    topCoord_2 += SRLRect.height

    instructionText = ['Press Buttons to Begin',
                       '( 1 - Easy ; 2 - Hard ; 3 - Hell )',
                       'Impairment ratio for final score: Easy - 0.7 ; Hard - 0.8 ; Hell - 1']

    DISPLAYSURF.fill(BGCOLOR)
    # ����ͼ��
    DISPLAYSURF.blit(IMAGESDICT['title'], titleRect)
    DISPLAYSURF.blit(IMAGESDICT['explanation'], SRLRect)

    # ��ӡ�ı���ȷ��λ��
    for i in range(len(instructionText)):
        instSurf = BASICFONT.render(instructionText[i], 1, TEXTCOLOR)
        instRect = instSurf.get_rect()
        topCoord_1 += 8  # ÿ������֮����8������
        instRect.top = topCoord_1
        instRect.centerx = HALF_WINWIDTH
        topCoord_1 += instRect.height  # ����ÿ�еĸ߶�
        DISPLAYSURF.blit(instSurf, instRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # ��������
                from settings import Settings
                ai_settings = Settings()
                if event.key == pygame.K_1:
                    Settings.bar_hei_speed_factor = 5
                    Settings.man_hei_speed_factor_up = 5
                    Settings.man_hei_speed_factor_down = 8
                    PARAMETER['coefficient'] = 0.7
                    run_game()
                elif event.key == pygame.K_2:
                    Settings.bar_hei_speed_factor = 6
                    Settings.man_hei_speed_factor_up = 6
                    Settings.man_hei_speed_factor_down = 6
                    PARAMETER['coefficient'] = 0.8
                    run_game()
                elif event.key == pygame.K_3:
                    Settings.bar_hei_speed_factor = 10
                    Settings.man_hei_speed_factor_up = 10
                    Settings.man_hei_speed_factor_down = 9
                    PARAMETER['coefficient'] = 1
                    run_game()
                return

        # ��DISPLAYSURF������ʾ��ʵ����Ļ
        pygame.display.update()
        FPSCLOCK.tick(FPS)


# ������Ϸ���еĺ���
def run_game():
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))  # ������Ļ����
    monster_image = IMAGESDICT['monster_im']
    monster_rect = monster_image.get_rect()  # ��ȡmonster�ľ���
    monster_rect.bottom = 500  # ����monster��ʼλ��
    monster_rect.right = 50  # ����monster��ʼλ��
    speed = [1, 1]  # monster���ٶȣ�ˮƽ�ٶ�Ϊ1����ֱ�ٶ�Ϊ1
    # �ò�ͬ���������class�������
    man = Man(screen)
    man_2 = Man_2(screen)
    initial_ordinary = Initial_Ordinary(ai_settings, screen, man)
    ordinary_1 = Ordinary_1(screen)
    ordinary_2 = Ordinary_2(screen)
    ordinary_3 = Ordinary_3(screen)
    macadam_2 = Macadam_2s(screen)
    conveyer = Conveyers(screen)
    stick = Stick(screen)
    # ������ҵĳ�ʼ�ɼ�Ϊ0
    score_1 = 0
    score_2 = 0

    pygame.mixer.music.play(-1, 0.0)

    while True:
        monster_rect = monster_rect.move(speed)  # ��monster��λ�ø���speed�ƶ�
        if (monster_rect.left < 0) or (monster_rect.right > 400):  # ���monster��ˮƽλ���ϳ�����Ļ��Χ����ômonster���˶������෴
            speed[0] = -speed[0]
        if (monster_rect.bottom > 600) or (monster_rect.top < 0):  # ���monster����ֱ�����ϳ�������Ļ��Χ����ômonster���˶������෴
            speed[1] = -speed[1]
        screen.blit(monster_image, monster_rect)  # ����Ļ����monster��״̬

        if man.rect.y < 600 or man_2.rect.y < 600:  # ������1�����2��û�д�������Ļ���ˣ�����Ϸ����
            if man.rect.y < 600 and man_2.rect.y < 600:
                score_1 += 0.01 * PARAMETER['coefficient']
                score_2 += 0.01 * PARAMETER['coefficient']

            elif man.rect.y < 600 and man_2.rect.y > 600:  # ������2������Ļ���ˣ������2���������1����
                score_1 += 0.01 * PARAMETER['coefficient']
                score_2 += 0
            elif man.rect.y > 600 and man_2.rect.y < 600:  # ������1��������Ļ���ˣ������1���������2����
                score_1 += 0
                score_2 += 0.01 * PARAMETER['coefficient']

            gf.check_events(ai_settings, screen, man, man_2, score_1, score_2)

            man.update_wid()  # �������1������λ��
            man_2.update_wid()  # �������2������λ��
            man.update_hei(initial_ordinary)  # �������1�ڳ�ʼ�ϰ����˶�����ֱλ��
            man_2.update_hei(initial_ordinary)  # �������2�ڳ�ʼ�ϰ����˶�����ֱλ��
            initial_ordinary.update_hei()  # ���³�ʼ�ϰ���λ��
            ordinary_1.update_hei(screen)  # ���µ�һ����ͨ�ϰ���λ��
            ordinary_2.update_hei(screen)  # ���µڶ�����ͨ�ϰ���λ��
            ordinary_3.update_hei(screen)  # ���µ�������ͨ�ϰ���λ��
            macadam_2.update_hei(screen)  # ������ʯ�ϰ���λ��
            conveyer.update_hei(screen)  # ���´��ʹ���λ��
            man_2.update_hei_1(initial_ordinary, ordinary_1, ordinary_2, ordinary_3, macadam_2, conveyer,
                               monster_rect)  # �������2����ͨ�ϰ�����ʯ�����ʹ����˶�����ֱλ��
            man_2.update_stick(stick)  # �������2��̵����λ��
            man.update_hei_1(initial_ordinary, ordinary_1, ordinary_2, ordinary_3, macadam_2, conveyer,
                             monster_rect)  # �������1����ͨ�ϰ�����ʯ�����ʹ����˶�����ֱλ��
            man.update_stick(stick)  # �������1��̵����λ��
            macadam_2.check_collide(screen, man, man_2)  # ����������ʯ�Ƿ���ײ

            gf.update_screen(ai_settings, screen, man, man_2, initial_ordinary, ordinary_1, ordinary_2, ordinary_3,
                             macadam_2, conveyer, stick)

        else:  # ������1�����2�������������GAME OVER����
            score_1 += 0
            score_2 += 0
            gf.check_events(ai_settings, screen, man, man_2, score_1, score_2)
            gf.drawText_1('GAME OVER', font, screen, (ai_settings.screen_width / 3), (ai_settings.screen_height / 3))
            pygame.display.update()

            pygame.mixer.music.stop()
            gameOverSound.play()
            time.sleep(3)
            score_1 = int(score_1)
            score_2 = int(score_2)

            Scorewinwid = 500
            Scorewinhei = 150
            TEXTCOLOR = (255, 255, 255)
            BACKGROUNDCOLOR = (0, 0, 0)
            pygame.init()
            # �̶���Ļλ��
            os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (
                (SCREENWIDTH - Scorewinwid) / 2, (SCREENHEIGHT - Scorewinhei) / 2)
            ScoreWindow = pygame.display.set_mode((Scorewinwid, Scorewinhei))
            pygame.display.set_caption('Score Save')
            BASICFONT = pygame.font.Font('Comici.ttf', 20)
            gf.drawText_1("Do you want to save this score?", BASICFONT, ScoreWindow, (Scorewinwid / 3),
                          (Scorewinhei / 3) - 10)
            gf.drawText_1("If yes, please press Y !", BASICFONT, ScoreWindow, (Scorewinwid / 3), (Scorewinhei / 3 + 15))
            gf.drawText_1("If no, please press N !", BASICFONT, ScoreWindow, (Scorewinwid / 3), (Scorewinhei / 3 + 40))
            pygame.display.flip()

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_n:
                            sys.exit()
                        elif event.key == pygame.K_y:
                            score_1 = int(score_1)
                            stu1 = ["a", score_1]
                            out_1 = open('Stu1_csv.csv', 'a', newline="")
                            csv_write = csv.writer(out_1, dialect='excel')
                            csv_write.writerow(stu1)
                            print("write over")
                            filename = 'Stu1_csv.csv'
                            with open(filename) as f:
                                reader = csv.reader(f)
                                header_row = next(reader)
                                print(header_row)
                                for index, column_header in enumerate(header_row):
                                    print(index, column_header)
                                scores_1 = [score_1]
                                for row in reader:
                                    new_score = int(row[1])
                                    scores_1.append(new_score)
                                scores_1.remove(score_1)
                                scores_1.append(score_1)
                                print(scores_1)

                            score_2 = int(score_2)
                            stu2 = ["b", score_2]
                            out_2 = open('Stu2_csv.csv', 'a', newline="")
                            csv_write = csv.writer(out_2, dialect='excel')
                            csv_write.writerow(stu2)
                            print("write over")
                            filename_2 = 'Stu2_csv.csv'
                            with open(filename_2) as f:
                                reader = csv.reader(f)
                                header_row = next(reader)
                                print(header_row)
                                for index, column_header in enumerate(header_row):
                                    print(index, column_header)
                                scores_2 = [score_2]
                                for row in reader:
                                    new_score_2 = int(row[1])
                                    scores_2.append(new_score_2)
                                scores_2.remove(score_2)
                                scores_2.append(score_2)
                                print(scores_2)

                            from matplotlib import pyplot as plt
                            fig = plt.figure(dpi=128, figsize=(3, 2))
                            plt.plot(scores_1, c='red', label="score 1")
                            plt.plot(scores_2, c='gray', label="score 1")
                            plt.title("Score", fontsize=18)
                            plt.xlabel = ('')
                            plt.ylabel = ('score')
                            plt.tick_params(axis='both', which='major', labelsize=16)
                            plt.legend(loc=9)
                            plt.savefig('scoreshow.png', bbox_inches='tight')
                            top_score_1 = max(scores_1)
                            top_score_2 = max(scores_2)
                            if top_score_1 > top_score_2:
                                winner = 'Player 1'
                            elif top_score_1 < top_score_2:
                                winner = 'Player 2'
                            else:
                                winner = 'Player 1 and Player 2'
                            WINDOWWIDTH = 800
                            WINDOWHEIGHT = 600
                            pygame.init()
                            # �̶���Ļλ��
                            os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (
                                (SCREENWIDTH - WINDOWWIDTH) / 2, (SCREENHEIGHT - WINDOWHEIGHT) / 2)
                            windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
                            pygame.display.set_caption('Score Show')
                            DISPLAYSURF.fill(BGCOLOR)

                            BASICFONT_1 = pygame.font.Font('Comici.ttf', 38)
                            BASICFONT_2 = pygame.font.Font('Comici.ttf', 28)
                            gf.drawText_2(winner, BASICFONT_1, windowSurface, 330, 130)
                            gf.drawText_2("Player 1's current score is " + str(score_1), BASICFONT_2, windowSurface,
                                          225, 200)
                            gf.drawText_2("Player 2's current score is " + str(score_2), BASICFONT_2, windowSurface,
                                          225, 250)
                            Scoreimage = {'show': pygame.image.load('scoreshow.png'),
                                          'top': pygame.image.load('huizhang.jpg'),
                                          'title': pygame.image.load('winner.png')}
                            SHRect_1 = Scoreimage['show'].get_rect()
                            image_position = 300
                            SHRect_1.top = image_position
                            SHRect_1.centerx = HALF_WINWIDTH
                            image_position += SHRect_1.height
                            windowSurface.blit(Scoreimage['show'], SHRect_1)
                            SHRect_2 = Scoreimage['title'].get_rect()
                            image_position = 50
                            SHRect_2.top = image_position
                            SHRect_2.centerx = HALF_WINWIDTH
                            image_position += SHRect_2.height
                            windowSurface.blit(Scoreimage['title'], SHRect_2)
                            SHRect_3 = Scoreimage['top'].get_rect()
                            image_position = 46
                            SHRect_3.top = image_position
                            SHRect_3.centerx = 346
                            image_position += SHRect_3.height
                            windowSurface.blit(Scoreimage['top'], SHRect_3)
                            pygame.display.flip()
                            time.sleep(10)
                            return
            break

        gf.update_screen(ai_settings, screen, man, man_2, initial_ordinary, ordinary_1, ordinary_2, ordinary_3,
                         macadam_2, conveyer, stick)


if __name__ == '__main__':
    main()
