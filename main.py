from tkinter import *
import random
import words

WHITE = "#ffffff"

words = words.common_words
random_words = []

for i in range(250):
    word = random.choice(words)
    random_words.append(word)


# -------- UI Setup -------- #

window = Tk()
window.title("Typing Speed Test")
window.config(padx=70, pady=70, bg=WHITE)


# -------- Logo -------- #

logo_canvas = Canvas(width=250, height=333, highlightthickness=0, bg=WHITE)
logo_img = PhotoImage(file="typing-test-logo.png")
logo_canvas.create_image(125, 166, image=logo_img)
logo_canvas.grid(column=2, row=0)

window.mainloop()
