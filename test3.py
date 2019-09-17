import sys

import pygame
from pygame.sprite import Group
from test3set import Settings
from kunkun import kunkun1
import kunkunfunctions as kf
from em import zhouqi



def run_game():
    pygame.init()
    ai_settings=Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("test3")
    kunkun = kunkun1(ai_settings, screen)
    balls = Group()
    #start main loop
    zhouqis = Group()

    kf.create_fleet(ai_settings, screen, kunkun, zhouqis)

    while True :
        kf.check_events(ai_settings, screen, kunkun, balls)
        # kf.check_events(kunkun)
        kunkun.update()

        kf.update_ball( zhouqis, balls)
        kf.update_zhouqis(ai_settings, zhouqis)
        kf.update_screen(ai_settings, screen, kunkun, zhouqis, balls)
        # visiable
        # kf.update_screen(ai_settings, screen , kunkun)


run_game()


