"""========================================="""
# =            Import Section                  =
"""========================================="""
from PIL import Image
import password_application_cls
import generate_password_cls

# =========  End of Import Section      =======

"""========================================="""
# =       Constants Section                    =
"""========================================="""
FILEPATH = "./src/029/logo.png"
IMG = Image.open(FILEPATH)
WIN_HEIGHT = IMG.height  # add 10 for padding
WIN_WIDTH = IMG.width
IMG_HEIGHT = int(IMG.height / 2)
IMG_WIDTH = int(IMG.width / 2)
FONT_NAME = "Tahoma"
BACKGROUND = "white"
letters = ""
numbers = ""
symbols = ""
# =========  End of Constants Section  =======

"""========================================="""
# =              Lists Section                 =
"""========================================="""
website_label = [
    "Website: ",
    17,
    1,
    "black",
    "white",
    "Tahoma",
    12,
    "normal",
    0,
    2,
    "e",
]
email_label = [
    "Email/Username: ",
    17,
    1,
    "black",
    "white",
    "Tahoma",
    12,
    "normal",
    0,
    3,
    "e",
]
password_label = [
    "Password: ",
    17,
    1,
    "black",
    "white",
    "Tahoma",
    12,
    "normal",
    0,
    4,
    "e",
]
ltr_slider_label = [
    "Number of Letters: ",
    17,
    1,
    "black",
    "white",
    "Tahoma",
    12,
    "normal",
    0,
    5,
    "e",
]
num_slider_label = [
    "Number of Numbers: ",
    17,
    1,
    "black",
    "white",
    "Tahoma",
    12,
    "normal",
    0,
    6,
    "e",
]
sym_slider_label = [
    "Number of Symbols: ",
    17,
    1,
    "black",
    "white",
    "Tahoma",
    12,
    "normal",
    0,
    7,
    "e",
]
alias_label = [
    "Alias for Website: ",
    17,
    1,
    "black",
    "white",
    "Tahoma",
    12,
    "normal",
    0,
    8,
    "e",
]
alias_txtbx = [
    25,
    1,
    "black",
    "white",
    "Tahoma",
    12,
    "normal",
    1,
    8,
    5,
    5,
    1,
    "w",
    5,
    5,
]
website_txtbx = [
    55,
    1,
    "black",
    "white",
    "Tahoma",
    12,
    "normal",
    1,
    2,
    5,
    5,
    2,
    "w",
    5,
    5,
]
email_txtbx = [
    35,
    1,
    "black",
    "white",
    "Tahoma",
    12,
    "normal",
    1,
    3,
    5,
    5,
    1,
    "w",
    5,
    5,
    "bigbry2k3@gmail.com"
]
password_txtbx = [
    35,
    1,
    "black",
    "white",
    "Tahoma",
    12,
    "normal",
    1,
    4,
    5,
    5,
    1,
    "w",
    5,
    5,
]
generate_password_button = [
    "Generate Password",
    16,
    1,
    "black",
    "white",
    "Tahoma",
    12,
    "normal",
    2,
    3,
    "center",
    0,
    0,
    0,
    10,
    "check_character_len"
]
save_button = [
    "Save Info",
    16,
    1,
    "black",
    "white",
    "Tahoma",
    12,
    "normal",
    2,
    4,
    "center",
    0,
    0,
    0,
    3,
]
reset_button = [
    "Reset Form",
    16,
    1,
    "black",
    "white",
    "Tahoma",
    12,
    "normal",
    2,
    5,
    "center",
    0,
    0,
    0,
    3,
]
exit_button = [
    "Exit",
    16,
    1,
    "black",
    "white",
    "Tahoma",
    12,
    "normal",
    2,
    6,
    "center",
    0,
    0,
    0,
    3,
]
letter_count_txtbx = [
    2,
    1,
    "black",
    "white",
    "Tahoma",
    12,
    "normal",
    1,
    5,
    5,
    5,
    1,
    "w",
    5,
    5,
]
number_count_txtbx = [
    2,
    1,
    "black",
    "white",
    "Tahoma",
    12,
    "normal",
    1,
    6,
    5,
    5,
    1,
    "w",
    5,
    5,
]
symbol_count_txtbx = [
    2,
    1,
    "black",
    "white",
    "Tahoma",
    12,
    "normal",
    1,
    7,
    5,
    5,
    1,
    "w",
    5,
    5,
]
# =========  End of Lists Section   =======


