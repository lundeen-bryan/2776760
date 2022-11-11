"""========================================="""
# =            Import Section                  =
"""========================================="""
from PIL import Image
import password_application_cls
import generate_password_cls
import sys

sys.path.insert(0, "./src/")  # imports file_control.py from this parent folder
from _clear_console import clear
import dictionaries as dc

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
# =========  End of Constants Section  =======


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
    See dictionaries.py for all parameters
    Calls to:
         Sends list to app.create_label
    """
    app.create_label(*arguments_list)
    app.frame.update()


def create_textbox(arguments_list):
    """Takes a list of items and unpacks it to use as arguments to create a textbox
    See dictionaries.py for all parameters
    Calls to:
         Sends list to app.create_textbox
    """
    app.create_textbox(*arguments_list)
    app.frame.update()


def create_button(arguments_list):
    """Takes a list of items and unpacks it to use as arguments to create a textbox
    See dictionaries.py for all parameters
    Calls to:
         Sends list to app.create_textbox
    """
    app.create_button(*arguments_list)
    app.frame.update()


def check_character_len():
    app.check_character_len
    verified_length = pw.password_len_verified()
    if verified_length == True:
        password.insert(
            0, pw.get_all_characters(letter_count, number_count, symbol_count)
        )



# =========  End of Functions Section  =======

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def button_pressed(button):
    pass

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

if __name__ == "__main__":
    clear()
    app = password_application_cls.PasswordApplication()
    pw = generate_password_cls.GeneratePassword()
    update()
    create_label(dc.label_dictionary["for_website_label"].values())
    create_label(dc.label_dictionary["for_email_label"].values())
    create_label(dc.label_dictionary["for_password_label"].values())
    create_label(dc.label_dictionary["for_letter_count_label"].values())
    create_label(dc.label_dictionary["for_number_count_label"].values())
    create_label(dc.label_dictionary["for_symbol_count_label"].values())
    create_label(dc.label_dictionary["for_alias_textbox_label"].values())
    letter_count = create_textbox(dc.textbox_dictionary["for_letter_count_textbox"].values())
    number_count = create_textbox(dc.textbox_dictionary["for_number_count_textbox"].values())
    symbol_count = create_textbox(dc.textbox_dictionary["for_symbol_count_textbox"].values())
    alias = create_textbox(dc.textbox_dictionary["for_alias_textbox"].values())
    website = create_textbox(dc.textbox_dictionary["for_website_textbox"].values())
    email = create_textbox(dc.textbox_dictionary["for_email_textbox"].values())
    password = create_textbox(dc.textbox_dictionary["for_password_textbox"].values())
    generate_btn = create_button(dc.button_dictionary["for_password_button"].values())
    save_btn = create_button(dc.button_dictionary["for_save_button"].values())
    reset_btn = create_button(dc.button_dictionary["for_reset_button"].values())
    exit_btn = create_button(dc.button_dictionary["for_exit_button"].values())

    app.frame.mainloop()