#project 4
#rock paper scissor game

import random

def get_winner(user, computer):
    if user == computer:
        return "It's a tie!"#if user input is same as computer choice
    #game rules
    rules = {
        "rock": ["scissor", "pin"],
        "paper": ["rock"],
        "scissor": ["paper"],
        "pin": ["paper", "scissor"]
    }

    if computer in rules[user]:
        return "You win!"#if games goes under the rules and user winning than it will return this
    else:
        return "Computer wins!"#if user fails

def main():
    choices=["rock","paper","scissor","pin"]#choices in game user can choose any of this so as computer
    user_choice=input('Enter your choice(Rock,paper,scissor or pin): ')
    if user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, scissor, or pin.")#error
        return
    system_choice=random.choice(choices)#computer randomly choose any
    print(f"Your choice={user_choice},Computer choice={system_choice}")#printing both choices
    #result
    result = get_winner(user_choice, system_choice)
    print(result)

if __name__ == '__main__':
    main()
