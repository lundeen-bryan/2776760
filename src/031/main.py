"""========================================="""
# =            Imports Section                 =
"""========================================="""

import json
import random
import sys
import tkinter as tk
import os

sys.path.insert(0, "./src/")  # imports file_control.py from this parent folder
import css  # py file holding styles
from PIL import Image # use to get source image parameters

# =========  End of Imports Section      =======

"""========================================="""
# =           Constants Section                =
"""========================================="""
BG = css.BACKGROUND_HEX_COLOR
SIDE_2_BG = css.SIDE_2_BACKGROUND
PARENT_FOLDER = "./src/031/"
FRONT_PATH = PARENT_FOLDER + "images/card_front.png"
BACK_PATH = PARENT_FOLDER + "images/card_back.png"
FRONT_IMG = Image.open(FRONT_PATH)
BACK_IMG = Image.open(BACK_PATH)
FRONT_FONT_COLOR = "black"
BACK_FONT_COLOR = "white"
IMG_HEIGHT = int(FRONT_IMG.height)
IMG_WIDTH = int(FRONT_IMG.width)
WIN_WIDTH = IMG_WIDTH
WIN_HEIGHT = IMG_HEIGHT
LANG_FONT = ("Arial", 40, "italic")  # font properties are a tuple
WORD_FONT = ("Arial", 60, "bold")  # font properties are a tuple
TIMER_FONT = ("Arial", 18, "bold")  # font properties are a tuple
TRADEMARK = "\u2122"  # this is a unicode string for trademark
TIMER_COUNTDOWN_START_VALUE = 4


# =========  End of Constants Section      =======

"""========================================="""
# =             Class Section                  =
"""========================================="""


