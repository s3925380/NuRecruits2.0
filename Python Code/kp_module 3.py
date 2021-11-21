import pygame


def init():
    pygame.init()
    screen = pygame.display.set_mode((400,400))
    pygame.display.set_caption('Drone Navigation Control')


def get_key(key_name):
    result = False
    for event in pygame.event.get(): pass
    key_press = pygame.key.get_pressed()
    user_key = getattr(pygame, 'K_{}'.format(key_name))
    if key_press[user_key]:
        result = True
    pygame.display.update()
    return result


def main():
    # Run until the user asks to quit
    run = True
    while run:

        if get_key("a"):
            print("left")
        if get_key("d"):
            print("right")
        if get_key("w"):
            print("up")
        if get_key("s"):
            print("down")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


if __name__ == '__main__':
    init()
    main()