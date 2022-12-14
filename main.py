from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")

def next_card():
    pass

window = Tk()
window.title("Flash Card Ultra")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=400, height=263)
canvas.create_text(200, 75, text="title", font=("Ariel", 20, "italic"))
canvas.create_text(200, 150, text="word", font=("Ariel", 30, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=next_card)
known_button.grid(row=1, column=1)


window.mainloop()