#Write a simple joke bot. The bot starts by asking the user what they want. However, your program will only respond to one response: Joke.

import random

PROMPT=str(input('What do you want: '))#user input joke
SORRY=str("Sorry!I only tell jokes.")#if user input any other word than joke it will print this
JOKE=[ #joke template any joke from this will randomly print when user input will be joke 
   "Here is a joke for you!\nWhy do programmers prefer dark mode? Because the light attracts bugs! ",
    "Here is a joke for you!\nWhat do you call 8 hobbits? A hobbyte.",
    "Here is a joke for you!\nWhat will you call the father of chicken?You will call him chicken ke-bab",
    "Here is a joke for you!\n How many programmers does it take to change a light bulb? None. That's a hardware problem.",
    "Here is a joke for you!\nI told my computer I needed a break, and now it won’t stop sending me beach wallpapers.",
    "Here is a joke for you!\nWhy did the computer show up at work late? It had a hard drive."
]

def main(user_input):
    user_input=user_input.strip().lower()

    if "joke" in user_input:
        print(random.choice(JOKE))#calling JOKE Response
    else:
        print(SORRY)    #response
if __name__ == "__main__":
    main(PROMPT)