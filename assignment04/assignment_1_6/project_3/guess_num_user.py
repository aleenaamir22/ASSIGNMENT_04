#guessing number game(user)
import random

def main():
    print("🤔 Guessing Number Game (User)")#printing
    print("Can you guess the number between 1 and 100?")#printing 
    number=random.randint(1,100)#range
    attempts = 0

    while True:
        try:
            user_input = int(input("Enter your guess: "))#user input
            attempts += 1#attempt count

            if user_input < number:
                print("Too low! Try again.")#if the guessed number is low
            elif user_input > number:
                print("Too high! Try again.")#if the guess number is high
            else:
                print(f"🎉 You guessed it right! The number was {number}.")#response
                print(f"You got it right {attempts} attempts.")#printing attempt
                break
        except ValueError:
         print("Please enter a valid number.") #error      
if __name__ =='__main__':
    main()    