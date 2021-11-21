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


def main():
    screen = pygame.display.set_mode((1000, 400))

    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)
    font = pygame.font.Font('freesansbold.ttf', 50)

    message_1 = 'Controls:'
    text_1 = font.render(message_1, True, green, blue)
    rect_1 = text_1.get_rect()
    rect_1.center = (1000 // 2, 200 // 2)

    message_2 = 'W=Up S=Down A=Left D=Right'
    text_2 = font.render(message_2, True, green, blue)
    rect_2 = text_2.get_rect()
    rect_2.center = (1000 // 2, 400 // 2)

    run = True
    while run:
        screen.fill(white)
        screen.blit(text_1, rect_1)
        screen.blit(text_2, rect_2)
        if keypress("a"):
            print("left")
        if keypress("d"):
            print("right")
        if keypress("w"):
            print("up")
        if keypress("s"):
            print("down")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                run = False
            pygame.display.update()


if __name__ == '__main__':
    init()
    main()
