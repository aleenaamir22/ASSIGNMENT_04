#tiny mad lib 07
#Write a program which prompts the user for an adjective, then a noun, then a verb, and then prints a fun sentence with those words!

def main():
     adj=input('Please enter an adjective:  ')#user input adj
     noun=input('Please enter a noun(living things):  ')#user input noun
     verb=input('Please enter a verb:  ')#user input verb
     
     sentence=(f'The {adj} {noun} could {verb} every evening!')#combining sentence

     print(sentence)#response


if __name__ == '__main__':
    main()    