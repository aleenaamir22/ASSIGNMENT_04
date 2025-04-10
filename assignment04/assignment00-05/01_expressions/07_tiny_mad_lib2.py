import random

def main():
    adj = input('Enter an adjective: ')
    noun = input('Enter a noun (living thing): ')
    verb = input('Enter a verb: ')

    templates = [
        f"The {adj} {noun} loves to {verb} in the rain!",
        f"Every evening, a {adj} {noun} would {verb} on the rooftop.",
        f"Can a {adj} {noun} really {verb} like that?",
        f"Once upon a time, a {adj} {noun} tried to {verb} a watermelon.",
        f"The {adj} {noun} could {verb} every weekend!"
    ]

    print("\n" + random.choice(templates))

if __name__ == '__main__':
    main()
