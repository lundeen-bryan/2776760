def rock_game():
    rock = '''
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
            ______)
            _______)
            _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    '''

    #Write your code below this line 👇
    import random

    #Opening screen
    print(
        '''
        Welcome to another game of Rock, Paper, Scissors!

        Here are the rules:
        - Rock beats Scissors
        - Scissors beats Paper
        - Paper beats Rock
        '''
    )

    #get random pick
    random_pick = random.randint(1,3)

    #ask user what choice they want
    user_pick = input(
        '''
        Choose either:
            R for Rock,
            P for Paper, or
            S for Scissors
        to continue or
            X to Exit the game.
        '''
    )
    while user_pick not in {"R","P","S","X"}:
        user_pick = input("Please chose either R, P, or S to continue")

    #users choice
    if user_pick == "R":
        print("You chose Rock!")
        print(rock)
    elif user_pick == "P":
        print("You chose Paper!")
        print(paper)
    elif user_pick == "S":
        print("You chose Scissors!")
        print(scissors)
    elif user_pick == "X":
        exit(0)

    #the computer's choice
    if random_pick == 1:
        print("The computer chose Rock!")
        print(rock)
    elif random_pick == 2:
        print("The computer chose Paper!")
        print(scissors)
    elif random_pick == 3:
        print("The computer chose Scissors!")
        print(paper)

    #evaluate the user's choice vs the computer's choice

    #user picks Rock
    if user_pick == "R" and random_pick == 1:
        print("Start over, you and the computer tied.")
    elif user_pick == "R" and random_pick == 2:
        print("Rock beats Scissors! You Win!")
    elif user_pick == "R" and random_pick == 3:
        print("Paper beats Rock! You Lose!")
    #user picks Paper
    elif user_pick == "P" and random_pick == 1:
        print("Paper beats Rock! You Win!")
    elif user_pick == "P" and random_pick == 2:
        print("Start over, you and the computer tied.")
    elif user_pick == "P" and random_pick == 3:
        print("Scissors beats Paper! You Lose!")
    #user picks Scissors
    elif user_pick == "S" and random_pick == 1:
        print("Rock beats Scissors! You Lose!")
    elif user_pick == "S" and random_pick == 2:
        print("Scissors beats Paper! You Win!")
    elif user_pick == "S" and random_pick == 3:
        print("Start over, you and the computer tied.")
    return

#display option to play the game or exit
play_game = input("Do you want to play a game of Rock, Paper, Scissors? \nType Y for yes and N for no to continue...")
play_game = play_game.capitalize()

if play_game == "Y":
    rock_game()
else:
    exit(0)