class FlashCardApp:
    def __init__(self):
        super().__init__()
        self.frame = tk.Tk()
        self.frame.title(f"Flashy - The Flash Card App! by BryCo{TRADEMARK}")
        self.frame.minsize(width=WIN_WIDTH, height=WIN_HEIGHT)
        self.frame.config(bg=BG, padx=50, pady=50)
        self.canvas = tk.Canvas(
            self.frame,
            width=WIN_WIDTH,
            height=WIN_HEIGHT,
            bg=BG,
            highlightthickness=0,
        )
        self.image = tk.PhotoImage(file=FRONT_PATH)
        self.img_height = IMG_HEIGHT
        self.img_width = IMG_WIDTH
        self.image_size = (int(IMG_WIDTH / 2), int(IMG_HEIGHT / 2))
        self.canvas_image = self.canvas.create_image(
            self.image_size, image=self.image
        )  # image size is a tuple
        self.canvas.grid(row=1, column=0, sticky="n", columnspan=2)
        self.side = 1
        self.learned_list = []
        self.button_no_image = tk.PhotoImage(
            file=PARENT_FOLDER + "images/wrong.png"
        )
        self.button_no = tk.Button(
            image=self.button_no_image,
            bd=0,
            bg=BG,
            command=self.flip,
            highlightthickness=0,
        )
        self.button_no.grid(row=2, column=0)
        self.button_yes_image = tk.PhotoImage(
            file=PARENT_FOLDER + "images/right.png",
        )
        self.button_yes = tk.Button(
            image=self.button_yes_image,
            bd=0,
            bg=BG,
            command=self.learned_word,
            highlightthickness=0,
        )
        self.button_yes.grid(row=2, column=1)
        self.french_word = "none"
        self.english_word = "none"
        self.language_selected = "French"
        self.language_label = tk.Label(
            text=self.language_selected.capitalize(),
            bg="white",
            fg="black",
            font=(LANG_FONT),
        )
        self.language_label.place(relx=0.5, rely=0.25, anchor="center")
        self.word_selected = self.french_word
        self.word_label = tk.Label(
            text=self.word_selected.lower(),
            bg="white",
            fg="black",
            font=(WORD_FONT),
        )
        self.word_label.place(
            relx=0.5,
            rely=0.45,
            anchor="center",
        )
        self.timer_value = TIMER_COUNTDOWN_START_VALUE
        self.timer_text = "{:02d}".format(self.timer_value)
        self.timer_label = tk.Label(
            text=f"Seconds Remaining: {self.timer_text}",
            bg="white",
            fg="black",
            font=(TIMER_FONT),
        )
        self.timer_label.place(relx=0.5, rely=0.1, anchor="center")
        self.load_learned_list()
        self.get_word()
        self.side_1()

    def load_learned_list(self):
        with self.open_text_file("r") as text_file:
            for line in text_file:
                ea_line = line[:-1]
                self.learned_list.append(ea_line)
        print(self.learned_list)

    def get_word(self):
        """changes the word on the card with new words"""
        with self.open_json("r") as word_file:
            data = json.load(word_file)
            key_list = list(data.keys())
            key = random.choice(key_list)
            while key in self.learned_list:
                key = random.choice(key_list)
            french = data[key]["French"]
            english = data[key]["English"]
            self.french_word = french
            self.english_word = english

    def countdown(self):
        count = int(self.timer_value)
        if int(count) > 0:
            self.frame.after(1000, self.countdown)
            count = int(count) - 1
            self.timer_value = count
            self.timer_text = "{:02d}".format(count)
            self.timer_label.config(
                text=f"Seconds Remaining: {self.timer_text}"
            )
        else:
            self.timer_value = TIMER_COUNTDOWN_START_VALUE
            self.timer_text = "{:02d}".format(self.timer_value)
            self.timer_label.config(
                text=f"Seconds Remaining: {self.timer_text}"
            )
            self.flip()

    def flip(self):
        if self.side == 1:
            self.side = 2
            self.side_2()
        else:
            self.side = 1
            self.side_1()

    def side_1(self):
        """holds parameters for the first side of the card"""
        self.get_word()
        new_image = tk.PhotoImage(file=FRONT_PATH)
        self.image = new_image
        self.canvas.itemconfig(self.canvas_image, image=new_image)
        self.language_label.config(
            text="French", bg="white", fg=FRONT_FONT_COLOR
        )
        self.word_label.config(
            text=self.french_word, bg="white", fg=FRONT_FONT_COLOR
        )
        self.timer_label.config(
            text="{:02d}".format(self.timer_value),
            bg="white",
            fg=FRONT_FONT_COLOR,
        )
        self.countdown()

    def side_2(self):
        """holds parameters for the second side of the card"""
        new_image = tk.PhotoImage(file=BACK_PATH)
        self.image = new_image
        self.canvas.itemconfig(self.canvas_image, image=new_image)
        self.language_label.config(
            text="English", bg=SIDE_2_BG, fg=BACK_FONT_COLOR
        )
        self.word_label.config(
            text=self.english_word, bg=SIDE_2_BG, fg=BACK_FONT_COLOR
        )
        self.timer_label.config(text="", bg=SIDE_2_BG, fg=BACK_FONT_COLOR)

    def learned_word(self):
        self.learned_list.append(self.french_word)
        with self.open_text_file("a") as text_file:
            text_file.write(f"{self.french_word}\n")
        self.flip()

    def open_json(self, mode="r"):
        """opens a json file returns contents, much faster than pandas on the csv"""
        path = PARENT_FOLDER + "data/french_words.json"
        if check_file_path(path) == True:
            data_file = open(
                path, mode, encoding="utf-8"
            )
            return data_file
        else:
            show_msg("File or Folder Not Found", f"Sorry, but {path} doesn't exist.")

    def open_text_file(self, mode="r"):
        path = PARENT_FOLDER + "data/learned_words.txt"
        if check_file_path(path) == True:
            text_file = open(
                path, mode, encoding="utf-8"
            )
            return text_file
        else:
            show_msg("File or Folder Not Found", f"Sorry, but {path} doesn't exist.")

def check_file_path(path):
    path_exists = os.path.exists(path)
    return path_exists

def show_msg(title, message):
    from tkinter import ttk

    root = tk.Tk()
    root.title(title)
    root.resizable(False, False)
    root.geometry("")

    options = {"fill": "both", "padx": 10, "pady": 10, "ipadx": 5}

    ttk.Label(
        root, text=f"{message}"
    ).pack(**options)
    root.mainloop()

# =========  End of Class Section         =======

# main function
if __name__ == "__main__":
    app = FlashCardApp()
    app.frame.mainloop()
