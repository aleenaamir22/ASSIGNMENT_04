#03_wholesome_machine
#Write a program which prompts the user to type an affirmation of your choice

def main():
        affirmation="I am growing, learning, and becoming the best version of myself every day." #affirmation
        
        while True:   
          print(f'Please enter the given affirmation: {affirmation}')#print the initial line

          user_input=input(f'Enter the affirmation here: ')#user input the affirmation
       
          if user_input == affirmation:
              print("✅That's Right")#if user enter the correct affirmation than reponse will be this
              break
          else:
              print('❌That was not the affirmation ')     #if user enter the wrong affirmation than reponse will be this
              
              


if __name__ == '__main__':
    main()    