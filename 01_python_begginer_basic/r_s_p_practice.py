# rock paper scissor 
import random
def get_choices():
    player_choice = input("Enter your choice (rock/paper/scissor) : ")
    options = ["rock", "paper", "scissor"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose : {player} , computer chose : {computer}")
    if player == computer:
        return "It's a tie!!"
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

    elif player == "scissor":
        if computer == "rock":
            return "rock smashes scissors! you lose."
        else:
            return "scissor cuts the paper! you win"
    
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)