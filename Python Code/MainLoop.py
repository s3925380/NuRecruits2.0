import tkinter as tk
import time
import threading

switch = True
root = tk.Tk()


def program1():
    def run():
        while (switch == True):
            print('Running program 1')
            time.sleep(0.5)
            if switch == False:
                break

    thread = threading.Thread(target=run)
    thread.start()


def auto():

    global switch
    switch = True
    print('Initiating Automatic Control')
    program1()


def manual():
    print('Initiating Manual Control')
    global switch
    switch = False


def kill():
    root.destroy()


onbutton = tk.Button(root, text="Auto", command=auto)
onbutton.pack()
offbutton = tk.Button(root, text="Manual", command=manual)
offbutton.pack()
killbutton = tk.Button(root, text="EXIT", command=kill)
killbutton.pack()

root.mainloop()
