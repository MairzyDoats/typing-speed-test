from tkinter import *
from tkinter.scrolledtext import ScrolledText
import os.path
import random
import math
import words

WHITE = "#ffffff"
timer = None
counter_started = False

words = words.common_words
random_words_list = []
random_words = ""

if os.path.isfile("last_score.txt"):
    with open(file="last_score.txt", mode="r") as file:
        data = file.read()
        if data == "":
            score = 0
        else:
            score = int(data)
else:
    score = 0

if os.path.isfile("highscore.txt"):
    with open(file="highscore.txt", mode="r") as file:
        data = file.read()
        if data == "":
            highscore = score
        else:
            highscore = int(data)
else:
    highscore = score


# -------- Functions -------- #


def generate_words():
    global random_words_list
    global random_words
    random_words_list = []
    random_words = ""
    while len(random_words_list) < 250:
        word = random.choice(words)
        if word not in random_words_list:
            random_words_list.append(word)

    for word in random_words_list:
        random_words = random_words + word + " "


def reset():
    global counter_started
    counter_started = False
    timer_label.config(text="1:00")
    generate_words()
    entry.config(state=NORMAL)
    entry.delete("1.0", END)
    text_to_type.config(state=NORMAL)
    text_to_type.delete("1.0", END)
    text_to_type.insert(END, random_words)
    text_to_type.config(state=DISABLED)


def compare():
    typed_words = entry.get("1.0", END).split(" ")
    matches = set(typed_words) & set(random_words_list)
    score = len(matches) + 1
    update_highscore(score)
    entry.insert(END, f"\n\nYou have written {score} words in one minute!")
    entry.config(state=DISABLED)


def update_highscore(score):
    with open(file="last_score.txt", mode="w") as file:
        file.write(f"{score}")
    if os.path.isfile("highscore.txt"):
        with open(file="highscore.txt") as file:
            data = file.read()
        with open(file="highscore.txt", mode="r+") as file:
            if data == "":
                file.write(f"{score}")
                highscore = score
            else:
                highscore = int(file.read())
                if score > highscore:
                    file.seek(0)
                    file.write(f"{score}")
                    highscore = score

    else:
        with open(file="highscore.txt", mode="w") as file:
            file.write(f"{score}")
            highscore = score
    high_score_label.config(text=f"Highscore: {highscore}")
    last_score_label.config(text=f"Last score: {score}")


def start_countdown(args):
    global counter_started
    if not counter_started:
        counter_started = True
        count_down(60)
    else:
        pass


def count_down(count):
    global counter_started
    if counter_started:
        count_min = math.floor(count / 60)
        count_sec = count % 60
        if count_sec < 10:
            count_sec = f"0{count_sec}"
        timer_label.config(text=f"{count_min}:{count_sec}")

        if count > 0:
            global timer
            timer = root.after(1000, count_down, count - 1)
        else:
            compare()


generate_words()


# -------- UI Setup -------- #

root = Tk()
root.title("Typing Speed Test")
root.config(padx=70, pady=70, bg=WHITE)

# -------- Logo -------- #

logo_canvas = Canvas(width=150, height=200, highlightthickness=0, bg=WHITE)
logo_img = PhotoImage(file="typing-test-logo.png")
logo_canvas.create_image(75, 100, image=logo_img)
logo_canvas.grid(column=2, row=0)

# -------- Timer -------- #

timer_label = Label(text="1:00", bg=WHITE, font=("Courier New", 24, "bold"))
timer_label.config(padx=20, pady=20)
timer_label.grid(column=2, row=1)
reset_button = Button(text="Reset",
                      font=("Lucinda Grande", 14, "normal"),
                      command=lambda: reset(),
                      bg=WHITE)
reset_button.grid(column=2, row=2)

# -------- Text Canvas -------- #

frame1 = Frame(root, width=4000, height=500)
frame1.config(padx=50, pady=50, bg=WHITE)
frame1.grid(column=2, row=3)
high_score_label = Label(frame1,
                         text=f"Highscore: {highscore}",
                         font=("Lucinda Grande", 12, "normal"),
                         bg=WHITE)
high_score_label.config(padx=20, pady=20)
high_score_label.grid(column=0, row=0)
last_score_label = Label(frame1,
                         text=f"Last score: {score}",
                         font=("Lucinda Grande", 12, "normal"),
                         bg=WHITE)
last_score_label.config(padx=20, pady=20)
last_score_label.grid(column=1, row=0)
text_to_type = ScrolledText(frame1,
                            height=15,
                            width=50,
                            font=("Courier New", 12, "normal"),
                            wrap="word")
text_to_type.insert(END, random_words)
text_to_type.config(state=DISABLED)
text_to_type.grid(column=0, row=1)
text_to_type.yview_moveto("0.0")

# -------- Text Canvas -------- #

entry = ScrolledText(frame1,
                     height=15,
                     width=50,
                     font=("Courier New", 12, "normal"),
                     wrap="word")
entry.grid(column=1, row=1)
entry.bind('<Key>', start_countdown)

root.mainloop()
