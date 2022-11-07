import time
import tkinter as tk
from PIL import Image

filepath = "./src/028/tomato.png"
img = Image.open(filepath)

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Tahoma"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
WIN_HEIGHT = img.height + 10  # add 10 for padding
WIN_WIDTH = img.width + 10
IMG_HEIGHT = int(img.height / 2)
IMG_WIDTH = int(img.width / 2)

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# ---------------------------- UI SETUP ------------------------------- #
class PomodoroApp:
    def __init__(self):
        super().__init__()
        self.frame = tk.Tk()
        self.frame.title("Pomodoro")
        self.frame.minsize(width=WIN_WIDTH, height=WIN_HEIGHT)
        self.frame.config(bg=YELLOW, padx=50, pady=25)
        self.tomato_img = tk.PhotoImage(file=filepath)
        self.odd_even = 1
        self.canvas = tk.Canvas(
            self.frame,
            width=WIN_WIDTH,
            height=WIN_HEIGHT,
            bg=YELLOW,
            highlightthickness=0,
        )
        self.canvas.create_image(
            IMG_WIDTH, IMG_HEIGHT + 5, image=self.tomato_img
        )  # 100x111
        self.starting_time = 1 * 60
        self.mins, self.secs = divmod(self.starting_time, 60)
        self.timer_value = "{:02d}:{:02d}".format(self.mins, self.secs)
        self.timer_text = self.canvas.create_text(
            IMG_WIDTH + 7,
            (WIN_HEIGHT / 2) + 15,
            text=self.timer_value,
            fill="white",
            font=(FONT_NAME, 35, "normal"),
        )
        self.canvas.grid(row=1, column=1, sticky="n")
        self.label = tk.Label(
            text="Timer", font=("Courier", 40, "bold"), fg=GREEN, bg=YELLOW
        )
        self.label.grid(column=1, row=0)
        self.start_button = tk.Button(
            text="Start",
            font=(FONT_NAME, 12, "normal"),
            highlightthickness=0,
            command=self.pomodoro_timer,
        )
        self.start_button.grid(column=0, row=2)
        self.reset_button = tk.Button(
            text="Reset",
            font=(FONT_NAME, 12, "normal"),
            highlightthickness=0,
            command=self.reset_timer,
        )
        self.reset_button.grid(column=2, row=2)
        self.checkmark = tk.Label(
            text="",
            fg=GREEN,
            bg=YELLOW,
            font=(FONT_NAME, 20, "normal"),
        )
        self.checkmark.grid(column=1, row=3)

    def reset_timer(self):
        self.label.config(text="Work", fg=GREEN)
        self.update_times(25)

    def update_times(self, minutes):
        minutes *= 60
        new_mins, new_secs = divmod(minutes, 60)
        self.mins = new_mins
        self.secs = new_secs
        self.timer_value = "{:02d}:{:02d}".format(new_mins, new_secs)
        self.canvas.itemconfig(self.timer_text, text=self.timer_value)
        self.pomodoro_timer()

    def odd_even_func(self):
        if self.odd_even % 2 == 0:  # if even
            self.label.config(text="Break", fg=PINK)
            self.update_times(5)
        elif self.odd_even == 8:  # if 8th rep
            self.label.config(text="Long Break", fg="blue")
            self.update_times(20)
        elif self.odd_even > 8:
            self.label.config(text="Done", fg=RED)
            self.canvas.itemconfig(self.timer_text, text="00:00")
        else:
            self.reset_timer()  # if odd

    def update_checkmark(self):
        if int(self.odd_even) > 1:
            rep_completed = int(self.odd_even) / 2
            new_checkmarks = []
            for _ in range(rep_completed):
                new_checkmarks.append(chr(10004))
                self.checkmark.config(text=" ".join(new_checkmarks))

    def pomodoro_timer(self):
        converted_mins = int(self.mins * 60)
        count = int(self.secs) + int(converted_mins)
        if int(count) > 0:
            self.frame.after(1000, self.pomodoro_timer)
            count = int(count) - 1
            new_mins, new_secs = divmod(count, 60)
            self.mins = new_mins
            self.secs = new_secs
            self.timer_value = "{:02d}:{:02d}".format(new_mins, new_secs)
            self.canvas.itemconfig(self.timer_text, text=self.timer_value)
        else:  # if count < 0 then change odd_even
            self.update_checkmark()
            self.odd_even += 1
            self.odd_even_func()


if __name__ == "__main__":
    app = PomodoroApp()
    app.frame.mainloop()
