import keyboard
while True:
    if keyboard.is_pressed('a'):
        print('left pressed')
    elif keyboard.is_pressed('w'):
        print('up pressed')
    elif keyboard.is_pressed('s'):
        print('down pressed')
    elif keyboard.is_pressed('d'):
        print('right pressed')
    elif keyboard.is_pressed('x'):
        print('Exit')
        break
