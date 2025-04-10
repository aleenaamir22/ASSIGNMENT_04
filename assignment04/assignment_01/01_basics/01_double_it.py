#basic double it
#Write a program that asks a user to enter a number. Your program will then double that number and print out the result. It will repeat that process until the value is 100 or greater.

def main():
    print("Double your number")#printed message
    user_input=int(input('Enter a number: '))#user input

    while user_input <= 100:#loop
       user_input = user_input * 2
       print(user_input , end=" ")#printing response

if __name__ == '__main__':
    main()