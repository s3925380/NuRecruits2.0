import key_press_module as key
from djitellopy import Tello
from time import sleep
import pygame
import cv2
import numpy as np
import sys
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'
key.init()
medical_drone = Tello()
medical_drone.connect()
print(medical_drone.get_battery())
medical_drone.streamon()


def control_drone():
    left_right, back_forward, up_down, yaw = 0, 0, 0, 0
    speed = 50

    if key.keypress("RETURN"):
        flight_height = medical_drone.get_height()
        if flight_height == 0:
            medical_drone.takeoff()
            sleep(2)
            auto = True
            while auto:
                if key.keypress("BACKSPACE"):
                    print("Ending Automatic Mode")
                    auto = False
                    break
                medical_drone.move_forward(150)
                if key.keypress("BACKSPACE"):
                    print("Ending Automatic Mode")
                    auto = False
                    break
                sleep(1)
                medical_drone.rotate_clockwise(90)
                if key.keypress("BACKSPACE"):
                    print("Ending Automatic Mode")
                    auto = False
                    break
                sleep(1)
            medical_drone.send_rc_control(0, 0, 0, 0)
            return [left_right, back_forward, up_down, yaw]
        else:
            auto = True
            while auto:
                if key.keypress("BACKSPACE"):
                    print("Ending Automatic Mode")
                    auto = False
                    break
                medical_drone.move_forward(150)
                if key.keypress("BACKSPACE"):
                    print("Ending Automatic Mode")
                    auto = False
                    break
                medical_drone.rotate_clockwise(90)
                if key.keypress("BACKSPACE"):
                    print("Ending Automatic Mode")
                    auto = False
                    break
            medical_drone.send_rc_control(0, 0, 0, 0)
            return [left_right, back_forward, up_down, yaw]

    if key.keypress("a"):
        left_right = -speed
    elif key.keypress("d"):
        left_right = speed

    if key.keypress("w"):
        back_forward = speed
    elif key.keypress("s"):
        back_forward = -speed

    if key.keypress("UP"):
        up_down = speed
    elif key.keypress("DOWN"):
        up_down = -speed

    if key.keypress("LEFT"):
        yaw = -speed
    elif key.keypress("RIGHT"):
        yaw = speed

    if key.keypress("x"):
        flight_height = medical_drone.get_height()
        if flight_height != 0:
            medical_drone.land()
        else:
            pass
    elif key.keypress("SPACE"):
        flight_height = medical_drone.get_height()
        if flight_height == 0:
            medical_drone.takeoff()
        else:
            pass

    return [left_right, back_forward, up_down, yaw]


screen = pygame.display.set_mode((1000, 800))

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
red = (255, 0, 0)
font = pygame.font.Font('freesansbold.ttf', 30)
font1 = pygame.font.Font('freesansbold.ttf', 50)

message_1 = 'Controls:'
text_1 = font1.render(message_1, True, red, white)
rect_1 = text_1.get_rect()
rect_1.center = (1000 // 2, 100 // 2)

message_2 = 'Left - A  Right - D  Forward - W  Back - S'
text_2 = font.render(message_2, True, blue, white)
rect_2 = text_2.get_rect()
rect_2.center = (1000 // 2, 250 // 2)

message_3 = 'Ascend - UP  Descend - DOWN  Rotate - LEFT/RIGHT'
text_3 = font.render(message_3, True, blue, white)
rect_3 = text_3.get_rect()
rect_3.center = (1000 // 2, 350 // 2)

message_4 = 'Take off - SPACEBAR  Land - X'
text_4 = font.render(message_4, True, blue, white)
rect_4 = text_4.get_rect()
rect_4.center = (1000 // 2, 450 // 2)

message_5 = 'Start Auto - ENTER  Cancel Auto - BACKSPACE'
text_5 = font.render(message_5, True, red, white)
rect_5 = text_5.get_rect()
rect_5.center = (1000 // 2, 550 // 2)


run = False
while not run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            medical_drone.get_frame_read().stop()
            medical_drone.streamoff()

            run = True
    control = control_drone()
    medical_drone.send_rc_control(control[0], control[1], control[2], control[3])
    img = medical_drone.get_frame_read().frame
    img = cv2.resize(img, (720, 480))

    frame = np.fliplr(img)
    frame = np.rot90(frame)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    surface = pygame.surfarray.make_surface(frame)
    screen.fill(white)
    screen.blit(text_1, rect_1)
    screen.blit(text_2, rect_2)
    screen.blit(text_3, rect_3)
    screen.blit(text_4, rect_4)
    screen.blit(text_5, rect_5)
    screen.blit(surface, (140, 300))
    cv2.waitKey(1)

pygame.quit()
sys.exit()




'''
MIT License

Copyright (c) 2018 DAMIÀ FUENTES ESCOTÉ

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''
