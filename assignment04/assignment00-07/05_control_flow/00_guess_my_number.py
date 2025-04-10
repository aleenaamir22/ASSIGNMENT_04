#guessing number game
import random
def main():

    number=random.randint(0,100)

    print('\033[1m\033[3m 🤔 I am thinking of a number between 0 and 100\033[0m ')
    while True:
       guess=int(input('Guess a integer number:'))

       if guess < number:
        print('Your guess is to Low')
       elif guess > number:
        print('Your guess is to high') 
       else:
        print(f"Congrats you guessed it right.The number was {number}")      
        break
if __name__ == '__main__':
    main()    