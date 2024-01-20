import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors) : ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player" : player_choice , "computer" : computer_choice}
    
    return choices

def check_win(player,computer):
    # print("You chose " + player + "Computer chose " + computer)
    print(f"You chose {player}, Computer chose {computer}") 
    if player == computer:
        return "its a tie"
    elif player == "rock":
        if computer == "paper":
            return "paper covers the rock! you lose."
        else:
            return "rock smashes scissors! you win"
    elif player == "paper":
        if computer == "rock":
            return "paper covers the rock! you win."
        else:
            return "scissors cuts the paper! you lose"

    elif player == "scissors":
        if computer == "rock":
            return "rock smashes scissors! you lose."
        else:
            return "scissor cuts the paper! you win"
    
# choices = get_choices()
# p_choice = choices["player"]    #when use print insted of return
# c_choice = choices["computer"]
# check_win(p_choice, c_choice)

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)