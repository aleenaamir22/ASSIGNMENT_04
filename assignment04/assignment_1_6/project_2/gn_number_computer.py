#guessing number game(computer)
import random

def main():
    number=(1,100)#range
    computer_guess=(random.randint(number[0],number[1]))#computer guessing a random number

    print("🤔Guessing number game(computer)")#printed
    print("Can you guess the number between 1 and 100")#printed
    print(f'The number was:{computer_guess}')#response
if __name__ =='__main__':
    main()    