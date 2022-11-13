# from https://testingonprod.com/2021/10/24/how-to-send-text-messages-with-python-for-free/
import smtplib
import sys

CARRIERS = {
    "att": "@mms.att.net",
    "tmobile": "@tmomail.net",
    "verizon": "@vtext.com",
    "sprint": "@messaging.sprintpcs.com"
}

USER_INFO = {}

def get_user_input():
  print(f"Please enter your name below:")
  name = input("> ").strip()
  print(f"Please enter your phone number below:")
  phone_number = input("> ").strip()
  print(f"Please enter your email address:")
  email = input("> ").strip()
  print(f"Please enter the password for your email account:")
  password = input("> ").strip()
  print("CARRIERS:")
  for ea in CARRIERS.keys():
    print(f"\t\t{ea}")
  print("Please enter the name of one of the carriers above:")
  carrier = input("> ").strip()
  USER_INFO[name]["phone_number"] = phone_number
  USER_INFO[name]["email"] = email
  USER_INFO[name]["password"] = password
  USER_INFO[name]["carrier"] = carrier

def send_message(phone_number, carrier, message):
    recipient = phone_number + CARRIERS[carrier]
    auth = (EMAIL, PASSWORD)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(auth[0], auth[1])

    server.sendmail(auth[0], recipient, message)


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print(f"Usage: python3 {sys.argv[0]} <PHONE_NUMBER> <CARRIER> <MESSAGE>")
        sys.exit(0)

    phone_number = sys.argv[1]
    carrier = sys.argv[2]
    message = sys.argv[3]

    send_message(phone_number, carrier, message)