import random
def get_choice():
    player_choices = input("Input you choices {Rcok,Paper,Ceaser} : ")
    options=["Rcok","Paper","Ceaser"]
    computer_choice = random.choice(options)
    choices={"Player":player_choices,"Computer":computer_choice}
    return choices
def check_win(player,computer):
    print(f'You chosse {player} and computer chosse {computer}.')
    if player == computer:
        print("It's a tie!")
    else:
        print("It's a win!")
        return
choices=get_choice()
check_win(choices["Player"],choices["Computer"])
