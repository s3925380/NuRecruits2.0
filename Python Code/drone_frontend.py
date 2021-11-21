
from drone_backend import *
from djitellopy import Tello
from time import sleep
import pygame
import cv2
import numpy as np
import sys
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
medical_drone = Tello()
medical_drone.connect()
print(medical_drone.get_battery())
medical_drone.streamon()


def control_drone():
    left_right, back_forward, up_down, yaw = 0, 0, 0, 0
    speed = 50
    if keypress("ESCAPE"):
        medical_drone.get_frame_read().stop()
        medical_drone.streamoff()
        pygame.quit()
        sys.exit()
    if keypress("RETURN"):
        flight_height = medical_drone.get_height()
        if flight_height == 0:
            screen.blit(text_6, rect_6)
            pygame.display.update()
            medical_drone.takeoff()
            sleep(2)
            auto = True
            while auto:
                screen.blit(text_6, rect_6)
                pygame.display.update()
                if keypress("BACKSPACE"):
                    print("Ending Automatic Mode")
                    auto = False
                    break
                medical_drone.move_forward(150)
                if keypress("BACKSPACE"):
                    print("Ending Automatic Mode")
                    auto = False
                    break
                sleep(1)
                medical_drone.rotate_clockwise(90)
                if keypress("BACKSPACE"):
                    print("Ending Automatic Mode")
                    auto = False
                    break
                sleep(1)
            medical_drone.send_rc_control(0, 0, 0, 0)
            return [left_right, back_forward, up_down, yaw]
        else:
            auto = True
            while auto:
                screen.blit(text_6, rect_6)
                pygame.display.update()
                if keypress("BACKSPACE"):
                    print("Ending Automatic Mode")
                    auto = False
                    break
                medical_drone.move_forward(150)
                if keypress("BACKSPACE"):
                    print("Ending Automatic Mode")
                    auto = False
                    break
                sleep(1)
                medical_drone.rotate_clockwise(90)
                if keypress("BACKSPACE"):
                    print("Ending Automatic Mode")
                    auto = False
                    break
                sleep(1)
            medical_drone.send_rc_control(0, 0, 0, 0)
            return [left_right, back_forward, up_down, yaw]

    if keypress("a"):
        left_right = -speed
    elif keypress("d"):
        left_right = speed

    if keypress("w"):
        back_forward = speed
    elif keypress("s"):
        back_forward = -speed

    if keypress("UP"):
        up_down = speed
    elif keypress("DOWN"):
        up_down = -speed

    if keypress("LEFT"):
        yaw = -speed
    elif keypress("RIGHT"):
        yaw = speed

    if keypress("x"):
        flight_height = medical_drone.get_height()
        if flight_height != 0:
            screen.blit(text_6, rect_6)
            pygame.display.update()
            medical_drone.land()
        else:
            pass
    elif keypress("SPACE"):
        flight_height = medical_drone.get_height()
        if flight_height == 0:
            screen.blit(text_6, rect_6)
            pygame.display.update()
            medical_drone.takeoff()
            sleep(2)
        else:
            pass

    if keypress("i"):
        stats = "Battery:" + str(medical_drone.get_battery()) + " "
        stats += "Temperature:" + str(medical_drone.get_temperature()) + " "
        stats += "Height:" + str(medical_drone.get_height()) + " "
        stats += "Flight Time:" + str(medical_drone.get_flight_time()) + " "
        stats += "Distance TOF:" + str(medical_drone.get_distance_tof()) + " "
        stats += "Speed x:" + str(medical_drone.get_speed_x()) + " "
        stats += "Speed y:" + str(medical_drone.get_speed_y()) + " "
        stats += "Speed z:" + str(medical_drone.get_speed_z()) + " "
        stats += "Acceleration:" + str(medical_drone.get_acceleration_x()) + " "
        print(stats)

    return [left_right, back_forward, up_down, yaw]


screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption('Drone Navigation Control')

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

message_6 = 'CAMERA UNAVAILABLE'
text_6 = font1.render(message_6, True, red, blue)
rect_6 = text_6.get_rect()
rect_6.center = (1000 // 2, 1100 // 2)

run = False
while not run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            medical_drone.get_frame_read().stop()
            medical_drone.streamoff()
            pygame.quit()
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
