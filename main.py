from tkinter import *
from tkinter.scrolledtext import ScrolledText
import random
import math
import words

WHITE = "#ffffff"
timer = None
counter_started = False

words = words.common_words
random_words = ""

for i in range(250):
    word = random.choice(words)
    random_words = random_words + word + " "


# -------- Functions -------- #


def start_countdown(args):
    global counter_started
    if not counter_started:
        count_down(60)
        counter_started = True
    else:
        pass


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    timer_label.config(text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = root.after(1000, count_down, count - 1)


# -------- UI Setup -------- #

root = Tk()
root.title("Typing Speed Test")
root.config(padx=70, pady=70, bg=WHITE)


# -------- Logo -------- #

logo_canvas = Canvas(width=250, height=333, highlightthickness=0, bg=WHITE)
logo_img = PhotoImage(file="typing-test-logo.png")
logo_canvas.create_image(125, 166, image=logo_img)
logo_canvas.grid(column=2, row=0)


# -------- Timer -------- #

timer_label = Label(text="01:00", bg=WHITE, font=("Courier New", 24, "bold"))
timer_label.config(padx=20, pady=20)
timer_label.grid(column=2, row=1)

# -------- Text Canvas -------- #

frame1 = Frame(root, width=4000, height=500)
frame1.config(padx=50, pady=50, bg=WHITE)
frame1.grid(column=2, row=2)
text_scrollbar = Scrollbar(frame1, orient=VERTICAL)
text_canvas = Canvas(frame1, width=500, height=400, bg=WHITE)
text_canvas.grid(column=0, row=0)
text_scrollbar.grid(column=1, row=0, sticky="ns")
text_to_type = text_canvas.create_text(250, 150, text=random_words, font=("Courier New", 12, "normal"), width=490)
text_scrollbar.config(command=text_canvas.yview)
text_canvas.config(yscrollcommand=text_scrollbar.set, scrollregion=text_canvas.bbox("all"))
text_canvas.yview_moveto('0.0')


# -------- Text Canvas -------- #

entry = ScrolledText(frame1, height=22, width=50, font=("Courier New", 12, "normal"))
entry.grid(column=2, row=0)
entry.bind('<Key>', start_countdown)

root.mainloop()
