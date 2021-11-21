
import pygame


def init():

    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption('Drone Navigation Control')


def keypress(key_name):
    result = False
    for event in pygame.event.get():
        pass
    key_press = pygame.key.get_pressed()
    user_key = getattr(pygame, 'K_{}'.format(key_name))
    if key_press[user_key]:
        result = True
    pygame.display.update()
    return result
