#05_double_it
#Write a program that asks a user to enter a number. Your program will then double that number and print out the result.

def main():
    print("🔁 Double Your Number Until It Reaches 100 or More")#printed msg

    user_input = int(input("Enter a number (integer): "))#user input

    while user_input < 100:#loop
        user_input = user_input * 2
        print(user_input, end=" ")#response
    
if __name__ == '__main__':
    main()
