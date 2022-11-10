import tkinter as tk

"""============================================
=            Class Section                    =
============================================"""


class PasswordApplication:
    def __init__(self):
        super().__init__()
        self.frame = tk.Tk()
        self.title = "Password Manager"
        self.frame.title(self.title)
        self.win_height = 100
        self.win_width = 1000
        self.img_filepath = "./src/029/logo.png"
        self.image = tk.PhotoImage(file=self.img_filepath)
        self.bg_color = "white"
        self.x_padding = 10
        self.y_padding = 10
        self.img_height = 400
        self.img_width = 400
        self.label_website = "Website: "
        self.label_email = "Email/Username: "
        self.label_pass = "Password: "
        self.label_generate = "Generate Password"
        self.label_add = "Add"

    def create_frame(self):
        self.frame.minsize(width=self.win_width, height=self.win_height)
        self.frame.config(
            bg=self.bg_color, padx=self.x_padding, pady=self.y_padding
        )
        self.title = "New Tkinter Frame"

    def create_canvas(self):
        self.canvas = tk.Canvas(
            self.frame,
            width=self.win_width,
            height=self.win_height,
            bg=self.bg_color,
            highlightthickness=0,
        )
        self.canvas.create_image(
            self.img_width,
            self.img_height,
            image=self.image,
        )  # 100x111
        self.canvas.grid(row=1, column=1, sticky="n", pady=20)

    def create_label(
        self,
        display_text="Label",
        label_width=10,
        label_height=1,
        foreground="black",
        background="white",
        font_name="Tahoma",
        font_size=12,
        font_style="normal",
        label_column=0,
        label_row=0,
        label_align="w",
    ):
        self.label = tk.Label(
            text=display_text,
            width=label_width,
            height=label_height,
            fg=foreground,
            bg=background,
            font=(font_name, font_size, font_style),
            anchor=label_align,
            highlightthickness=0,
        )
        self.label.grid(row=label_row, column=label_column)

    def create_textbox(
        self,
        default_text="",
        txtbox_width=10,
        txtbox_height=1,
        foreground="black",
        background="white",
        font_name="Tahoma",
        font_size=12,
        font_style="normal",
        txtbox_column=0,
        txtbox_row=0,
        x_padding=0,
        y_padding=0,
        span_columns=1,
        txtbox_align="w",
        grid_xpad=0,
        grid_ypad=0,
    ):
        self.textbox = tk.Text(
            width=txtbox_width,
            height=txtbox_height,
            font=(font_name, font_size, font_style),
            fg=foreground,
            bg=background,
            padx=x_padding,
            pady=y_padding,
            highlightthickness=0,
        )
        self.textbox.grid(
            row=txtbox_row,
            column=txtbox_column,
            columnspan=span_columns,
            sticky=txtbox_align,
            padx=grid_xpad,
            pady=grid_ypad,
        )
        self.textbox.insert("1.0", default_text)

    def create_button(
        self,
        display_text="Label",
        button_width=10,
        button_height=1,
        foreground="black",
        background="white",
        font_name="Tahoma",
        font_size=12,
        font_style="normal",
        button_column=0,
        button_row=0,
        button_align="w",
        x_padding=0,
        y_padding=0,
        grid_xpad=0,
        grid_ypad=0,
        call_func=None,
    ):
        self.button = tk.Button(
            text=display_text,
            width=button_width,
            height=button_height,
            fg=foreground,
            bg=background,
            font=(font_name, font_size, font_style),
            anchor=button_align,
            padx=x_padding,
            pady=y_padding,
            command=call_func,
        )
        self.button.grid(row=button_row, column=button_column, padx=grid_xpad, pady=grid_ypad)

    def update_values(
        self,
        win_height,
        win_width,
        imaage_filepath,
        bg_color,
        img_height,
        img_width,
        xpadding,
        ypadding,
    ):
        self.win_height = win_height
        self.win_width = win_width
        self.img_filepath = imaage_filepath
        self.bg_color = bg_color
        self.img_height = img_height
        self.img_width = img_width
        self.x_padding = xpadding
        self.y_padding = ypadding
        self.create_frame()
        self.create_canvas()


"""========  End of Class Section          ====
"""
