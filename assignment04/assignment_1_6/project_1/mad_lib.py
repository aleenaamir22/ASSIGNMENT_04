import random

def main():
    # User input - adjectives
    print("Enter 6 adjectives one by one:")
    user_input_adj1 = input("Enter your first adjective: ")
    user_input_adj2 = input("Enter your second adjective: ")
    user_input_adj3 = input("Enter your third adjective: ")
    user_input_adj4 = input("Enter your fourth adjective: ")
    user_input_adj5 = input("Enter your fifth adjective: ")
    user_input_adj6 = input("Enter your sixth adjective: ")

    # Nouns
    print("Enter 3 nouns one by one:")
    user_input_noun1 = input("Enter your first noun: ")
    user_input_noun2 = input("Enter your second noun: ")
    user_input_noun3 = input("Enter your third noun (plural if you want): ")

    # Verbs
    print("Enter 4 verbs one by one:")
    user_input_verb1 = input("Enter your first verb: ")
    user_input_verb2 = input("Enter your second verb: ")
    user_input_verb3 = input("Enter your third verb: ")
    user_input_verb4 = input("Enter your fourth verb: ")

    #Random Paragraph 
    paragraphs = [

        f"""Yesterday, I saw a {user_input_adj1} {user_input_noun1} trying to {user_input_verb1} on top of a {user_input_adj2} {user_input_noun2}.
It was so {user_input_adj3} that I had to {user_input_verb2} twice before realizing I wasn’t dreaming.
Then, a group of {user_input_adj4} {user_input_noun3}s showed up and started to {user_input_verb3} like there was no tomorrow.
Honestly, it was the most {user_input_adj5} thing I’ve ever seen—right after that time I accidentally {user_input_verb4} into a {user_input_adj6} sandwich.""",

        f"""One time at summer camp, a {user_input_adj1} {user_input_noun2} decided to {user_input_verb1} while wearing a {user_input_adj2} hat made out of {user_input_noun1}.
Everyone thought it was {user_input_adj3}, but then it started to {user_input_verb2} and got stuck in a tree.
Suddenly, a {user_input_adj4} {user_input_noun3} appeared and began to {user_input_verb3} with absolutely no explanation.
By the end of the day, the whole camp was {user_input_verb4} and someone painted the mess with a {user_input_adj5} brush shaped like a {user_input_adj6} balloon.""",

        f"""My pet {user_input_noun1} is a bit {user_input_adj1}. Last weekend it tried to {user_input_verb1} across a {user_input_adj2} {user_input_noun2}.
It ended up in a {user_input_adj3} puddle and started to {user_input_verb2} uncontrollably.
Soon a {user_input_adj4} {user_input_noun3} rolled by, and they both began to {user_input_verb3} together.
It was the most {user_input_adj5} day ever—until I {user_input_verb4} into a {user_input_adj6} hedge!""",

        f"""In a {user_input_adj1} land far away, a {user_input_noun1} set out to {user_input_verb1} the legendary {user_input_adj2} {user_input_noun2}.
With a {user_input_adj3} cape and a dream, it managed to {user_input_verb2} across treacherous terrain.
A {user_input_adj4} army of {user_input_noun3}s tried to stop it but were too distracted by its ability to {user_input_verb3}.
Eventually, the hero {user_input_verb4} into the sunset, victorious and smelling like {user_input_adj5} {user_input_adj6} cheese."""
    ]

    #printing random para with user input
    selected_paragraph = random.choice(paragraphs)
    print("\nYour Random Funny Story\n")
    print(selected_paragraph)

if __name__ == '__main__':
    main()
