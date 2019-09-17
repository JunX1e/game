import sys

import pygame

from ball import ball1
from em import zhouqi
from kunkun import kunkun1
import music as Music

def check_keydown_events(event, ai_settings, screen, kunkun, balls):
    if event.key == pygame.K_RIGHT:
        kunkun.moving_right = True
    elif event.key == pygame.K_LEFT:
        kunkun.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire(ai_settings, screen, kunkun, balls)
    elif event.key == pygame.K_ESCAPE:
        sys.exit()
    elif event.key == pygame.K_z:
        Music.play(10)
        # Music.clock(10)



def check_keyup_event(event, kunkun):
    if event.key == pygame.K_RIGHT:
        kunkun.moving_right = False
    elif event.key == pygame.K_LEFT:
        kunkun.moving_left = False

def check_events(ai_settings, screen, kunkun, balls):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, kunkun, balls)

        elif event.type == pygame.KEYUP:
            check_keyup_event(event, kunkun)

def get_number_zhouqis_x(ai_settings, zhouqi_width):
    available_space_x = ai_settings.screen_width - 2 * zhouqi_width
    number_zhouqi_x = int(available_space_x / (2 * zhouqi_width))
    return number_zhouqi_x

def get_number_rows(ai_settings, kunkun_height, zhouqi_height):
    available_space_y = (ai_settings.screen_height - 3*zhouqi_height - kunkun_height)
    number_rows = int(available_space_y / (2*kunkun_height))
    return number_rows

def create_zhouqi(ai_settings, screen, zhouqis, zhouqi1_number, row_number):
    zhouqi1 = zhouqi(ai_settings, screen)
    zhouqi1_width = zhouqi1.rect.width
    zhouqi1.x = zhouqi1_width + 2 * zhouqi1_width * zhouqi1_number
    zhouqi1.rect.y = zhouqi1.rect.height + 2*zhouqi1.rect.height*row_number
    zhouqi1.rect.x = zhouqi1.x
    zhouqis.add(zhouqi1)


def create_fleet(ai_settings, screen, kunkun, zhouqis):
    zhouqi1 =zhouqi(ai_settings, screen)
    number_zhouqis_x = get_number_zhouqis_x(ai_settings, zhouqi1.rect.width )

    number_rows = get_number_rows(ai_settings, kunkun.rect.height/1.25, zhouqi1.rect.height)

    for row_number in range(number_rows):
         for zhouqi1_number in range(number_zhouqis_x):
              create_zhouqi(ai_settings, screen, zhouqis, zhouqi1_number, row_number)

def update_screen(ai_settings, screen, kunkun, zhouqis, balls):

    screen.fill(ai_settings.bg_color)

    for ball in balls.sprites():
        ball.draw_ball()
    kunkun.blitme()
    zhouqis.draw(screen)
    pygame.display.flip()


def update_ball(zhouqis, balls):
    balls.update()

    for ball in balls.copy():
        if ball.rect.bottom <= 0:
            balls.remove(ball)

    collisions = pygame.sprite.groupcollide(balls, zhouqis, True, True)


def fire(ai_settings, screen, kunkun, ball):
    if len(ball) < ai_settings.ball_allowed:
        new_ball = ball1(ai_settings, screen, kunkun)
        ball.add(new_ball)

def update_zhouqis(ai_settings, zhouqis):
    check_fleet_edges(ai_settings, zhouqis)
    zhouqis.update()

def check_fleet_edges(ai_settings, zhouqis):

    for zhouqi in zhouqis.sprites():
        if zhouqi.check_edges():
            change_fleet_direction(ai_settings, zhouqis)
            break


def change_fleet_direction(ai_settings, zhouqis):

    for zhouqi in zhouqis.sprites():
        zhouqi.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

