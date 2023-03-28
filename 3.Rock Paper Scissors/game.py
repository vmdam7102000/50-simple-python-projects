from random import randint

def get_computer_decision() -> int:
    com_rand = randint(0,2)
    return com_rand

def get_user_decision() -> int:
    print("Enter your choice \n 0: Rock \n 1: Paper \n 2: Scissors")
    choice = int(input())
    return choice

def game_play(user_choice, com_choice):

    if user_choice == com_choice:
        print("it's a draw!")

    elif user_choice == 0:
        if com_choice == 1:
            print("you lose")
        else:
            print("you win")

    elif user_choice == 1:
        if com_choice == 2:
            print("you lose")
        else:
            print("you win")

    elif user_choice == 2:
        if com_choice == 0:
            print("you lose")
        else:
            print("you win")


if __name__ == '__main__':
    while True:
        try:
            user_choice = get_user_decision()
        except ValueError as e:
            print("invalid selection")
            continue
        com_choice = get_computer_decision()
        game_play(user_choice,com_choice)

        play_again = input("play again? (y/n)")
        if play_again.lower() == 'n':
            break