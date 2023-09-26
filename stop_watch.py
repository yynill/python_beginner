# on stop and reset wired numbers - idk ?

import tkinter
import time

# create window + set attributes
window = tkinter.Tk()
window.title("Stopwatch")
window.minsize(width=250, height=250)

start_time = 0
running = False


def update_label(label, ms_label):
    current_time = time.time()
    elapsed_time = current_time - start_time
    hours = int(elapsed_time) // 3600
    minutes = int(elapsed_time % 3600) // 60
    seconds = int(elapsed_time) % 60
    milliseconds = int((elapsed_time % 1) * 1000) // 10

    time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    ms_string = f"{milliseconds:02d}"

    label['text'] = time_string
    ms_label['text'] = ms_string

    if running:
        label.after(113, update_label, label, ms_label)


def start(label):
    global running
    global start_time
    if not running:
        start_time = time.time() - start_time
        running = True
        update_label(label, ms_label)


def stop():
    global running
    if running:
        global start_time
        start_time = time.time() - start_time
        running = False


def reset(label):
    global running
    global start_time
    start_time = 0
    running = False
    label['text'] = "00:00:00"
    ms_label['text'] = "00"


f_top = tkinter.Frame(window)

label = tkinter.Label(f_top, text="00:00:00",
                      fg="black", font="Verdana 30 bold")
label.pack(side="left")

ms_label = tkinter.Label(
    f_top, text="00", fg="darkgray", font="Verdana 15")
ms_label.pack(side="bottom")

f = tkinter.Frame(window)

# creating buttons
start_button = tkinter.Button(
    f, text='Start', width=6, command=lambda: start(label))
stop_button = tkinter.Button(
    f, text='Stop', width=6, command=lambda: stop())
reset_button = tkinter.Button(
    f, text='Reset', width=6, command=lambda: reset(label))

# adding buttons to window + align
f_top.pack(anchor='center', pady=5)
f.pack(anchor='center', pady=5)
start_button.pack(side="left")
stop_button.pack(side="left")
reset_button.pack(side="left")

window.mainloop()