"""========================================="""
# =           Functions Section                =
"""========================================="""

def update():
    """After the tkinter obj is created, this updates the values passed from main"""
    app.frame.after(
        1000,
        app.update_values(
            WIN_HEIGHT,
            WIN_WIDTH,
            FILEPATH,
            BACKGROUND,
            IMG_HEIGHT,
            IMG_WIDTH,
            25,
            25,
        ),
    )


def create_label(arguments_list):
    """Takes a list of items and unpacks it to use as arguments to create a label

    Args:
        display_text (string): the text on the label
        label_width (int): width of label, should be # of characters or the longest in the column
        label_height (int): height of label, usually measured by lines default=1
        foreground (string): color of text
        background (string): color of background
        font_name (string): font type for text on label
        font_size (int): size in pixels of font
        font_style (string): either bold, italic, normal
        label_column (int): location on the grid in column
        label_row (int): location on the grid in row
        alignment (string): w gives left alignment of text, e gives right alignment

    Calls to:
         Sends list to app.create_label
    """
    app.create_label(*arguments_list)
    app.frame.update()


def create_textbox(arguments_list):
    """Takes a list of items and unpacks it to use as arguments to create a textbox

    Args:
        display_text (string): the text on the textbox
        box_width (int): width of textbox, should be # of characters or the longest in the column
        box_height (int): height of textbox, usually measured by lines default=1
        foreground (string): color of text
        background (string): color of background
        font_name (string): font type for text on textbox
        font_size (int): size in pixels of font
        font_style (string): either bold, italic, normal
        box_column (int): location on the grid in column
        box_row (int): location on the grid in row

    Calls to:
         Sends list to app.create_textbox
    """
    app.create_textbox(*arguments_list)
    app.frame.update()


def create_button(arguments_list):
    """Takes a list of items and unpacks it to use as arguments to create a textbox

    Args:
        display_text (string): the text on the textbox
        box_width (int): width of textbox, should be # of characters or the longest in the column
        box_height (int): height of textbox, usually measured by lines default=1
        foreground (string): color of text
        background (string): color of background
        font_name (string): font type for text on textbox
        font_size (int): size in pixels of font
        font_style (string): either bold, italic, normal
        box_column (int): location on the grid in column
        box_row (int): location on the grid in row

    Calls to:
         Sends list to app.create_textbox
    """
    app.create_button(*arguments_list)
    app.frame.update()

def check_character_len():
  verified_length = pw.password_len_verified()
  if verified_length == True:
    password.insert(0, pw.get_all_characters(letter_count, number_count, symbol_count))

# =========  End of Functions Section  =======

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def button_pressed(button):
  pass
# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

if __name__ == "__main__":
    app = password_application_cls.PasswordApplication()
    pw = generate_password_cls.GeneratePassword()
    update()
    create_label(website_label)
    create_label(email_label)
    create_label(password_label)
    create_label(ltr_slider_label)
    create_label(num_slider_label)
    create_label(sym_slider_label)
    create_label(alias_label)
    alias = create_textbox(alias_txtbx)
    website = create_textbox(website_txtbx)
    email = create_textbox(email_txtbx)
    password = create_textbox(password_txtbx)
    generate_btn = create_button(generate_password_button)
    save_btn = create_button(save_button)
    reset_btn = create_button(reset_button)
    exit_btn = create_button(exit_button)
    letter_count = create_textbox(letter_count_txtbx)
    number_count = create_textbox(number_count_txtbx)
    symbol_count = create_textbox(symbol_count_txtbx)

    app.frame.mainloop()
