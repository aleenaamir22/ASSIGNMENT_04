#Problem statement 02
#Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!"
def main():
#asking user their favorite animal name
    user_input=input("\033[1m\033[3m Enter the name of your favorite animal: \033[0m ") #User input will be bold and italic 

    print(f'\033[1m\033[3m My favorite animal is also {user_input}!\033[0m')#in response it will showed up also in bold and italic form

if __name__ == '__main__':
    main()   