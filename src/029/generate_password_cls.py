import random

"""========================================="""
# =             Class Section                  =
"""========================================="""


class GeneratePassword:
    def __init__(self):
        super().__init__()
        self.password_list = ""
        self.total_characters = 0
        self.password = ""
        self.total_letters = ""
        self.letters = [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "K",
            "L",
            "M",
            "N",
            "O",
            "P",
            "Q",
            "R",
            "S",
            "T",
            "U",
            "V",
            "W",
            "X",
            "Y",
            "Z",
        ]
        self.numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
        self.letter_count = 0
        self.number_count = 0
        self.symbol_count = 0

    def get_all_characters(self, letters, numbers, symbols):
        self.total_characters = letters + numbers + symbols
        if self.password_len_verified() == True:
            if letters != 0:
                for _ in range(1, letters + 1):
                    self.password_list += str(random.choice(self.letters))
            if numbers != 0:
                for _ in range(1, numbers + 1):
                    self.password_list += str(random.choice(self.numbers))
            if symbols != 0:
                for _ in range(1, symbols + 1):
                    self.password_list += str(random.choice(self.symbols))
        self.randomize_characters()

    def password_len_verified(self):
      if self.total_characters > 8:
        return True
      else:
        return False

    def randomize_characters(self):
        if len(self.password_list) > 0:
            for _ in range(1, self.total_characters + 1):
                self.password += str(random.choice(self.password_list))
        else:
            print("Need to create a length of characters first.")


# =========    End of Class Section      =======
