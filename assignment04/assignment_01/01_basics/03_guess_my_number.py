#Guess my number
import random
def main():

    num=random.randint(0,100)

    print("I am guessing a number between 0 and 100")
    while True:
     guess_number=int(input('Enter a number: '))

     if guess_number < num:
        print("Your guess is to low⬇️")
     elif guess_number > num:
        print("Your guess is to high⬆️")
     else:
        print("Congrats!You guessed it right🎉")
        break
if __name__ == '__main__':
    main()